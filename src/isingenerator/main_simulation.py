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

from typing import List, Dict
import numpy as np

from src.isingenerator.monte_carlo_simulation import MonteCarloSimulation
from src.isingenerator.lattice_square import LatticeSquare
from src.isingenerator.ising_model_2d import IsingModel2D
from src.isingenerator.topological_variables import TopologicalVariables
#from src.isingenerator.geometric_variables import GeometricVariables
from src.isingenerator.geometric_variables_dos import GeometricVariables

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
        geometric_variables: bool = False,
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
            geometric variables (bool, optional): Option to calculate the geometric variables of the last spin matrix.

        Returns:
            List: Final data for simulation.
        """

        # Here we create memory arrays to store the data of interest.
        mean_domain_size_array: float = 0
        domain_number_array: float = 0
        magnetization_array: float = 0
        mean_magnetization_array: float = 0
        energy_array: float = 0

        half: float = steps / 2
        number_data: int = half/epsilon
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
                    
                    magnetization_array+=ising_model.calculate_magnetization()
                    mean_magnetization_array+=(ising_model.calculate_magnetization())/no_spines
                    energy_array+=ising_model.calculate_energy(J, B, mu)
                    # Compute Topological Variables
                    #TopologicalVariables.label_ring(
                    #    getattr(ising_model, "_matrix")
                    #)
                    #domain_number_array+=TopologicalVariables.number_of_domains()
                    #mean_domain_size_array+=TopologicalVariables.mean_domain_size()
            
        
        if geometric_variables:
            graph = GeometricVariables.ising_matrix_to_graph(
                getattr(ising_model, "_matrix")
            )
            frc = GeometricVariables.forman_ricci_curvature_edge(
                graph, 
                f"forman_ricci_information_dos_{kT:.5f}.png"
            )
            
        if geometric_variables:
            return [
                "{:.5f}".format(kT),
                "{:.5f}".format(B),
                "{:.5f}".format(energy_array/number_data),
                "{:.5f}".format(magnetization_array/number_data),
                "{:.5f}".format(mean_magnetization_array/number_data),
                "{:.5f}".format(domain_number_array/number_data),
                "{:.5f}".format(mean_domain_size_array/number_data),
                "{:.5f}".format(frc)
            ]
        else:
            return [
                "{:.5f}".format(kT),
                "{:.5f}".format(B),
                "{:.5f}".format(energy_array/number_data),
                "{:.5f}".format(magnetization_array/number_data),
                "{:.5f}".format(mean_magnetization_array/number_data),
                "{:.5f}".format(domain_number_array/number_data),
                "{:.5f}".format(mean_domain_size_array/number_data)
            ]
            
