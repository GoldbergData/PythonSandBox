counts = {1963: 2, 1964: 3, 1965: 2, 1966: 1, 1967: 2, 1968: 1, 1969: 2, 1970: 1}


def my_lambda(count_index):
    print('debug: count_index: {}'.format(count_index))
    print('debug: counts[count_index]: {}'.format(counts[count_index]))
    return counts[count_index]

print(max(counts, key=my_lambda))


