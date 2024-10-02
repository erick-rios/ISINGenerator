''' Module to implement the geometric variables'''

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

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Tuple
from collections import Counter

class GeometricVariables:
    """Static class for geometric variables in 2D Ising Model"""

    @staticmethod
    def ising_matrix_to_graph(ising_matrix: np.ndarray) -> nx.Graph:
        """
        Converts an Ising model matrix to a graph representation.

        In the graph, nodes represent spins with a value of 1, and edges connect adjacent nodes that also have a spin value of 1. 
        This method accounts for periodic boundary conditions.

        Args:
            ising_matrix (np.ndarray): A 2D array representing the Ising model matrix, where each element is either 1 or -1.

        Returns:
            nx.Graph: An undirected graph where nodes are tuples representing matrix coordinates, and edges connect adjacent spins with a value of 1.
        """
        # Get the dimensions of the matrix
        N, M = np.shape(ising_matrix)

        # Create an undirected graph
        G = nx.Graph()

        # Iterate over each position in the matrix
        for i in range(N):
            for j in range(M):
                # Add a node if the spin value is 1
                if ising_matrix[i, j] == 1:
                    G.add_node((i, j))
                    
                    # Define neighbors with periodic boundary conditions (ring-like conditions)
                    neighbors: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]] = (
                        (i, (j - 1) % M),   # left neighbor
                        (i, (j + 1) % M),   # right neighbor
                        ((i - 1) % N, j),   # upper neighbor
                        ((i + 1) % N, j)    # lower neighbor
                    )

                    # Add edges to neighbors that also have a spin value of 1
                    for neighbor in neighbors:
                        if ising_matrix[neighbor] == 1:
                            G.add_edge((i, j), neighbor)

        return G

    @staticmethod
    def forman_ricci_curvature_edge(graph: nx.Graph, name_image: str) -> float:
        """
        Computes the Forman-Ricci curvature for each edge in the given graph, calculates the total Forman-Ricci curvature of the graph,
        and saves the results in a PNG image showing the normalized distribution of curvature values.

        The Forman-Ricci curvature for an edge is calculated based on the degrees of the nodes connected by the edge.

        Args:
            graph (nx.Graph): An undirected graph.
            name_image (str): The name of the output PNG image file.

        Returns:
            float: The total Forman-Ricci curvature of the graph.
        """
        
        KT_VALUE = name_image.split('_')[-1].split('.png')[0]
        
        frc_total = 0
        frc_values = []

        # Compute Forman-Ricci curvature for each edge
        for node in graph.nodes:
            neighbors = list(graph.neighbors(node))
            for neighbor in neighbors:
                frc = -graph.degree(node) - graph.degree(neighbor)
                graph[node][neighbor]["forman_ricci_curvature"] = frc
                frc_values.append(frc)
                frc_total += frc

        # Calculate the normalized distribution of curvature values
        count_values = Counter(frc_values)
        total_count = sum(count_values.values())
        normalized_distribution = {k: v / total_count for k, v in count_values.items()}

        # Plot the distribution of Forman-Ricci curvature values
        plt.figure(figsize=(10, 6))
        colors = sns.color_palette("husl", len(normalized_distribution))
        for idx, (curvature, count) in enumerate(sorted(normalized_distribution.items())):
            plt.bar(curvature, count, color=colors[idx], label=f'Curvature: {curvature}, Density: {count:.5f}')

        plt.title(f'Normalized Distribution of Forman-Ricci Curvature for $T = {KT_VALUE}$')
        plt.xlabel('Forman-Ricci Curvature')
        plt.ylabel('Density')
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=1)
        plt.tight_layout()
        plt.savefig(name_image)
        plt.close()

        return frc_total

