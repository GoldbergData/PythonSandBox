# Write a function, tag_count, that takes as its argument a list of strings. It should return a count of how many of
# those strings are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it
# begins with a left angle bracket "<" and end with a right angle bracket ">".

# You can assume that the list of string that will be given as input will not contain empty strings.

# TODO: Define the tag_count function

import re


def tag_count(input_list):
    p = re.compile('<\W*\w*>')
    counter = 0
    for i in input_list:
        matched = (p.match(i))
        if matched:
            print(matched.group())
        if matched:
            counter += 1
    return counter


# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))
