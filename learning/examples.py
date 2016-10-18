# very basic python training
name = input('What is your name: ')
print ('My name is', name)
age = int(input('How old are you?: '))
print (age)
print (name, 'is', age, 'years old')

# square
flo = float(input('Insert number to square: '))
print ('Result is', flo ** 2)

# lenght and area enclosed of circle
from math import pi
rad = float(input('Insert radius in cm: '))
print ('Length is', 2 * pi * rad, 'cm')
print ('Area enclosed is', pi * (rad ** 2), 'cm2')
