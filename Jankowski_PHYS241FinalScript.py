import numpy as np
import matplotlib.pyplot as plt


def matrix_generator(minimum_x, maximum_x, number_of_dimensions, potential_name, potential_parameter)


hbar = 1.0
mass = 1.0

grid_spacing = (maximum_x - minimum_x) / (number_of_dimensions - 1)
unit_prefactor = hbar**2 / (2 * mass * grid_spacing**2)


horizontal_grid = np.linspace(minimum_x, maximum_x, num=number_of_dimensions)
if potential_name == 'harmonic':
    angular_frequency = potential_parameter * hbar / (mass * (maximum_x - minimum_x)**2)
    reduced_potential = 0.5 * mass * np.power(angular_frequency * horizontal_grid, 2) / unit_prefactor


elif potential_name == 'sinusoidal':
  well_width = (maximum_x - minimum_x)
  wave_vector = np.pi / well_width
  pre_factor = 5 * potential_parameter * hbar**2 / (2. * mass * well_width**2)
  reduced_potential = pre_factor * np.sin(wave_vector * (horizontal_grid + 0.5*well_width)) / units_prefactor


elif potential_name == 'square':
well_width = (maximum_x - minimum_x) / 2.
well_depth = potential_parameter * well_width
number_of_well_points = int(number_of_dimensions / 2.)
number_of_outside_points = int(number_of_dimensions / 4.)
reduced_potential = np.zeros(len(horizontal_grid))
reduced_potential[0:number_of_outside_points] = well_depth
reduced_potential[number_of_well_points+number_of_outside_points:] = well_depth
reduced_potential /= units_prefactor


else:
    horizontal_grid = np.linspace(minimum_x, maximum_x, num=number_of_dimensions)
    reduced_potential = 0. * horizontal_grid

off_diagonal_terms_array = -1. * np.ones(number_of_dimensions-1)
diagonal_terms_array = np.full(number_of_dimensions, 2) + reduced_potential

matrix_one = np.diagflat(off_diagonal_terms_array, -1)
matrix_two = np.diagflat(diagonal_terms_array)
matrix_three = np.diagflat(off_diagonal_terms_array, 1)

matrix_total = units_prefactor*(matrix_one + matrix_two + matrix_three)

return matrix_total


if __name__ == "__main__":
  dimension_number = 400
  length_scale = 1
  x_range = [-2*length_scale, 2*length_scale]
  potential_names = ['harmonic', 'sinusoidal', 'square']

  for index, potential in enumerate(potential_names):

      hamiltonian_matrix = generate_matrix(x_range[0], x_range[1], dimension_number, potential, length_scale)
      print(f'H[{potential}, {dimension_number}] = {hamiltonian_matrix}')
      print()

      import matplotlib as mpl
      mpl.use('macosx')

      import matplotlib.pyplot as plt

      x_values = np.linspace(x_range[0], x_range[1], num=dimension_number)
      y_values = np.diag(hamiltonian_matrix)
      plt.plot(x_values, y_values)
      plt.xlabel(r'$x_i$')
      plt.ylabel(r'$H[x_i]$')
      plt.title(rf'$v =$ {potential}, $N = ${dimension_number}')
      plt.show()