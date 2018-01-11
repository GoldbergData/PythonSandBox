# In this quiz, make two changes to the program:

# Move (refactor) the code that checks the answers into a separate function. Give it a good name. Use a loop to call
# that function on each answer, so that there aren't five calls to the function. Improve the docstring and add
# comments to make the code easier to understand. This doesn't cover the whole list of improvements, but it's a good
# start! If you want to do more, feel free. Your code will be tested on some test cases, so just make sure it still
# works correctly!

def check_answer(my_answer, answer):
    if my_answer == answer:
        result = True
    else:
        result = False
    return result


def score_quiz(my_answers, answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results = []
    passing_score = 0.7
    index = 0

    for i in my_answers:
        results.append(check_answer(i, answers[index]))
        index += 1

    quiz_length = len(results)
    count_correct = sum(results)
    quiz_score = count_correct / quiz_length

    if quiz_score > passing_score:
        return "Congratulations, you passed the test! You scored {} out of {}.".format(count_correct, quiz_length)
    else:
        return "Unfortunately, you did not pass. You scored {} out of {}.".format(count_correct, quiz_length)


student_answers = [1, 1, 2, 3, 4, 5]
key_answer = [1, 1, 2, 3, 4, 5]

print(score_quiz(student_answers, key_answer))
