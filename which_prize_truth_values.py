# Rewrite the which_prize() function from earlier to use what you've learned about truth values. Start your function
# by setting the variable prize = None, change the prize depending on the number of points and then use another
# conditional to return a message depending on whether prize is there or not. This will avoid repeating the return
# part of the code.

# Points	Prize
# 0 - 50	wooden rabbit
# 51 - 150	No prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin

def which_prize(points):
    prize = None
    if points < 0 or (points >= 51 and points <= 150):
        prize = "Oh dear, no prize this time."
    elif points >= 0 and points <= 50:
        prize = "Congratulations! You have won a wooden rabbit!"
    elif points >= 151 and points <= 180:
        prize = "Congratulations! You have won a wafer-thin mint!"
    elif points >= 181 and points <= 200:
        prize = "Congratulations! You have won a penguin!"
    if prize:
        return prize
    else:
        return "Oh dear, no prize this time."

print(which_prize(-1))
print(which_prize(25))
print(which_prize(75))
print(which_prize(175))
print(which_prize(190))