from src.isingenerator.create_data_simulation import CreateDataSimulation
from multiprocessing import Pool
from typing import Tuple, List, Any

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
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_1.csv", 30000000, 3.0, 3.0, 0.0, 900, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_2.csv", 30000000, 3.1, 3.1, 0.0, 900, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_3.csv", 30000000, 3.2, 3.2, 0.0, 900, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_4.csv", 30000000, 3.3, 3.3, 0.0, 900, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_1.csv", 30000000, 3.4, 3.4, 0.0, 900, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_2.csv", 30000000, 3.5, 3.5, 0.0, 900, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_3.csv", 30000000, 3.6, 3.6, 0.0, 900, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_4.csv", 30000000, 3.7, 3.7, 0.0, 900, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_1.csv", 30000000, 3.8, 3.8, 0.0, 900, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_1.csv", 30000000, 3.9, 3.9, 0.0, 900, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_2.csv", 30000000, 4.0, 4.0, 0.0, 900, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_1.csv", 30000000, 3.8, 3.8, 0.0, 900, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_1.csv", 400000, 1.0, 4.0, 0.1, 100, 0.8, 1.0, 1.0, 15, False),
        ("/home/soundskydriver/Documents/ISINGenerator/data_prueba_2.csv", 400000, 1.0, 4.0, 0.1, 300, 0.8, 1.0, 1.0, 15, False),
    ]
    
    # Create a Pool of 4 processes
    with Pool(33) as pool:
        pool.map(simulate_data, arguments_list)
    
 

