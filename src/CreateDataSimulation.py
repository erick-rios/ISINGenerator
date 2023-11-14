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
from src.MainSimulation import *
from src.WriterCsv import *
import numpy as np


class CreateDataSimulation:
    """Class for creating the dataset from an Ising Model 2D using Monte Carlo and Markov Chains."""
    def __init__(
        self,
        file_name: str,
        steps: int,
        initial_step_kT: float,
        final_step_kT: float,
        delta_kT: float,
        dimension: int,
        J: float = 1.0,
        mu: float = 1.0,
        epsilon: int = 15,
        initial_step_B: float = None,
        final_step_B: float = None,
        delta_B: float =  None
    ) -> None:
        """_summary_

        Args:
            _file_name (str): _description_
            steps (int): _description_
            initial_step_kT (float): _description_
            final_step_kT (float): _description_
            delta_kT (float): _description_
            delta_B (float): _description_
            dimension (int): _description_
            J (float, optional): _description_. Defaults to 1.0.
            mu (float, optional): _description_. Defaults to 1.0.
            epsilon (int, optional): _description_. Defaults to 1.0.
            initial_step_B (float, optional): _description_. Defaults to None.
            final_step_B (float, optional): _description_. Defaults to None.
            B (float, optional): _description_. Defaults to None.
        """
        self._file_name = file_name
        self._steps = steps
        self._initial_step_kT = initial_step_kT
        self._final_step_kT = final_step_kT
        self._delta_kT = delta_kT
        self._delta_B = delta_B
        self._dimension = dimension
        self._J = J
        self._mu = mu
        self._epsilon = epsilon
        if initial_step_B is not None and final_step_B is not None and delta_B is not None:
            self._initial_step_B = initial_step_B
            self._final_step_B = final_step_B
            self._delta_B = delta_B
        else:
            self._B = 0 
            
        

    def __repr__(self) -> str:
        return (
            "<Create Data Simulation["
            + f"_file_name = {self._file_name}, "
            + f"steps = {self.steps}, "
            + f"initial_step_kT = {self.initial_step_kT}, "
            + f"initial_step_kT = {self.final_step_kT}, "
            + f"delta_temperature = {self.delta_kT}\n"
            + f"initial_step_B = {self.initial_step_B}, "
            + f"initial_step_B = {self.final_step_B}, "
            + f"delta_B = {self.delta_B}, "
            + f"B = {self.B}, "
            + f"dimension = {self.dimension}"
            f"J = {self.J}, " + f"mu = {self.mu}"
        )

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        if self.initial_step_B is None and self.final_step_B is None:
            return (
                "{Create Data Simulation\n"
                + f"_file_name = {self._file_name}\n"
                + f"number_of_steps = {self.steps}\n"
                + f"interval_temperatures = [{self.initial_step_kT},{self.final_step_kT}]\n"
                + f"delta_temperature = {self.delta_kT}\n"
                + f"value_magnetic_field = {self.B}\n"
                + f"constant_of_interaction_between_spins = {self.J}"
                + f"constant_of_magnetic_moment = {self.mu}"
                + f"shape_Ising_Model_2D = ({self.dimension,self.dimension})"
                + "}"
            )
        else:
            return (
                "{<Create Data Simulation>\n"
                + f"_file_name={self._file_name}\n"
                + f"number_of_steps = {self.steps}\n"
                + f"interval_temperatures = [{self.initial_step_kT},{self.final_step_kT}]\n"
                + f"delta_temperature = {self.delta_kT}\n"
                + f"intervalo_magnetic_field = [{self.initial_step_B},{self.final_step_B}]\n"
                + f"delta_magnetic_field = {self.delta_B}"
                + f"constant_of_interaction_between_spins = {self.J}"
                + f"constant_of_magnetic_moment = {self.mu}"
                + f"shape_Ising_Model_2D = ({self.dimension,self.dimension})"
                + "}"
            )

    def generate_csv_data_nonzero_magnetic_field(self) -> str:
        """Generates a csv archive with the data of the simulation. This is for a non-zero external magnetic field.

        Returns:
            str: The name of the file created.
        """
        # Create a list to store data.
        data = []

        # Perform nested loops
        for kT in np.arange(
            self._initial_step_kT, self._final_step_kT + self._delta_kT, self._delta_kT
            ):
            for B in np.arange(
                self._initial_step_B, self._final_step_B + self._delta_B, self._delta_B
            ):
                data.append(
                    MainSimulation.create_observables(
                        self.steps, kT,  self._dimension, self._J, B, self._mu, self._epsilon
                    )
                )

        # Write data to CSV file
        WriterCsv.write_data(self._file_name, data)

        # Return the generated file
        return self._file_name

    def generate_csv_data_zero_magnetic_field(self) -> str:
        """Generates a csv archive with the data of the simulation. This is for a zero external magnetic field.

        Returns:
            str: The name of the file created.
        """
        # Create a list to store data.
        data = []

        # Perform the nested loop
        for kT in np.arange(
            self._initial_step_kT, self._final_step_kT + self._delta_kT, self._delta_kT
        ):
            data.append(
                MainSimulation.create_observables(
                    self._steps, kT, self._dimension, self._J, self._B , self._mu, self._epsilon
                )
            )

        # Write data to CSV file
        WriterCsv.write_data(self._file_name, data)

        # Return the generated file
        return self._file_name
    
 
    # properties

    def __getattribute__(self, _name: str) -> Any:

        return object.__getattribute__(self, _name)

    # setters

    def __setattr__(self, _name: str, value: Any) -> None:
        object.__setattr__(self, _name, value)
    
