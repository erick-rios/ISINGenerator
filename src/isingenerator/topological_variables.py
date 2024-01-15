"""Module a class for compute the Topological Values of the 2D Ising Model"""
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

from typing import List

import numpy as np
import scipy.ndimage



class TopologicalVariables:
    """Class for calculating topological variables in a spin matrix."""

    _labels: np.ndarray = None
    _num_labels: float  = None
    _max_label: float = None
    _domain_lengths : List[float] = None
    
    @staticmethod
    def label_ring(matrix:np.ndarray) -> List:
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
        
        TopologicalVariables._labels = labels
        TopologicalVariables._num_labels = num_labels
        TopologicalVariables._max_label = max_label

        #return [labels, num_labels, max_label]

    @staticmethod
    def find_domains(matrix: np.ndarray = None) -> np.ndarray:
        """
        Label the holes in the spin matrix, considering boundary conditions.

        Returns:
            np.ndarray: The matrix with labels, taking into account boundary conditions.
        """
        #matrix_copy = matrix.copy()
        #return TopologicalVariables.label_ring(matrix_copy)[0]
        if TopologicalVariables._labels is None:
            TopologicalVariables.label_ring(matrix)
        return TopologicalVariables._labels
    
    @staticmethod
    def number_of_domains(matrix: np.ndarray = None) -> int:
        """
        Count the number of domains in the spin matrix, considering ring-like boundary conditions.

        Returns:
            int: Number of labels in the matrix.
        """
        #matrix_copy = matrix.copy()
        #return TopologicalVariables.label_ring(matrix_copy)[1]
        if TopologicalVariables._num_labels is None:
            TopologicalVariables.label_ring(matrix)
        return TopologicalVariables._num_labels

    @staticmethod
    def length_of_domains(matrix: np.ndarray = None) -> np.ndarray:
        """
        Calculate the length of domains in the spin matrix, considering ring-like boundary conditions.

        Args:
            matrix (np.ndarray, optional): The matrix of the microstate. Defaults to None.

        Returns:
            np.ndarray: Number of elements per label in the labels matrix.
        """
        #matrix_copy = matrix.copy()
        #labels, _, num_features = TopologicalVariables.label_ring(matrix)
        if TopologicalVariables._labels is None:
            TopologicalVariables.label_ring(matrix)
        
        labels = TopologicalVariables._labels
        num_features = TopologicalVariables._max_label
        TopologicalVariables._domain_lengths = scipy.ndimage.histogram(
            labels, 0, num_features + 1, num_features + 1
        )[1:]
        
        return TopologicalVariables._domain_lengths

    @staticmethod
    def mean_domain_size(matrix: np.ndarray = None) -> float:
        """
        Calculate the average size of domains in the spin matrix, considering ring-like boundary conditions.

        Args:
            matrix (np.ndarray, optional): Matrix of the microstate. Defaults to None.

        Returns:
            float: Average size of the domains in the matrix.
        """
        #matrix_copy = matrix.copy()
        if TopologicalVariables._domain_lengths is None:
            TopologicalVariables._domain_lengths = TopologicalVariables.length_of_domains(matrix)
        mask = TopologicalVariables._domain_lengths != 0
        non_zero_values = TopologicalVariables._domain_lengths[mask]

        if not non_zero_values.any():
            return 0

        mean = np.mean(non_zero_values)

        return mean
    
    @staticmethod
    def get_num_labels()-> int:
        """
        Returns the number of labels calculated by the las call to label_ring

        Returns:
            int: Number of labels
        """
        return TopologicalVariables._num_labels
    
    @staticmethod
    def get_max_label()->int:
        """
        Returns the maximum label calculated by the las call to label_ring

        Returns: 
            int: Maximum label calculated
        """
        return TopologicalVariables._max_label

    @staticmethod
    def get_labels()->int:
        """
        Returns the maximum label calculated by the las call to label_ring

        Returns: 
            int: Maximum label calculated
        """
        return TopologicalVariables._labels
