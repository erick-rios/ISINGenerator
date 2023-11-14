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
    """This class represents a 2D lattice, where each element is initialized randomly with ones and zeros based on the specified percentage of ones."""

    def __init__(
        self, rows: int = 15, columns: int = 15, percentange_ones: float = 0.8
    ) -> None:
        """Initialize an instance of the LatticeSquare class.

        Args:
            rows (int, optional): Number of rows in the lattice. Defaults to 15.
            columns (int, optional): Number of columns in the lattice. Defaults to 15.
            percentage_ones (float, optional): Percentage of ones in the lattice. Should be a float between 0 and 1.
                Defaults to 0.8.


        Example:
            >>> lattice = LatticeSquare()
            >>> lattice_with_custom_params = LatticeSquare(rows=10, columns=20, percentage_ones=0.5)
        """

        self._rows = rows
        self._columns = columns
        self._percentage_ones = percentange_ones
        self._matrix = None

    def __repr__(self) -> str:
        """Return a string representation of the LatticeSquare object.

        Returns:
            str: A string containing information about the rows, columns, and percentage of ones.

        Example:
            >>> lattice = LatticeSquare()
            >>> repr(lattice)
            '<LatticeSquare[_rows=15, _columns=15, percentage_ones=0.8]>'
        """
        return f"<LatticeSquare[_rows={self._rows}, columns={self._columns}, percentage_ones={self._percentage_ones}]>"

    def __str__(self) -> str:
        """Return a formatted string representation of the LatticeSquare object.

        Returns:
            str: A formatted string containing information about the rows, columns, and percentage of ones.

        Example:
            >>> lattice = LatticeSquare()
            >>> str(lattice)
            'LatticeSquare\n_rows=15\ncolumns=15\npercentage_ones=0.8'
        """
        return f"LatticeSquare\n_rows={self._rows}\ncolumns={self._columns}\npercentage_ones={self._percentage_ones}"

    def create_matrix(self) -> np.array:
        """Create the spin matrix for the 2D Ising model with a given distribution of positive spins.

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
        """Choose a random position from spin matrix.


        Args:
            matrix (np.array): Spin matrix.

        Returns:
            list: Row and column of the spin matrix randomly chosen.
        """
        m, n = self._rows, self._columns
        i = random.randint(0, m - 1)
        j = random.randint(0, n - 1)
        return [i, j]

    # properties

    def __getattribute__(self, _name: str) -> Any:
        """Retrieve the value of the specified attribute.

        This method is automatically called when attempting to access an attribute of an object.

        Args:
            _name (str): The name of the attribute to retrieve.

        Returns:
            Any: The value of the specified attribute.

        Raises:
            AttributeError: If the attribute is not found.

        Example:
            >>> obj = LatticeSquare(3, 4, 0.9)
            >>> obj.attribute_name  # This triggers __getattribute__
            'attribute_value'
        """
        return object.__getattribute__(self, _name)

    # setters

    def __setattr__(self, _name: str, value: Any) -> None:
        """Set the value of the specified attribute.

        This method is automatically called when attempting to set the value of an attribute of an object.

        Args:
            _name (str): The name of the attribute to set.
            value (Any): The value to assign to the attribute.

        Returns:
            None

        Raises:
            AttributeError: If the attribute is read-only or cannot be set.

        Example:
            >>> obj = LatticeSquare(3, 4, 0.8)
            >>> obj.attribute_name = 'new_value'  # This triggers __setattr__
        """
        object.__setattr__(self, _name, value)
