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
from isingenerator.monte_carlo_simulation import MonteCarloSimulation
from isingenerator.lattice_square import LatticeSquare
from isingenerator.ising_model_2d import IsingModel2D
from isingenerator.topological_variables import TopologicalVariables


class MainSimulation:
    """Static class for implementing the main simulation of 2D Ising Model"""

    @staticmethod
    def create_observables(
        steps: int,
        kT: float,
        dimension: int = 15,
        J: float = 1,
        B: float = 0,
        mu: float = 1,
        epsilon: int = 15,
        create_images: bool = False,
    ) -> list:
        """Runs the simulation of the 2D Ising Model.

        Args:
            kT (float): Boltzmann constant times.
            steps (int): Number of iterations.
            dimension (int, optional): Dimension of spin matrix. Defaults to 15.
            J (float, optional): Interaction constant between spins. Defaults to 1.
            B (float, optional): External Magnetic Field. Defaults to 0.
            mu (float, optional): Magnetic moment. Defaults to 1.
            epsilon (int, optional): Amount designated to smooth the obtained quantities.. Defaults to 15.
            create_images (bool, optional): Option to visualize the changes on spin matrix. Defaults to False.

        Returns:
            list: Final data for simulation.
        """

        # Here we create memory arrays to store the data of interest.

        mean_domain_size_array: list[float] = []
        domain_number_array: list[float] = []
        magnetization_array: list[float] = []
        energy_array: list[float] = []

        half = steps / 2

        # Initialize the spin array
        lattice = LatticeSquare(dimension, dimension)
        matrix = lattice.create_matrix()
        ising_model = IsingModel2D(matrix)

        for step in range(steps):
            setattr(
                ising_model,
                "_matrix",
                MonteCarloSimulation.markov_chain_move(lattice, dimension, 1 / kT),
            )
            if step >= half:
                if step % epsilon == 0:
                    magnetization_array.append(ising_model.calculate_magnetization())
                    energy_array.append(ising_model.calculate_energy(J, B, mu))
                    domain_number_array.append(
                        TopologicalVariables.number_of_domains(
                            getattr(ising_model, "_matrix")
                        )
                    )
                    mean_domain_size_array.append(
                        TopologicalVariables.mean_domain_size(
                            getattr(ising_model, "_matrix")
                        )
                    )

        return [
            kT,
            B,
            np.mean(energy_array),
            np.mean(magnetization_array),
            np.mean(domain_number_array),
            np.mean(mean_domain_size_array),
        ]
