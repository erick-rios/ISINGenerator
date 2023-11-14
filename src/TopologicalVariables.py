# Copyright (C) 2023, Erick Jesús Ríos González

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA.

import numpy as np
import scipy.ndimage


class TopologicalVariables:
    """Class for calculating topological variables in a spin matrix."""

    @staticmethod
    def label_ring(matrix:np.ndarray) -> list:
        """
        Label the holes in the spin matrix, considering ring-like boundary conditions.

        Returns:
            list: A list containing the matrix with labels, the number of labels, and the maximum label.
        """
        matrix_copy = matrix.copy() + 1
        labels, num_labels = scipy.ndimage.label(matrix_copy > 0)

        # Correct labels on column borders
        for i in range(labels.shape[0]):
            if matrix_copy[i, 0] > 0 and matrix_copy[i, -1] > 0:
                if labels[i, 0] != labels[i, -1]:
                    labels[labels == labels[i, -1]] = labels[i, 0]

        # Correct labels on row borders
        for j in range(labels.shape[1]):
            if matrix_copy[0, j] > 0 and matrix_copy[-1, j] > 0:
                if labels[0, j] != labels[-1, j]:
                    labels[labels == labels[-1, j]] = labels[0, j]

        if np.array_equal(np.unique(labels), np.array([1])):
            num_labels = 1
        else:
            num_labels = len(np.unique(labels)) - 1

        max_label = np.max(np.unique(labels))

        return [labels, num_labels, max_label]

    @staticmethod
    def find_domains(matrix: np.ndarray) -> np.ndarray:
        """
        Label the holes in the spin matrix, considering boundary conditions.

        Returns:
            np.ndarray: The matrix with labels, taking into account boundary conditions.
        """
        matrix_copy = matrix.copy()
        return TopologicalVariables.label_ring(matrix_copy)[0]
    @staticmethod
    def number_of_domains(matrix: np.ndarray) -> int:
        """
        Count the number of domains in the spin matrix, considering ring-like boundary conditions.

        Returns:
            int: Number of labels in the matrix.
        """
        matrix_copy = matrix.copy()
        return TopologicalVariables.label_ring(matrix_copy)[1]

    @staticmethod
    def length_of_domains(matrix: np.ndarray) -> np.ndarray:
        """
        Calculate the length of domains in the spin matrix, considering ring-like boundary conditions.

        Returns:
            np.ndarray: Number of elements per label in the labels matrix.
        """
        matrix_copy = matrix.copy()
        labels, _, num_features = TopologicalVariables.label_ring(matrix_copy)
        domain_lengths = scipy.ndimage.histogram(
            labels, 0, num_features + 1, num_features + 1
        )[1:]

        return domain_lengths

    @staticmethod
    def mean_domain_size(matrix: np.ndarray) -> float:
        """
        Calculate the average size of domains in the spin matrix, considering ring-like boundary conditions.

        Returns:
            float: Average size of the domains in the matrix.
        """
        matrix_copy = matrix.copy()
        domain_lengths = TopologicalVariables.length_of_domains(matrix_copy)
        mask = domain_lengths != 0
        non_zero_values = domain_lengths[mask]

        if not non_zero_values.any():
            return 0

        mean = np.mean(non_zero_values)

        return mean
    
