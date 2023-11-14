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

from src.LatticeSquare import *
from src.Neighbors import *
import numpy as np


class MonteCarloSimulation:
    """Class for implementing the Markov Chain Algorithm."""

    @staticmethod
    def markov_chain_move(lattice: LatticeSquare, N: int, beta: float) -> np.array:
        """This method is for implementing the Monte Carlo method using the Metropolis algorithm. The goal is to efficiently make the change until reaching the base state using Boltzmann probability as a condition.

        Args:
            matrix (np.array): Spin matrix
            N (int): Dimension of the spin matrix.
            beta (float): One divided Boltzmann constant times temperature.

        Returns:
            np.array: The matrix after making spin changes, aiming to achieve the minimum energy.
        """
        a, b = lattice.random_position()
        site = lattice._matrix[a, b]
        sum_neigh = Neighbors.sum_neighbors_position(lattice._matrix, a, b, N)
        delta_e = MonteCarloSimulation.delta_energy(site, sum_neigh)
        if delta_e < 0:
            site *= -1
        elif np.random.random() < np.exp(-delta_e * beta):
            site *= -1
        lattice._matrix[a, b] = site

        return lattice._matrix

    @staticmethod
    def delta_energy(value_of_site: int, sum_nb: int) -> int:
        """Function to get the delta energy to implement the Monte Carlo Simulation.

        Args:
            value_of_site (int): Value of spin in spin matrix site chosen.
            sum_nb (int): Sum of nearest neighbors for a spin value on site.

        Returns:
            int: Delta energy.
        """

        delta_e = 2 * value_of_site * sum_nb

        return delta_e
