import numpy as np

inch_to_cm = 2.54
foot_to_inch = 12
yard_to_feet = 3
mile_to_yard = 1760
meter_to_cm = 100
kilometer_to_meter = 1000

my_house_in_kilometers= (8.4 * mile_to_yard * yard_to_feet * foot_to_inch * inch_to_cm) / (meter_to_cm * kilometer_to_meter)

print(f'My house is {my_house_in_kilometers} kilometers away')