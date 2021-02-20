states = {
    'oregon': 'or',
    'florida': 'fl',
    'california': 'ca',
    'new york': 'ny',
    'michigan': 'mi'
}

cities = {
    'ca': 'san francisco',
    'mi': 'detroit',
    'fl': 'jacksonville'
}

cities['ny'] = 'new york'
cities['or'] = 'portland'

print('-' * 10)
print('ny state has: ', cities['ny'])
print('or state has: ', cities['or'])

print('-' * 10)
print("michigan's abbreviation is: ", states['michigan'])
print("florida's abbreviation is: ", states['florida'])

print('-' * 10)
print('michigan has: ', cities[states['michigan']])
print('florida has: ', cities[states['florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('texas')

if not state:
    print("sorry, no taxas.")

city = cities.get('tx', 'does not exist')
print(f"the city for the state 'tx' is: {city}")
