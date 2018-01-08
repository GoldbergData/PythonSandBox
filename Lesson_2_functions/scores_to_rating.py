def convert_to_numeric(number):
    """
    Convert the score to a float.
    """
    return float(number)

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

def scores_to_rating(score1, score2, score3, score4, score5):
    """
    :param score1: float, int, string
    :param score2: float, int, string
    :param score3: float, int, string
    :param score4: float, int, string
    :param score5: float, int, string
    :return: Assigned rating based on rubric.
    """
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    middle_sum = sum_of_middle_three(score1, score2, score3, score4, score5)

    average_sum = middle_sum / 3

    rating = score_to_rating_string(average_sum)
    return rating


print(scores_to_rating(1, 2, 3, 4, 5))
