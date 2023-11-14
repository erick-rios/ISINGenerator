from isingenerator.lattice_square import LatticeSquare

matriz = LatticeSquare(4,4,0.5)

print(matriz.create_matrix())
print(matriz.random_position())
print(repr(matriz))
print(str(matriz))