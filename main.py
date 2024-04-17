import matplotlib as plt
from matplotlib.pyplot import plot, show
import numpy as np


density = 1.225

velocity = 27

length = 2.0

coeficient_of_drag = 0.09

distance = 0.5

theta = np.radians([15, 25, 30, 35, 40, 45])

def area_of_drag(length, distance, theta):
    return length * distance* np.sin(theta)
  

areas_drag= (area_of_drag(2, 0.5, theta))
print(areas_drag)


def F_drag(area_of_drag, velocity, density, coeficient_of_drag):
    return 0.5 * density * area_of_drag * velocity**2 * coeficient_of_drag


drags= (F_drag(areas_drag, 27, 1.225, 0.09))
print(drags)


def area_of_downforce(length, distance, theta):
    return length * distance* np.cos(theta)

areas_downforce= (area_of_downforce(2, 0.5, theta))
print(areas_downforce)


def F_downforce(area_of_downforce, velocity, density, coeficient_of_drag):
    return 0.5 * density * area_of_downforce * velocity**2 * coeficient_of_drag

downforces= (F_downforce(areas_downforce, 27, 1.225, 0.09))
print(downforces)


def plot_drag(length, distance, theta):
    plot(theta, area_of_drag(length, distance, theta))
    plt.xlabel('Angle of attack [degrees]')
    plt.ylabel('drag [N]')
    show()

if __name__ == '__main__':
    plot_drag(2, 0.5, theta)