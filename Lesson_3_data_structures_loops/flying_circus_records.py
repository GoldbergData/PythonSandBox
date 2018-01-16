# A regular flying circus happens twice or three times a month. For each month, information about the amount of money
# taken at each event is saved in a list, so that the amounts appear in the order in which they happened. The
# months' data is all collected in a dictionary called monthly_takings.

# For this quiz, write a function total_takings that calculates the sum of takings from every circus in the year.
# Here's a sample input for this function:

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

def total_takings(monthly_takings):
    pass # TODO: Implement this function
    total = []
    for i in monthly_takings:
        total.append(sum(monthly_takings[i]))
    return sum(total)

print(total_takings(monthly_takings))