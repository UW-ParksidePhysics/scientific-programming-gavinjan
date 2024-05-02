import numpy as np



def mass(density, volume):
  mass = density * volume
  return mass

density = [.7870, .0012, .9167, 1.050, 2.1450, 0.750, 1.00]
volume = [1000, 1000, 1000, 1000, 1000, 1000, 1000]


for index in range(len(density)):
  print(f'Mass of {index} is {mass(density[index], volume[index])}')
