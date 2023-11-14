<p align="center">
  <img src="/images/ISINGenerator(3).png" alt="Descripción de la imagen" width="250">
</p>


A library for creating a database that allows analyzing the energy, magnetization, the number of topological domains and the mean size of the topological domains in a square lattice of spins in a Ising Model of two dimensions. It is achieved using Monte Carlo simulation and implementing the Metropolis algorithm.


## Run Locally

Clone the project

```bash
  git clone https://github.com/erick-rios/ISINGenerator
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```
## Acknowledgements

## Authors

- [@erick-rios](https://github.com/erick-rios)

## Documentation

[Documentation](https://linktodocumentation)


## License

[GPL-3.0 license](https://choosealicense.com/licenses/gpl-3.0/



![Logo]()


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Usage/Examples

```py
import CreateDataSimulation from create_data_simulation


create_data_simulation = CreateDataSimulation(
        "/home/soundskydriver/Documents/ISINGMODEL2DGenerator/docs/hazte_porfavor.csv",
        20,
        1,
        2.0,
        0.1,
        3
    )

print(create_data_simulation.generate_csv_data_zero_magnetic_field())
```
## Support

For support, email erickjesusriosgonzalez@gmail.com or join our Slack channel.
