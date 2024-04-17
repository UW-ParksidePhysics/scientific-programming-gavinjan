def convert_ferenheight_temperature_to_celcius_temperature(farhenheit_temperature):
  return (5./9)*(farhenheit_temperature - 32)


def convert_celcius_temperature_to_ferenheight_temperature(celcius_temperature):
  return (9./5)*celcius_temperature + 32


if __name__ == "__main__":
  celcius_temperature = [0, 21, 100]
print('T_C\t\tT_C(T_F(T_C))')
for some_celcius_temperature in celcius_temperature:
  converted_temperature = convert_ferenheight_temperature_to_celcius_temperature(convert_celcius_temperature_to_ferenheight_temperature(some_celcius_temperature))
  print(f'{some_celcius_temperature} = {converted_temperature:.0f}')