# Implement the nearest_square function. The function takes an integer argument limit, and returns the largest square
# number that is less than limit. A square number is the product of an integer multiplied by itself, for example 36
# is a square number because it equals 6*6.

# There's more than one way to write this code, but I suggest you use a while loop!


def nearest_square(limit):
    i = 1
    square_number = 0
    while square_number < limit:
        square_number = i ** 2
        i += 1
        if i ** 2 >= limit:
            break
    return square_number


# Here is a test case you can copy to test your code. Feel free to write additional tests too!

test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))

test2 = nearest_square(200)
print("expected result: 196 actual result: {}".format(test2))