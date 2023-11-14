import sys
sys.path.append('../../src')

from TopologicalVariables import *
import numpy as np

matriz = np.array([[1,1,1,1],[-1,1,1,-1],[1,1,-1,1],[1,1,1,1]])

TopologicalVariables.find_domains(matriz)
TopologicalVariables.length_of_domains(matriz)
TopologicalVariables.mean_domain_size(matriz)
TopologicalVariables.label_ring(matriz)
TopologicalVariables.number_of_domains(matriz)