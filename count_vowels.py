# coding=utf-8
def count_vowels(a: object) -> object:
    lower_a = a.lower()
    vowels = 'aeiou'
    vowel_count = 0
    for i in vowels:
        vowel_count += lower_a.count(i)
    return vowel_count


prophecy = "And there shall in that time be rumours of things going astray, " \
           "and there will be a great confusion as to where things really are, " \
           "and nobody will really know where lieth those little things with the sort of raffia work base, " \
           "that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not " \
           "know where lieth the things possessed by their fathers that their fathers put there only just the night " \
           "before around eight o’clock… "

# TODO: set the value of vowel_count to be the number of vowels in prophecy


# Print the final count
print(count_vowels(prophecy))
