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


class Neighbors:
    @staticmethod
    def sum_of_neighbors(matrix: np.ndarray) -> int:
        """Calculate the sum of nearby neighbors in the spin matrix, considering periodic boundary conditions.

        Returns:
            int: The sum of nearby neighbors in the spin matrix.
        """

        rolled_up = np.roll(matrix, -1, axis=0)
        rolled_down = np.roll(matrix, 1, axis=0)
        rolled_left = np.roll(matrix, -1, axis=1)
        rolled_right = np.roll(matrix, 1, axis=1)

        sum_neighbors = rolled_up + rolled_down + rolled_left + rolled_right

        return sum_neighbors

    @staticmethod
    def sum_neighbors_position(matrix: np.ndarray, row: int, column: int, N: int) -> int:
        """Function to get the sum of the nearest neighbors due to a spin in a site on the Spin matrix.

        Args:
            row (int): Row of position in matrix.
            column (int): Column of position in matrix
            N (int): Dimension of matrix.

        Returns:
            int: Sum of nearest neighbors for a spin in a position [a,b]
        """
        a, b = row, column
        nb = (
            matrix[(a + 1) % N, b]
            + matrix[a, (b + 1) % N]
            + matrix[(a - 1) % N, b]
            + matrix[a, (b - 1) % N]
        )
        return nb
