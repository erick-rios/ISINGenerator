"""Module providing a class to generate a CSV file"""
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

import csv


class WriterCsv:
    """A class that contains the code that generates the CSV file with the simulation data for the Ising model."""
    @staticmethod
    def write_data(file_name: str, data: str, ) -> None:
        """Write simulation data to a CSV file.

        Args:
            file_name (str): The name of the CSV file.
            data (str): The simulation data to be written.
            encoding (str, optional): The encoding of the CSV file. Defaults to "utf-8".
        """
        # Write data to CSV file
        with open(file_name, "w", encoding = "utf-8", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(
                [
                    "kT",
                    "B",
                    "Energy",
                    "Magnetization",
                    "Domain Number",
                    "Mean Domains Size",
                ]
            )
            csv_writer.writerows(data)
