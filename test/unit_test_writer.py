"""
Module for simulating data and generating CSV files using multiprocessing.
"""

from multiprocessing import Pool
from typing import Tuple, List, Any
from src.isingenerator.create_data_simulation import CreateDataSimulation

def simulate_data(arguments: Tuple[str, int, float, float, float, int, float, float, float, int, bool]) -> Any:
    """
    Simulates data based on the provided arguments and generates a CSV file.

    Args:
        arguments (Tuple[str, int, float, float, float, int, float, float, float, int, bool]): 
            A tuple containing the following parameters:
            - filepath (str): Path to save the generated CSV file.
            - iterations (int): Number of iterations for the simulation.
            - initial_step_kT (float): Initial kT value for the simulation.
            - final_step_kT (float): Final kT value for the simulation.
            - delta_kT (float): Increment of kT value in each iteration for the simulation.
            - dimension_matrix (int): Dimension of the matrix.
            - percentage_ones (float): Fifth parameter for the simulation.
            - J (float): The constante of the interaction between spins.
            - mu (float): The constante of magnetic moment for the simulation.
            - epsilon (int): Epsilon to compute mean for the values in the matrix for the simulation.
            - geometric_variables (bool,): Boolean geometric_variables for the simulation settings. Only true if dimension_matrix == 1,000,000. Otherwise set to False.

    Returns:
        Any: The result of the data generation, typically the status or output of the CSV generation.
    """
    filepath, iterations, initial_step_kT, final_step_kT, delta_kT, dimension_matrix, percentage_ones, J, mu, epsilon, geometric_variables = arguments
    create_data_simulation = CreateDataSimulation(
        filepath,
        iterations,
        initial_step_kT,
        final_step_kT,
        delta_kT,
        dimension_matrix,
        percentage_ones,
        J,
        mu,
        epsilon,
        geometric_variables
    )
    return create_data_simulation.generate_csv_data_zero_magnetic_field()

if __name__ == "__main__":
    # List of arguments for each process
    arguments_list: List[Tuple[str, int, float, float, float, int, float, float, float, int, bool]] = [
        ("/home/soundskydriver/Documents/ISINGenerator/1000000_100_7500.csv", 1000000, 0.5, 5.0, 0.1, 100, 0.5, 1.0, 1.0, 7500, False),
        ("/home/soundskydriver/Documents/ISINGenerator/1000000_100_10000.csv", 1000000, 0.5, 5.0, 0.1, 100, 0.5, 1.0, 1.0, 10000, False),
        ("/home/soundskydriver/Documents/ISINGenerator/1100000_110_9075.csv", 1000000, 0.5, 5.0, 0.1, 110, 0.5, 1.0, 1.0, 9075, False),
        ("/home/soundskydriver/Documents/ISINGenerator/1100000_110_12100.csv", 1000000, 0.5, 5.0, 0.1, 110, 0.5, 1.0, 1.0, 12100, False),
        ("/home/soundskydriver/Documents/ISINGenerator/1200000_120_10800.csv", 1200000, 0.5, 5.0, 0.1, 120, 0.5, 1.0, 1.0, 10800, False),
        ("/home/soundskydriver/Documents/ISINGenerator/1200000_120_14400.csv", 1200000, 0.5, 5.0, 0.1, 120, 0.5, 1.0, 1.0, 14400, False),
        ("/home/soundskydriver/Documents/ISINGenerator/1300000_130_12675.csv", 1300000, 0.5, 5.0, 0.1, 130, 0.5, 1.0, 1.0, 12675, False),
        ("/home/soundskydriver/Documents/ISINGenerator/1300000_130_16900.csv", 1300000, 0.5, 5.0, 0.1, 130, 0.5, 1.0, 1.0, 16900, False),
    ]
    
    # Create a Pool of 4 processes
    with Pool(8) as pool:
        pool.map(simulate_data, arguments_list)
    
 

