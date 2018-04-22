# Quiz: readable_timedelta Write a function named readable_timedelta. The function should take one argument,
# an integer days, and return a string that says how many weeks and days that is. For example, calling the function
# and printing the result like this:

# print(readable_timedelta(10))
#
# 1 week(s) and 3 day(s).

# Include a docstring that explains what the function does.

# write your function here
def readable_timedelta(days):
    """
    :param days: an integer that expresses number of days
    :return: returns number of weeks and days as remainder
    """

    return("{} week(s) and {} day(s).".format(days // 7, days % 7))


# test your function
print(readable_timedelta(20))