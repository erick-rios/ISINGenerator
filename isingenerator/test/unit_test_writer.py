from isingenerator.create_data_simulation import CreateDataSimulation

create_data_simulation = CreateDataSimulation(
        "/home/soundskydriver/Documents/ISINGMODEL2DGenerator/docs/hazte_porfavor.csv",
        20,
        1,
        2.0,
        0.1,
        3
    )

print(create_data_simulation.generate_csv_data_zero_magnetic_field())