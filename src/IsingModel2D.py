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

from src.Neighbors import *
from typing import Any
import numpy as np


class IsingModel2D:
    """Class for calculating pnysical variables in a spin matrix."""

    def __init__(self, matrix: np.array) -> None:
        """Initializes an instance of the IsingModel2D class

        Args:
            matrix (np.array) = Spin matrix
        """

        self._matrix = matrix
        self._N = matrix.shape[0]

    def __repr__(self) -> str:
        return f"<IsingModel2D[_matrix = {self.__getattribute__('_matrix')}, _N = {self.__getattribute__('_N')}]>"

    def __str__(self) -> str:
        return (
            "IsingModel2D:\n"
            + f"matrix = {self.__getattribute__('_matrix')}\n"
            + f"dimension = {self.__getattribute__('_N')}, {self.__getattribute__('_N')}\n"
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
            matrix (np.array): spin matrix

        Returns:
            float: Total magnetization of spin matrix.
        """
        mag = np.sum(self._matrix)
        return mag

    # properties

    def __getattribute__(self, _name: str) -> Any:
        return object.__getattribute__(self, _name)

    # setters

    def __setattr__(self, _name: str, value: Any) -> None:
        object.__setattr__(self, _name, value)
