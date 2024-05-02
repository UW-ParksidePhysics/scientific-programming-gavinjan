from matplotlib.figure import figaspect
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, show, thetagrids
import numpy as np

# known values for the functions
density = 1.225 #the average density of air

velocity = 27 #set velocity of the car

speeds = np.array([15, 30, 45, 60, 75, 90]) #variable speeds for the car

length = 2.0 #fixed length of the aerodynamic service

coeficient_of_drag = 0.09 #coefficient of drag for an air foil

distance = 0.5 #fixed length of the aerodynamic surfaces hypotenuse

theta = np.radians([15, 30, 45, 60, 75, 90]) #list of possible angles
theta=np.radians(np.linspace(15, 90, 600)) #array of angles from 15 to 90 degrees
optimised_angle = np.radians(45) #the calculated optimal angle of attack for the control surface


#drag formula
def area_of_drag(length, distance, theta):
    return length * distance* np.sin(theta)


areas_drag= (area_of_drag(2, 0.5, theta))
print(areas_drag)


def F_drag(area_of_drag, velocity, density, coeficient_of_drag):
    return 0.5 * density * area_of_drag * velocity**2 * coeficient_of_drag


drags= (F_drag(areas_drag, 27, 1.225, 0.09))
print(drags)


#downforce formula
def area_of_downforce(length, distance, theta):
    return length * distance* np.cos(theta)

areas_downforce= (area_of_downforce(2, 0.5, theta))
print(areas_downforce)


def F_downforce(area_of_downforce, velocity, density, coeficient_of_drag):
    return 0.5 * density * area_of_downforce * velocity**2 * coeficient_of_drag

downforces= (F_downforce(areas_downforce, 27, 1.225, 0.09))
print(downforces)


#optimised drag formula
def optimised_area_of_drag(length, distance, optimised_angle):
    return length * distance* np.sin(optimised_angle)


optimised_areas_drag = optimised_area_of_drag(2, 0.5, optimised_angle)
print(optimised_areas_drag)


def optimised_F_drag(optimised_area_of_drag, speeds, density,coeficient_of_drag):
    return 0.5 * density * optimised_area_of_drag * speeds**2 * coeficient_of_drag

optimised_F_drags = optimised_F_drag(optimised_areas_drag, speeds, 1.225, 0.09)
print(optimised_F_drags)



#optimised downforce formula
def optimised_area_of_downforce(length, distance, optimised_angle):
    return length * distance* np.cos(optimised_angle)

optimised_areas_downforces= optimised_area_of_downforce(2, 0.5, optimised_angle)
print(optimised_areas_downforces)


def optimised_F_downforce(optimised_area_of_downforce, speeds, density,coeficient_of_drag):
    return 0.5 * density * optimised_area_of_downforce * speeds**2 * coeficient_of_drag

optimised_F_downforces= optimised_F_downforce(optimised_areas_downforces, 27, 1.225, 0.09)
print(optimised_F_downforces)


#plotting both aerodynamic components
def plot_drag(length, distance, theta):
    plot(theta, area_of_drag(length, distance, theta))
    plt.xlabel('Angle of attack [degrees]')
    plt.ylabel('drag [N]')
    plt.scatter(theta, drags, color='red')
    plt.title('angle of attack vs drag')
    show()


def plot_downforce(length, distance, theta):
    plot(theta, area_of_downforce(length, distance, theta))
    plt.xlabel('Angle of attack [degrees]')
    plt.ylabel('downforce [N]')
    plt.scatter(theta, downforces, color='blue')
    plt.title('angle of attack vs downforce')
    show()


#plotting combined aerodynamic components
angles=np.degrees(theta)
plt.plot(angles, downforces, color ='red', label=('downforce'))
plt.plot(angles, drags, color = 'blue', label=('drag'))
plt.legend()
plt.xlabel('angle of attack [degrees]')
plt.ylabel('force [N]')
plt.axvline(45, color='black', linestyle='--', label=('optimal angle'))
plt.show()




if __name__ == '__main__':
    plot_drag(2, 0.5, theta)
    plot_downforce(2, 0.5, theta)