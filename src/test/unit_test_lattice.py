import sys
sys.path.append('/home/soundskydriver/Documents/ISINGMODEL2DGenerator/src')



from LatticeSquare import *

matriz = LatticeSquare(4,4,0.5)

print(matriz.create_matrix())
print(matriz.random_position())