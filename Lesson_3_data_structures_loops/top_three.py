# Write a function, top_three, that takes a list as its argument, and returns a list of the three largest elements.
# For example, top_three([2,3,5,6,8,4,2,1]) == [8, 6, 5]

def top_three(input_list):
    """
    :param input_list: list
    :return: Returns a list of the three largest elements input_list in order from largest to smallest.
    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    sorted_list = sorted(input_list, reverse=True)
    return sorted_list[:3]


print(top_three([2, 3, 5, 6, 8, 4, 2, 1]))
