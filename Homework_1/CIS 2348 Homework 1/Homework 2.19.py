# Torrey Brett PSID: 1498427

ammt_lemon_juice = int(input('Enter amount of lemon juice (in cups):\n'))  #entry of cups
ammt_water = int(input('Enter amount of water (in cups):\n'))
ammt_agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
ammt_servings = int(input('How many servings does this make?\n'))

print('')

print('Lemonade ingredients - yields', ('{:.2f}'.format(ammt_servings)), 'servings')  # 6 servings
print(('{:.2f}'.format(ammt_lemon_juice)), 'cup(s) lemon juice')
print(('{:.2f}'.format(ammt_water)), 'cup(s) water')
print(('{:.2f}'.format(ammt_agave_nectar)), 'cup(s) agave nectar\n')

servings_wanted = int(input('How many servings would you like to make?\n')) #input of 48 servings

print('')

print('Lemonade ingredients - yields', ('{:.2f}'.format(servings_wanted)), 'servings')

print(('{:.2f}'.format(ammt_lemon_juice * 8)), 'cup(s) lemon juice') #16 cups
print(('{:.2f}'.format(ammt_water * 8)), 'cup(s) water')#128 cups
print(('{:.2f}'.format(ammt_agave_nectar * 8)), 'cup(s) agave nectar\n') #20 cups

print('Lemonade ingredients - yields', ('{:.2f}'.format(servings_wanted)), 'servings')


format_lem_juice = float('{:.2f}'.format(ammt_lemon_juice))
integer_format_lem = float(format_lem_juice)
gallon_lem = ((integer_format_lem * 8.0) / 16)
print("{:.2f}".format(gallon_lem), 'gallon(s) lemon juice')

format_water = float('{:.2f}'.format(ammt_water))
integer_format_water = float(format_water)
gallon_water = ((integer_format_water * 8.0) / 16)
print("{:.2f}".format(gallon_water), 'gallon(s) water')

format_agave_nectar = float('{:.2f}'.format(ammt_agave_nectar))
integer_format_agave = float(format_agave_nectar)
print((integer_format_agave * 8.0) / 16, 'gallon(s) agave nectar')

