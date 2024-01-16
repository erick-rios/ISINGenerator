from src.isingenerator.topological_variables import TopologicalVariables
import numpy as np
import time



# Crea una matriz de 1000x1000 con entradas aleatorias de 1 o -1
matrix = np.random.choice([-1], size=(10, 10))
start_time = time.time()
print(matrix)
print("label matrix",TopologicalVariables.get_labels())
print("Number of labels", TopologicalVariables.get_num_labels())
print("Max number of label", TopologicalVariables.get_max_label())

TopologicalVariables.label_ring(matrix)
print("label matrix",TopologicalVariables.get_labels())
print("Number of labels", TopologicalVariables.get_num_labels())
print("Max number of label", TopologicalVariables.get_max_label())
end_time = time.time()
execution_time = end_time -start_time
print("Execution time: ", execution_time)

#print("Primera parte")
print("Domains of the matrix", TopologicalVariables.find_domains())
print("Number of domains", TopologicalVariables.number_of_domains())
print("Tamaño de los dominios", TopologicalVariables.length_of_domains())
print("MDS", TopologicalVariables.mean_domain_size())