import numpy as np
from isingenerator.ising_model_2d import IsingModel2D

matriz = np.array([[1,1,1,1],[-1,1,1,-1],[1,1,-1,1],[1,1,1,1]])

ising_model = IsingModel2D(matriz)
print(ising_model.calculate_energy())
print(ising_model.calculate_magnetization())
print(repr(ising_model))
print(str(ising_model))