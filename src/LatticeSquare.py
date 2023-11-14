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

import random
from typing import Any
import numpy as np


class LatticeSquare:
    def __init__(self, rows: int = 15, columns: int = 15, percentange_ones: float = 0.8) -> None:
        self._rows = rows
        self._columns = columns
        self._percentage_ones = percentange_ones
        self._matrix = None

    def __repr__(self) -> str:
        return f"<LatticeSquare[_rows={self.rows}, columns={self._columns}, percentage_ones={self._percentage_ones}]>"

    def __str__(self) -> str:
        return f"LatticeSquare\n_rows={self.rows}\ncolumns={self._columns}\npercentage_ones={self._percentage_ones}"

    def create_matrix(self) -> np.array:
        """Function to create the spin matrix for the 2D Ising model with a given distribution of positive spins.

        Args:
            rows (int): Number of rows of spin matrix.
            columns (int): Number of columns of spin matrix.
            percentage_ones (float, optional): Percentage of positive spin values present in the spin matrix. Defaults to 0.8.

        Returns:
            np.array: Final spin matrix created.
        """

        total_elements = self._rows * self._columns

        # Calculates the quantity of ones and minus ones based on the given percentage.
        num_ones = int(self._percentage_ones * total_elements)
        num_minus_ones = total_elements - num_ones

        # Creates a list of ones and minus ones based on the calculated quantities.
        elements = [1] * num_ones + [-1] * num_minus_ones

        # Randomly shuffles the list of elements.
        np.random.shuffle(elements)

        # Creates the matrix from the shuffled list.
        matrix = np.array(elements).reshape(self._rows, self._columns)
        
        self._matrix = matrix

        return matrix

    def random_position(self) -> list:
        """Function to choose a random position from spin matrix.


        Args:
            matrix (np.array): Spin matrix.

        Returns:
            list: Row and column of the spin matrix randomly chosen.
        """
        m, n = self._rows, self._columns
        i = random.randint(0, m - 1)
        j = random.randint(0, n - 1)
        return [i, j]
    
    #properties
    
    def __getattribute__(self, _name: str) -> Any:
        return object.__getattribute__(self, _name)

    # setters

    def __setattr__(self, _name: str, value: Any) -> None:
        object.__setattr__(self, _name, value)
