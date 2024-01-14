"""
ISING MODEL 2D SQUARE LATTICE
"""


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

from typing import Any
import numpy as np
from isingenerator.neighbors import Neighbors


class IsingModel2D:
    """Class for calculating pnysical variables in a spin matrix."""

    def __init__(self, matrix: np.ndarray) -> None:
        """Initialize an instance of the IsingModel2D class.

        This class represents a 2D Ising model with a given spin matrix.

        Args:
            matrix (np.ndarray): The spin matrix representing the Ising model.

        Attributes:
            _matrix (np.ndarray): The spin matrix of the Ising model.
            _N (int): The dimension of the Ising model, inferred from the shape of the matrix.

        Example:
            >>> import numpy as np
            >>> spin_matrix = np.array([[1, -1], [-1, 1]])
            >>> ising_model = IsingModel2D(spin_matrix)
        """

        self._matrix = matrix
        self._N = matrix.shape[0]

    def __repr__(self) -> str:
        """Return a string representation of the IsingModel2D object.

        Returns:
            str: A string representation containing information about the spin matrix and dimension.

        Example:
            >>> ising_model = IsingModel2D(...)
            >>> repr(ising_model)
            '<IsingModel2D(_matrix=[[1, -1], [-1, 1]], _N=2)>'
        """

        return f"<IsingModel2D(_matrix={self._matrix}, _N={self._N})>"

    def __str__(self) -> str:
        """Return a formatted string representation of the IsingModel2D object.

        Returns:
            str: A formatted string containing information about the spin matrix and dimension.

        Example:
            >>> ising_model = IsingModel2D(...)
            >>> str(ising_model)
            'IsingModel2D:
            matrix = [[1, -1], [-1, 1]]
            dimension = (2, 2)'
        """
        return (
            f"IsingModel2D:\n"
            f"matrix = {self._matrix}\n"
            f"dimension = ({self._N}, {self._N})\n"
        )

    def calculate_energy(
        self, J: float = 1.0, B: float = 1.0, mu: float = 1.0
    ) -> float:
        """Function to calculate the energy of the 2D Ising model.

        Args:
            J (float): Interaction constant between spins.
            B (float): External magnetic field.
            mu (float): Magnetic moment

        Returns:
            float: Total energy of spin matrix
        """
        # Calculate the interaction energy between neighboring spins
        neighbors = Neighbors.sum_of_neighbors(self._matrix)
        interaction_energy = -J * np.sum(neighbors * self._matrix)

        # Calculate the energy of the external magnetic field
        field_energy = -(B * mu) * np.sum(self._matrix)

        # Calculate the total energy
        total_energy = interaction_energy + field_energy

        return total_energy

    def calculate_magnetization(self) -> float:
        """This method returns the magnetization of the spin matrix.

        Args:
            matrix (np.ndarray): spin matrix

        Returns:
            float: Total magnetization of spin matrix.
        """
        mag = np.sum(self._matrix)
        return mag

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
            >>> obj = IsingModel2D()
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
            >>> obj = IsingModel2D()
            >>> obj.attribute_name = 'new_value'  # This triggers __setattr__
        """
        object.__setattr__(self, _name, value)
