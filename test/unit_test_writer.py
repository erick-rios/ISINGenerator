from src.isingenerator.create_data_simulation import CreateDataSimulation

create_data_simulation = CreateDataSimulation(
        "C:\\Users\\danri\\Documents\\data_parte_2_2.csv",
        360000,
        1.0,
        4.0,
        0.005,
        16,
        0.8,
        1.0,
        1.0,
        15
    )

#create_data_simulation_non_zero = CreateDataSimulation(
#     "/home/soundskydriver/Documents/ISINGenerator/docs/data_nonzero.csv",
#    3000,
#    0.5,
#    2.0,
#    0.1,
#    16,
#    0.75,
#    initial_step_B= 0.0,
#    final_step_B=2.5,
#    delta_B=0.5
#)

print(create_data_simulation.generate_csv_data_zero_magnetic_field())
#print(create_data_simulation_non_zero.generate_csv_data_nonzero_magnetic_field())
