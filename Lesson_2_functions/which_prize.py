# In this quiz, implement a function called which_prize() that notifies a competitor of the
# prize they have won in a game, depending on the number of points they've scored.

# Points	Prize
# 0 - 50	wooden rabbit
# 51 - 150	No prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin

# The input to which_prize() will be the number of points (an integer). The function which_prize() should return
# the text "Congratulations! You have won a [prize name]!" with the prize name included if they have won a prize and
# the text "Oh dear, no prize this time." if there is no prize. As always, test your function to check whether
# it's performing correctly.

def which_prize(points):
    prize_one = "wooden rabbit"
    prize_three = "wafer-thin mint"
    prize_four = "penguin"
    if points < 0 or (points >= 51 and points <= 150):
        return "Oh dear, no prize this time."
    elif points >= 0 and points <= 50:
        return "Congratulations! You have won a {}!".format(prize_one)
    elif points >= 151 and points <= 180:
        return "Congratulations! You have won a {}!".format(prize_three)
    elif points >= 181 and points <= 200:
        return "Congratulations! You have won a {}!".format(prize_four)


print(which_prize(-1))
print(which_prize(25))
print(which_prize(75))
print(which_prize(175))
print(which_prize(190))