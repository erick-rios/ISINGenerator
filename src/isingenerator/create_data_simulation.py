"""Module providing a class for create the data simulation of the 2D Ising Model"""

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

from typing import Any, List, Dict
import numpy as np
import os

from src.isingenerator.main_simulation import MainSimulation
from src.isingenerator.writer_csv import WriterCsv



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
        percentage_ones: float = 0.8,
        J: float = 1.0,
        mu: float = 1.0,
        epsilon: int = 15,
        geometric_variables = False,
        initial_step_B: float = None,
        final_step_B: float = None,
        delta_B: float = None,
        
    ) -> None:
        """Initialize an instance of CreateDataSimulation.

        Args:
            file_name (str): The name of the file.
            steps (int): The number of steps.
            initial_step_kT (float): The initial temperature.
            final_step_kT (float): The final temperature.
            delta_kT (float): The temperature step.
            dimension (int): The dimension of the Ising Model 2D.
            percentage_ones (float):
            J (float, optional): The constant of interaction between spins. Defaults to 1.0.
            mu (float, optional): The constant of magnetic moment. Defaults to 1.0.
            geometric_variables(boolean, optional): An optional parameter with o default value of False to calculate the Forman Ricci curvature.
            epsilon (int, optional): An optional parameter with a default value of 15.
            initial_step_B (float, optional): The initial magnetic field. Defaults to None.
            final_step_B (float, optional): The final magnetic field. Defaults to None.
            delta_B (float, optional): The magnetic field step. Defaults to None.

        Note:
            If initial_step_B, final_step_B, and delta_B are provided, the magnetic field parameters
            will be used; otherwise, the default magnetic field value will be set to 0.

        Example:
            >>> simulation = CreateDataSimulation(
            ...     file_name="example.csv",
            ...     steps=1000,
            ...     initial_step_kT=0.5,
            ...     final_step_kT=2.0,
            ...     delta_kT=0.1,
            ...     dimension=20,
            ...     percentage_ones=0.4,
            ...     J=1.5,
            ...     mu=2.0,
            ...     initial_step_B=0.2,
            ...     final_step_B=1.0,
            ...     delta_B=0.2
            ... )
        """
        self._file_name = file_name
        self._steps = steps
        self._initial_step_kT = initial_step_kT
        self._final_step_kT = final_step_kT
        self._delta_kT = delta_kT
        self._dimension = dimension
        self._percentage_ones = percentage_ones
        self._J = J
        self._mu = mu
        self._epsilon = epsilon
        self._geometric_variables = geometric_variables
        if (
            initial_step_B is not None
            and final_step_B is not None
            and delta_B is not None
        ):
            self._initial_step_B = initial_step_B
            self._final_step_B = final_step_B
            self._delta_B = delta_B
        else:
            self._B = 0

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representing the object in a format that can be used to recreate it.

        Example:
            >>> simulation = CreateDataSimulation(...)
            >>> repr(simulation)
            '<CreateDataSimulation(_file_name=..., steps=..., initial_step_kT=...,
            final_step_kT=..., delta_temperature=..., initial_step_B=..., final_step_B=...,
            delta_B=..., B=..., dimension=..., J=..., mu=...)>'
        """
        if self._initial_step_B is None and self._final_step_B is None:
            return (
                "<Create Data Simulation["
                + f"_file_name = {self._file_name}, "
                + f"steps = {self._steps}, "
                + f"initial_step_kT = {self._initial_step_kT}, "
                + f"final_step_kT = {self._final_step_kT}, "
                + f"delta_temperature = {self._delta_kT}\n"
                + f"B = {self._B}, "
                + f"dimension = {self._dimension}, "
                + f"percentage_ones = {self._percentage_ones}, "
                + f"J = {self._J}, "
                + f"mu = {self._mu}]>"
            )
        else:
            return (
                "<Create Data Simulation["
                + f"_file_name = {self._file_name}, "
                + f"steps = {self._steps}, "
                + f"initial_step_kT = {self._initial_step_kT}, "
                + f"final_step_kT = {self._final_step_kT}, "
                + f"delta_temperature = {self._delta_kT}\n"
                + f"initial_step_B = {self._initial_step_B}, "
                + f"initial_step_B = {self._final_step_B}, "
                + f"delta_B = {self._delta_B}, "
                + f"B = {self._B}, "
                + f"dimension = {self._dimension}, "
                + f"percentage_ones = {self._percentage_ones}, "
                + f"J = {self._J}, "
                + f"mu = {self._mu}]>"
            )

    def __str__(self) -> str:
        """Generate a string representation of the object CreateDataSimulation.

        Returns:
            str: A formatted string containing information about the object.


        Note:
            The generated string includes details such as file name, number of steps, temperature intervals,
            magnetic field information, interaction constants, magnetic moment constants, and the shape of the Ising Model 2D.

            If `initial_step_B` and `final_step_B` are both None, the string represents the Create Data Simulation.
            Otherwise, it represents an alternative Create Data Simulation.

        Example:
            >>> simulation = CreateDataSimulation()
            >>> print(simulation)
            "{Create Data Simulation
            file_name = data_simulation.csv
            number_of_steps = 350,345
            interval_temperatures = [0.5,10]
            delta_temperature = 0.8
            value_magnetic_field = 2
            constant_of_interaction_between_spins = 8
            constant_of_magnetic_moment = 4
            shape_Ising_Model_2D = (15, 15)
            }"
        """
        if self._initial_step_B is None and self._final_step_B is None:
            return (
                "{Create Data Simulation\n"
                + f"file_name = {self._file_name}\n"
                + f"number_of_steps = {self._steps}\n"
                + f"interval_temperatures = [{self._initial_step_kT},{self._final_step_kT}]\n"
                + f"delta_temperature = {self._delta_kT}\n"
                + f"value_magnetic_field = {self._B}\n"
                + f"constant_of_interaction_between_spins = {self._J}\n"
                + f"constant_of_magnetic_moment = {self._mu}\n"
                + f"shape_Ising_Model_2D = ({self._dimension,self._dimension})\n"
                + f"dimension = {self._dimension}"
                + "}"
            )
        else:
            return (
                "{Create Data Simulation\n"
                + f"_file_name={self._file_name}\n"
                + f"number_of_steps = {self._steps}\n"
                + f"interval_temperatures = [{self._initial_step_kT},{self._final_step_kT}]\n"
                + f"delta_temperature = {self._delta_kT}\n"
                + f"intervalo_magnetic_field = [{self._initial_step_B},{self._final_step_B}]\n"
                + f"delta_magnetic_field = {self._delta_B}\n"
                + f"constant_of_interaction_between_spins = {self._J}\n"
                + f"constant_of_magnetic_moment = {self._mu}\n"
                + f"shape_Ising_Model_2D = ({self._dimension,self._dimension})\n"
                + f"dimension = {self._dimension}"
                + "}"
            )

    def generate_csv_data_nonzero_magnetic_field(self) -> str:
        """Generates a csv archive with the data of the simulation. This is for a non-zero external magnetic field.

        Returns:
            str: The name of the file created.
        """
        # Create a list to store data.
        data: List[float] = []


        # Perform nested loops
        for k_T in np.arange(
            self._initial_step_kT, self._final_step_kT + self._delta_kT, self._delta_kT
        ):
            for B in np.arange(
                self._initial_step_B, self._final_step_B + self._delta_B, self._delta_B
            ):
                data.append(
                    MainSimulation.create_observables(
                        self._steps,
                        k_T,
                        self._dimension,
                        self._percentage_ones,
                        self._J,
                        B,
                        self._mu,
                        self._epsilon,
                    )
                )

        # Write data to CSV file
        WriterCsv.write_data(self._file_name, data)

        # Return the generated file
        return self._file_name

    
    def generate_csv_data_zero_magnetic_field(self) -> str:
        """Generates a CSV archive with the data of the simulation. This is for a zero external magnetic field.

        Returns:
            str: The name of the file created.
        """
        
        COLUMNS_NAMES = [
                    "kT",
                    "B",
                    "energy",
                    "magnetization",
                    "Magnetization_per_site",
                    "domain_number",
                    "mean_domain_size",
                    "forman_ricci_curvature"
                ]
        
        # Write column names in CSV file
        WriterCsv.write_data(self._file_name, COLUMNS_NAMES)
        
        # Perform the nested loop
        for k_T in np.arange(
            self._initial_step_kT, self._final_step_kT + self._delta_kT, self._delta_kT
        ):
            
            results = MainSimulation.create_observables(
                    self._steps,
                    k_T,
                    self._dimension,
                    self._percentage_ones,
                    self._J,
                    self._B,
                    self._mu,
                    self._epsilon,
                    self._geometric_variables
                )
            # Write data to CSV file
            WriterCsv.write_data(self._file_name, results)
            
        # Return the generated file
        return self._file_name

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
            >>> obj = CreateDataSimulation()
            >>> obj.attribute_name  # This triggers __getattribute__
            'attribute_value'
        """
        return object.__getattribute__(self, _name)

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
            >>> obj = CreatesDataSimulation()
            >>> obj.attribute_name = 'new_value'  # This triggers __setattr__
        """
        object.__setattr__(self, _name, value)
