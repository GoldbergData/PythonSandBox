# The function in this quiz, median, returns the median value of an input list. Unfortunately it only works with
# lists that have an odd number of elements. Modify the function so that when median is given a list with an even
# number of elements, it returns the mean of the two central elements. The provided test cases demonstrate the
# expected behavior.

def median(numbers):
    # The sort method sorts a list directly, rather than returning a new sorted list
    numbers.sort()
    print(str(len(numbers) / 2) + ' becomes ' + str(int(len(numbers) / 2)))
    if int(len(numbers) / 2) % 2 == 0:
        middle_index_one = int(len(numbers) / 2) - 1
        middle_index_two = int(len(numbers) / 2)
        return (numbers[middle_index_one] + numbers[middle_index_two]) / 2
    middle_index = int(len(numbers) / 2)
    return numbers[middle_index]


test1 = median([1, 2, 3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1, 2, 3, 4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))
