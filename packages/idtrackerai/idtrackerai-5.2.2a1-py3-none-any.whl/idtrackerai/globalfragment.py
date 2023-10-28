# This file is part of idtracker.ai a multiple animals tracking system
# described in [1].
# Copyright (C) 2017- Francisco Romero Ferrero, Mattia G. Bergomi,
# Francisco J.H. Heras, Robert Hinz, Gonzalo G. de Polavieja and the
# Champalimaud Foundation.
#
# idtracker.ai is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details. In addition, we require
# derivatives or applications to acknowledge the authors by citing [1].
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# For more information please send an email (idtrackerai@gmail.com) or
# use the tools available at https://gitlab.com/polavieja_lab/idtrackerai.git.
#
# [1] Romero-Ferrero, F., Bergomi, M.G., Hinz, R.C., Heras, F.J.H.,
# de Polavieja, G.G., Nature Methods, 2019.
# idtracker.ai: tracking all individuals in small or large collectives of
# unmarked animals.
# (F.R.-F. and M.G.B. contributed equally to this work.
# Correspondence should be addressed to G.G.d.P:
# gonzalo.polavieja@neuro.fchampalimaud.org)
from typing import Literal, Sequence

import numpy as np

from . import Blob, Fragment
from .utils import load_id_images


class GlobalFragment:
    """Represents a collection of :class:`fragment.Fragment` N different
    animals. Where N is the number of animals in the video as defined by the
    user.

        Parameters
    ----------
    blobs_in_video : list
        List of lists of instances of :class:`blob.Blob`.
    fragments : list
        List of lists of instances of the class :class:`fragment.Fragment`
    first_frame_of_the_core : int
        First frame of the core of the global fragment.
        This also acts as a unique identifier of the global fragment.
    """

    accumulation_step: int | None = None
    """Integer indicating the accumulation step at which the global fragment
    was globally accumulated."""

    duplicated_identities: set
    first_frame_of_the_core: int
    fragments_identifiers: Sequence[int]
    fragments: list[Fragment]
    minimum_distance_travelled: float

    def __init__(
        self,
        blobs_in_video: list[list[Blob]],
        fragments: list[Fragment],
        first_frame_of_the_core: int,
    ):
        self.first_frame_of_the_core = first_frame_of_the_core
        self.fragments_identifiers = tuple(
            blob.fragment_identifier for blob in blobs_in_video[first_frame_of_the_core]
        )
        self.set_individual_fragments(fragments)

        for fragment in self:
            fragment.is_in_a_global_fragment = True

        self.minimum_distance_travelled = min(
            fragment.distance_travelled for fragment in self
        )

    @property
    def min_n_images_per_fragment(self):
        return min(fragment.n_images for fragment in self)

    def __iter__(self):
        return iter(self.fragments)

    @classmethod
    def from_json(cls, data: dict, fragments: list[Fragment] | None):
        global_fragment = cls.__new__(cls)
        if "individual_fragments_identifiers" in data:
            data["fragments_identifiers"] = data.pop("individual_fragments_identifiers")
        global_fragment.__dict__.update(data)
        if "duplicated_identities" in data:
            global_fragment.duplicated_identities = set(data["duplicated_identities"])

        if fragments is not None:
            global_fragment.set_individual_fragments(fragments)

        return global_fragment

    @property
    def used_for_training(self):
        """Boolean indicating if all the fragments in the global fragment
        have been used for training the identification network"""
        return all(fragment.used_for_training for fragment in self)

    def is_unique(self, number_of_animals: int):
        """Boolean indicating that the global fragment has unique
        identities, i.e. it does not have duplications."""
        return {fragment.temporary_id for fragment in self} == set(
            range(number_of_animals)
        )

    @property
    def is_partially_unique(self):
        """Boolean indicating that a subset of the fragments in the global
        fragment have unique identities"""

        identities_acceptable_for_training = [
            fragment.temporary_id
            for fragment in self
            if fragment.acceptable_for_training
        ]
        self.duplicated_identities = {
            x
            for x in identities_acceptable_for_training
            if identities_acceptable_for_training.count(x) > 1
        }
        return len(self.duplicated_identities) == 0

    def set_individual_fragments(self, fragments: list[Fragment]):
        """Gets the list of instances of the class :class:`fragment.Fragment`
        that constitute the global fragment and sets an attribute with such
        list.

        Parameters
        ----------
        fragments : list
            All the fragments extracted from the video.

        """
        self.fragments = [
            fragments[identifier] for identifier in self.fragments_identifiers
        ]

    def acceptable_for_training(
        self, accumulation_strategy: Literal["global", "partial"]
    ) -> bool:
        """Returns True if the global fragment is acceptable for training"""

        return (all if accumulation_strategy == "global" else any)(
            fragment.acceptable_for_training for fragment in self
        )

    @property
    def total_number_of_images(self) -> int:
        """Gets the total number of images in the global fragment"""
        return sum(fragment.n_images for fragment in self)

    def get_images_and_labels(self, id_images_file_paths):
        """Gets the images and identities in the global fragment as a
        labelled dataset in order to train the identification neural network

        If the scope is "pretraining" the identities of each fragment
        will be arbitrary.
        If the scope is "identity_transfer" then the labels will be
        empty as they will be infered by the identification network selected
        by the user to perform the transferring of identities.

        Parameters
        ----------
        id_images_file_paths : list
            List of paths (str) where the identification images are stored.
        scope : str, optional
            Whether the images are going to be used for training the
            identification network or for "pretraining", by default
            "pretraining".

        Returns
        -------
        Tuple
            Tuple with two Numpy arrays with the images and their labels.
        """
        images = []
        labels = []

        for temporary_id, fragment in enumerate(self):
            images += fragment.image_locations
            labels += [temporary_id] * fragment.n_images

        # labels have to be int64, else PyTorch crashes
        return load_id_images(id_images_file_paths, images), np.asarray(
            labels, dtype=np.int64
        )
