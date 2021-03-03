# Torrey Brett PSID: 1498427

def get_cost(s):
    if s == 'Oil change':
        return 35
    if s == 'Tire rotation':
        return 19
    if s == 'Car wash':
        return 7
    if s == 'Car wax':
        return 12


print('Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n')

first = input('Select first service:\n')
second = input('Select second service:\n')

print('\nDavy\'s auto shop invoice\n')

one = get_cost(first)
two = 0
print('Service 1: %s, $%d' % (first, one))
if second == '-':
    print('Service 2: No service')
else:
    two = get_cost(second)
    print('Service 2: %s, $%d' % (second, two))

print('\nTotal: $%d' % (one + two))
