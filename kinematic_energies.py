# define kinetic energy function
#define potential energy function
#import height and velocity functions from freefall_kinematics
#define the array of times from 0-2 v_0/g
#plot the energy versus time
# predefine mass and initial velocity

import numpy as np
from freefall_equations import  height, velocity



def kinematic_energy(velocity, mass):
  return 0.5 * mass * velocity**2


def potential_energy(height, mass, gravitational_acceleration):
  return mass * gravitational_acceleration * height


def calculate_energies(mass, initial_height, initial_velocity, number_of_times, kinematic_energies,  gravitational_acceleration=9.8):
  end_time = 2 * initial_velocity / gravitational_acceleration 
  times = np.linspace(0, end_time, number_of_times)
  heights = height(times, initial_height, initial_velocity, gravitational_acceleration)
  velocities = velocity(times, initial_velocity, gravitational_acceleration)
  potential_energies = potential_energy(heights, mass, gravitational_acceleration=gravitational_acceleration)
  total_energies = kinematic_energies + potential_energies
  return times, kinematic_energies, potential_energies, total_energies


def plot_energies(times, kinematic_energies, potential_energies, total_energies):
  import matplotlib.pyplot as plt
  plt.plot(times, kinematic_energies, label='$k(t)$')
  plt.plot(times, potential_energies, label='$p(t)$')
  plt.plot(times, total_energies, label='$E(t)$')
  plt.xlabel('$t(s)$')
  plt.ylabel('$E(J)$')



if __name__ == '__main__':
  object_mass = 1.
  starting_height = 1.
  starting_velocity = 1.
  time_sample_number = 100
  def calculate_energies(object_mass, starting_height, starting_velocity, time_sample_number,)
  plot_energies(times_and_energies[0], times_and_energies[1], times_and_energies[2], time_sample_number[3])