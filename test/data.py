#!/usr/bin/env python3

from isingenerator.create_data_simulation import CreateDataSimulation

data_01 = CreateDataSimulation(
        "data_parte_01.csv",
        360000,
        0.2,
        1.0,
        0.00025,
        16,
        0.8,
        1.0,
        1.0,
        15
    )
data_02 = CreateDataSimulation(
        "data_parte_02.csv",
        360000,
        1.0,
        2.0,
        0.00025,
        16,
        0.8,
        1.0,
        1.0,
        15
    )
data_03 = CreateDataSimulation(
        "data_parte_03.csv",
        360000,
        2.0,
        3.0,
        0.00025,
        16,
        0.8,
        1.0,
        1.0,
        15
    )
data_04 = CreateDataSimulation(
        "data_parte_04.csv",
        360000,
        3.0,
        4.0,
        0.00025,
        16,
        0.8,
        1.0,
        1.0,
        15
    )
data_05 = CreateDataSimulation(
        "data_parte_05.csv",
        360000,
        4.0,
        5.0,
        0.00025,
        16,
        0.8,
        1.0,
        1.0,
        15
    )
data_06 = CreateDataSimulation(
        "data_parte_06.csv",
        360000,
        5.0,
        6.0,
        0.00025,
        16,
        0.8,
        1.0,
        1.0,
        15
    )
data_07 = CreateDataSimulation(
        "data_parte_07.csv",
        360000,
        6.0,
        7.0,
        0.00025,
        16,
        0.8,
        1.0,
        1.0,
        15
    )
data_08 = CreateDataSimulation(
        "data_parte_08.csv",
        360000,
        7.0,
        8.0,
        0.00025,
        16,
        0.8,
        1.0,
        1.0,
        15
    )
data_09 = CreateDataSimulation(
        "data_parte_09.csv",
        360000,
        8.0,
        9.0,
        0.00025,
        16,
        0.8,
        1.0,
        1.0,
        15
    )
data_10 = CreateDataSimulation(
        "data_parte_10.csv",
        360000,
        9.0,
        10.0,
        0.00025,
        16,
        0.8,
        1.0,
        1.0,
        15
    )

data_01.generate_csv_data_zero_magnetic_field()
data_02.generate_csv_data_zero_magnetic_field()
data_03.generate_csv_data_zero_magnetic_field()
data_04.generate_csv_data_zero_magnetic_field()
data_05.generate_csv_data_zero_magnetic_field()
data_06.generate_csv_data_zero_magnetic_field()
data_07.generate_csv_data_zero_magnetic_field()
data_08.generate_csv_data_zero_magnetic_field()
data_09.generate_csv_data_zero_magnetic_field()
data_10.generate_csv_data_zero_magnetic_field()
    
