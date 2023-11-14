from isingenerator.create_data_simulation import CreateDataSimulation

create_data_simulation = CreateDataSimulation(
        "/home/soundskydriver/Documents/ISINGenerator/docs/data.csv",
        5000,
        0.5,
        2.0,
        0.1,
        10
    )

print(create_data_simulation.generate_csv_data_zero_magnetic_field())