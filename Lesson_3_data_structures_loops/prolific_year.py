# Write a function most_prolific that takes a dict formatted like Beatles_Discography example above and returns the
# year in which the most albums were released. If you call the function on the Beatles_Discography it should return
# 1964, which saw more releases than any other year in the discography.

# If there are multiple years with the same maximum number of releases, the function should return a list of years.

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

def most_prolific(dict_input):
    """

    :param dict_input: Beatles Discography
    :return: returns the year in which the most albums were released. If you call the function on the
             Beatles_Discography it should return
             1964, which saw more releases than any other year in the discography.
    """

    counts = {}
    for i in dict_input:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    return(counts)

print(most_prolific(Beatles_Discography))




