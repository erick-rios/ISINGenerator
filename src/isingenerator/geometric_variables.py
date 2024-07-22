import csv

import networkx as nx
import numpy as np

from typing import Tuple

class GeometricVariables:
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
    def forman_ricci_curvature_edge(graph: nx.Graph, output_file: str) -> float:
        """
        Computes the Forman-Ricci curvature for each edge in the given graph, calculates the total Forman-Ricci curvature of the graph,
        and saves the results in a CSV file.

        The Forman-Ricci curvature for an edge is calculated based on the degrees of the nodes connected by the edge.

        Args:
            graph (nx.Graph): An undirected graph.
            output_file (str): The path to the output CSV file.

        Returns:
            float: The total Forman-Ricci curvature of the graph.
        """
        frc_total = 0

        # Compute Forman-Ricci curvature for each edge
        for node in graph.nodes:
            neighbors = list(graph.neighbors(node))
            for neighbor in neighbors:
                frc = -graph.degree(node) - graph.degree(neighbor)
                graph[node][neighbor]["forman_ricci_curvature"] = frc

        # Open the CSV file for writing
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['u', 'v', 'forman_ricci_curvature'])  # Write the header

            # Write the edges and their Forman-Ricci curvature to the CSV file
            for u, v, data in graph.edges(data=True):
                frc_total += data["forman_ricci_curvature"]
                writer.writerow([u, v, data["forman_ricci_curvature"]])
        
        return frc_total


