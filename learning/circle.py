# first we need to import pi value from math library
from math import pi

# user input
rad = float(input('Insert radius in cm: '))

cor = rad >= 0

if cor:
    # read pi value from library
    print ('Imported value of pi is', pi)
    # radius and diameter print
    print ('Radius is', rad ,'cm')
    print ('Diameter is', 2 * rad, 'cm')
    # calculations of circle
    print ('Length of circumference is', 2 * pi * rad, 'cm')
    print ('Area enclosed is', pi * (rad ** 2), 'cm2')
    # calculations of sphere
    print ('Surface of sphere is', (4 * pi) * (rad ** 2), 'cm2')
    print ('Enclosed volume is', (4 / 3) * pi * (rad ** 3), 'cm3')
else:
    print ('Insert value higher than zero')
