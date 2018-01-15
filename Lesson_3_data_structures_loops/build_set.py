# In a similar way to building an empty list with my_list = [], you can create an empty set with my_set = set().
# Using this technique, and the add method, build a set of all of the square numbers greater than 0 and less than 2,000.
# For reference, I included my implementation of nearest_square function from an earlier quiz. You may call the
# function in your code, integrate it into your code, or ignore it altogether.

# Note: If you want to call the nearest_square function, you must define
# the function on a line before you call it. Feel free to move this code up!
def nearest_square(limit):
    squares = set()
    answer = 0
    while (answer + 1) ** 2 < limit:
        answer += 1
        squares.add(answer ** 2)
    return squares



# todo: populate "squares" with the set of all of the integers less
# than 2000 that are square numbers

squares = (nearest_square(2000))

print(squares)