"""Module providing class for main simulation of 2D Ising Model"""
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
from typing import List, Dict
from src.isingenerator.monte_carlo_simulation import MonteCarloSimulation
from src.isingenerator.lattice_square import LatticeSquare
from src.isingenerator.ising_model_2d import IsingModel2D
from src.isingenerator.topological_variables import TopologicalVariables


class MainSimulation:
    """Static class for implementing the main simulation of 2D Ising Model"""

    @staticmethod
    def create_observables(
        steps: int,
        kT: float,
        dimension: int = 15,
        percentage_ones: int = 0.8,
        J: float = 1,
        B: float = 0,
        mu: float = 1,
        epsilon: int = 15,
        create_images: bool = False,
    ) -> List:
        """Runs the simulation of the 2D Ising Model.

        Args:
            kT (float): Boltzmann constant times.
            steps (int): Number of iterations.
            dimension (int, optional): Dimension of spin matrix. Defaults to 15.
            percentange_ones (int,optional): Percentage of ones in the lattice. Should be a float between 0 and 1. Defaults to 0.8.
            J (float, optional): Interaction constant between spins. Defaults to 1.
            B (float, optional): External Magnetic Field. Defaults to 0.
            mu (float, optional): Magnetic moment. Defaults to 1.
            epsilon (int, optional): Amount designated to smooth the obtained quantities.. Defaults to 15.
            create_images (bool, optional): Option to visualize the changes on spin matrix. Defaults to False.

        Returns:
            List: Final data for simulation.
        """

        # Here we create memory arrays to store the data of interest.

        mean_domain_size_array: List[float]   = []
        domain_number_array: List[float]      = []
        magnetization_array: List[float]      = []
        mean_magnetization_array: List[float] = []
        energy_array: List[float] = []
        matrices_per_temperature: Dict[float: np.ndarray]={}

        half: float = steps / 2
        no_spines: float = dimension*dimension

        # Initialize the spin array
        lattice: LatticeSquare = LatticeSquare(dimension, dimension, percentage_ones)
        matrix: np.ndarray = lattice.create_matrix()
        ising_model: IsingModel2D = IsingModel2D(matrix)

        for step in range(steps):
            setattr(
                ising_model,
                "_matrix",
                MonteCarloSimulation.markov_chain_move(lattice, dimension, 1 / kT),
            )
            if step >= half:
                if step % epsilon == 0:
                    magnetization_array.append(ising_model.calculate_magnetization())
                    mean_magnetization_array.append((ising_model.calculate_magnetization())/no_spines)
                    energy_array.append(ising_model.calculate_energy(J, B, mu))
                    TopologicalVariables.label_ring(
                        getattr(ising_model, "_matrix")
                    )
                    domain_number_array.append(
                        TopologicalVariables.number_of_domains()
                    )
                    mean_domain_size_array.append(
                        TopologicalVariables.mean_domain_size()
                    )
                    matrices_per_temperature[step] = np.copy(getattr(ising_model, "_matrix"))

        return [
            kT,
            B,
            np.mean(energy_array),
            np.mean(magnetization_array),
            np.mean(mean_magnetization_array),
            np.mean(domain_number_array),
            np.mean(mean_domain_size_array),
            matrices_per_temperature
        ]
