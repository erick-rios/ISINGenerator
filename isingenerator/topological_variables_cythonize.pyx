# topological_variables.pyx
import numpy as np
import scipy.ndimage
from numpy cimport ndarray, int_t

class TopologicalVariables:
    cdef ndarray[int_t, ndim=2] _labels
    cdef float _num_labels
    cdef float _max_label
    cdef ndarray[int_t, ndim=1] _domain_lengths

    @staticmethod
    def label_ring(ndarray[int_t, ndim=2] matrix):
        """
        Label the holes in the spin matrix, considering ring-like boundary conditions.

        Returns:
            tuple: A tuple containing the matrix with labels, the number of labels, and the maximum label.
        """
        cdef ndarray[int_t, ndim=2] matrix_copy
        cdef ndarray[int_t, ndim=2] labels
        cdef int_t num_labels
        cdef int_t max_label
        cdef int_t i, j

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

    @staticmethod
    def find_domains(ndarray[int_t, ndim=2] matrix):
        """
        Label the holes in the spin matrix, considering boundary conditions.

        Returns:
            ndarray[int_t, ndim=2]: The matrix with labels, taking into account boundary conditions.
        """
        if TopologicalVariables._labels is None:
            TopologicalVariables.label_ring(matrix)
        return TopologicalVariables._labels

    @staticmethod
    def number_of_domains(ndarray[int_t, ndim=2] matrix):
        """
        Count the number of domains in the spin matrix, considering ring-like boundary conditions.

        Returns:
            int_t: Number of labels in the matrix.
        """
        if TopologicalVariables._num_labels is None:
            TopologicalVariables.label_ring(matrix)
        return TopologicalVariables._num_labels

    @staticmethod
    def length_of_domains(ndarray[int_t, ndim=2] matrix):
        """
        Calculate the length of domains in the spin matrix, considering ring-like boundary conditions.

        Args:
            matrix (ndarray[int_t, ndim=2]): The matrix of the microstate.

        Returns:
            ndarray[int_t, ndim=1]: Number of elements per label in the labels matrix.
        """
        cdef int_t num_features

        if TopologicalVariables._labels is None:
            TopologicalVariables.label_ring(matrix)

        num_features = TopologicalVariables._max_label
        TopologicalVariables._domain_lengths = scipy.ndimage.histogram(
            TopologicalVariables._labels, 0, num_features + 1, num_features + 1
        )[1:]

        return TopologicalVariables._domain_lengths

    @staticmethod
    def mean_domain_size(ndarray[int_t, ndim=2] matrix):
        """
        Calculate the average size of domains in the spin matrix, considering ring-like boundary conditions.

        Args:
            matrix (ndarray[int_t, ndim=2]): Matrix of the microstate.

        Returns:
            float: Average size of the domains in the matrix.
        """
        cdef ndarray[int_t, ndim=1] non_zero_values

        if TopologicalVariables._domain_lengths is None:
            TopologicalVariables._domain_lengths = TopologicalVariables.length_of_domains(matrix)

        non_zero_values = TopologicalVariables._domain_lengths[TopologicalVariables._domain_lengths != 0]

        if not non_zero_values.any():
            return 0

        return np.mean(non_zero_values)

    @staticmethod
    def get_num_labels():
        """
        Returns the number of labels calculated by the last call to label_ring

        Returns:
            int_t: Number of labels
        """
        return TopologicalVariables._num_labels

    @staticmethod
    def get_max_label():
        """
        Returns the maximum label calculated by the last call to label_ring

        Returns:
            int_t: Maximum label calculated
        """
        return TopologicalVariables._max_label

    @staticmethod
    def get_labels():
        """
        Returns the maximum label calculated by the last call to label_ring

        Returns:
            ndarray[int_t, ndim=2]: Maximum label calculated
        """
        return TopologicalVariables._labels
