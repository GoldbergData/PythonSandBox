# Write a function, remove_duplicates that takes a list as its argument and returns a new list containing the unique
# elements of the original list. The elements in the new list without duplicates can be in any order.

# Suggested test cases: Try an input list with no duplicate elements. The output list should be the same size as the
# original list. Try a small input list with a known number of unique entries, and some duplicates. Verify that the
# list without duplicates has the correct length.

def remove_duplicates(input_list):
    """

    :param input_list: list
    :return: returns a new list containing the unique
             elements of the original list.
    """
    length = len(input_list)
    for i in range(length):
        length = len(input_list)
        j = 0
        if i >= length:
            break
        while j < (length - 1):
            if input_list[i] != input_list[j]:
                j += 1
            if input_list[i] == input_list[j]:
                if i == j:
                    j += 1
                    pass
                else:
                    del input_list[j]
                    length = len(input_list)
    return input_list


test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 10, 10, 10]
test2 = [2, 2, 3, 3, 5, 5, 5, 5, 5, 5]
test3 = ['Angola', 'Maldives', 'India', 'United States', 'India']
print(remove_duplicates(test1))
