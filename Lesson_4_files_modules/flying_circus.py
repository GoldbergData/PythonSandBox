# You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.

# Write a function called create_cast_list that takes a filename as input and returns a list of actors' names. It
# will be run on the file flying_circus_cast.txt (this information was collected from imdb.com). Each line of that
# file consists of an actor's name, a comma, and then some (messy) information about roles they played in the
# programme. You'll need to extract only the name and add it to a list. You might use the .split() method to process
# each line.

import re

def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    # use the for loop syntax to process each line
    # and add the actor name to cast_list

    with open(filename) as f:
        # p = re.compile('^[a-z ]+', re.IGNORECASE) tried regex for fun, but line split is much easier
        for line in f:
            # matched = p.match(line)
            # if matched:
            line_data = line.split(',')
            cast_list.append(line_data[0])
            # cast_list.append(matched.group())
    return cast_list

print(create_cast_list('flying_circus_cast.txt'))

