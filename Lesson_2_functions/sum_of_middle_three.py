# Now it's time to complete the sum_of_middle_three function. Make sure that you test it out using print statements.
# You can start with an outline you wrote earlier. You can find the maximum and the minimum by using max() and min().
#  max() returns the maximum out of a group of numbers, and min() returns the minimum. For example:
# max(1,2,3,4) #returns 4
# min(1,2,3,4) #returns 1

def sum_of_middle_three(score1, score2, score3, score4, score5):
    """
    :param score1: float
    :param score2: float
    :param score3: float
    :param score4: float
    :param score5: float
    :return: Total of the middle three numbers
    """
    sum_of_middle = (score1 + score2 + score3 + score4 + score5) - max(score1, score2, score3, score4, score5) - min(
        score1, score2, score3, score4, score5)
    return sum_of_middle


print(sum_of_middle_three(1, 2, 3, 4, 5))
