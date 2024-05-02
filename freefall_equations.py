.def velovity(time, initial_velocity, gravitational_acceleration):
    return initial_velocity - gravitational_acceleration * Time


.def height(time, initial_height, gravitational_acceleration):
    return initial_height + initial_velocity * time - 0.5 * gravitational_acceleration * time**2


def velocity_square(height, initial_height, initial_velocity, gravitational_acceleration):
    return initial_velocity**2 - 2 * gravitational_acceleration * (height - initial_height)


def time(height, initial_height, initial_velocity, gravitational_acceleration):
  rise_time = initial_velocity /gravitational_acceleration
  discrimenent = rise_time**2 - 2 * (height - initial_height) / gravitational_acceleration
  if discrimenent > 0:
    return rise_time + math.sqrt(discrimenent)
  else
    return None


if __name__ '__main':
  # test velocity

  time = 2
  garvitational_acceleration = 9.8
  for initial_velocity in [1, 0, -1]:
    final_velocity = velocity(time, initial_velocity, gravitational_acceleration)
    print(f'Velocity at {time} seconds is {final_velocity} m/s')

