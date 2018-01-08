# Time to get that final helper function completed, score_to_rating_string! Here's the table to remind you of how
# the values map to ratings.

# Average Score	Rating
# 0 <= score < 1	Terrible
# 1 <= score < 2	Bad
# 2 <= score < 3	OK
# 3 <= score < 4	Good
# 4 <= score <= 5	Excellent

def score_to_rating_string(score):
    """
    :param score: float
    :return: return rating assigned by rubric
    """
    rating = None
    if score >= 0 and score < 1:
        rating = "Terrible"
    elif score >= 1 and score < 2:
        rating = "Bad"
    elif score >= 2 and score < 3:
        rating = "OK"
    elif score >= 3 and score < 4:
        rating = "Good"
    elif score >= 4 and score < 5:
        rating = "Excellent"
    if rating:
        return rating
    else:
        return "Oh dear, no rating this time."

print(score_to_rating_string(0.5))
print(score_to_rating_string(1.5))
print(score_to_rating_string(2.5))
print(score_to_rating_string(3.5))
print(score_to_rating_string(4.5))
