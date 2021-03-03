# Torrey Brett PSID: 1498427

import math
height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))

Area = width * height

print('Wall area:', Area, 'square feet')

paint = Area / 350
print('Paint needed:', '{:.2f}'.format(paint), 'gallons')

can = math.ceil(paint)
print('Cans needed:', can, 'can(s)\n')

paintColors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

color = input("Choose a color to paint the wall:")
print('')

if color in paintColors:
    print("Cost of purchasing {0} paint: ${1}".format(color, can*paintColors[color]))
else:
    print("Sorry!! {0} paint not found".format(color))
