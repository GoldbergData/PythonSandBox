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
    for i in range(len(input_list)):
        j = i + 1
        print("debug: i: {}".format(i))
        print("debug: j: {}".format(j))
        while j < length:
            if i > 0:
                print("debug inside if: i: {}".format(i))
                input_list.insert(0, input_list[i])
                print("debug after if: i: {}".format(input_list[0]))
            print("debug: input_list[i]: {}".format(input_list[i]))
            print("debug: input_list[j]: {}".format(input_list[j]))
            if input_list[0] == input_list[j]:
                del input_list[j]
            j += 1
    return input_list







countries = ['Angola', 'Maldives', 'India', 'United States', 'India']
print(remove_duplicates(countries))