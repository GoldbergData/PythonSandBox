# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai': 17.8, 'Istanbul': 20.0, 'Karachi': 13.0, 'Mumbai': 12.5}

def get_key(input_dict, key):
    return max(input_dict[key])

print(max(population, key=lambda key: population[key]))

#print(get_key(population))

print(max(population))