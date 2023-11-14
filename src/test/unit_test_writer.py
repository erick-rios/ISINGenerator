import sys
sys.path.append('/home/soundskydriver/Documents/ISINGMODEL2DGenerator/src')

from CreateDataSimulation import *

create_data_simulation = CreateDataSimulation(
        "/home/soundskydriver/Documents/ISINGMODEL2DGenerator/docs/hazte_porfavor.csv",
        20,
        1,
        2.0,
        0.1,
        3
    )

print(create_data_simulation.generate_csv_data_zero_magnetic_field())