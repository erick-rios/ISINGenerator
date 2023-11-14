<p align="center">
  <img src="/images/ISINGenerator(3).png" alt="Descripción de la imagen" width="250">
</p>


A library for creating a database that allows analyzing the energy, magnetization, the number of topological domains and the mean size of the topological domains in a square lattice of spins in a Ising Model of two dimensions. It is achieved using Monte Carlo simulation and implementing the Metropolis algorithm.


## Run Locally

Clone the project

```bash
  git clone https://github.com/erick-rios/ISINGenerator
```
Instal by PyPI

```bash
  $ python3 -m pip install ISINGenerator
```
## Acknowledgements

## Authors

- [@erick-rios](https://github.com/erick-rios)

## Documentation

[http://isingenerator.readthedocs.io/](http://isingenerator.readthedocs.io/)


## License

[GPL-3.0 license](https://choosealicense.com/licenses/gpl-3.0/)

## Screenshots

<p align="center">
  <img src="/images/isingit.png" width="400" />
  <img src="/images/Screenshot 2023-06-19 at 14-06-59 PrTr_UAM_IZT.png" width="400" /> 
</p>



## Usage/Examples

```py
from isingenerator.create_data_simulation import CreateDataSimulation 


create_data_simulation = CreateDataSimulation(
        "/home/../../../data_simulation.csv", # Name of the file
        20,                                   # Steps
        1,                                    # initial_step_kT
        2.0,                                  # final_step_kT
        0.1,                                  # delta_kT
        3                                     # dimension
        0.56                                  # percentage_ones
    )

print(create_data_simulation.generate_csv_data_zero_magnetic_field())
```
## Support

For support, email erickjesusriosgonzalez@gmail.com or join our Slack channel.
