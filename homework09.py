# For this homework assignment I had to creat a program that uses a list to store quiz scores and get the average of
# the scores, and show the grade letter.

# I first had to define the functions that would be used later in the program. The first def function is getting the
# number of scores that will be input by the user.
# The second def function is getting the average of all quiz scores that was entered by the user.

def get_quiz_score():
    score = int(input("Enter a score "))
    return score

def average(total, number_of_scores):
    avg = float()
    if number_of_scores != 0:
        avg = total / number_of_scores
    return avg

# The mainline function is where I prompt the user to enter the information, so they can see the average score and
# the letter grade.

# I declared the variables at the top that I will be using for the program.

score = int()
total = int()
quiz_scores = list()
grade_A = int()
grade_B = int()
grade_C = int()
grade_D = int()
grade_F = int()
number_of_scores = int(input("How many scores? "))

# For the first loop, is where the number of scores that was entered by the user
# will be gathered to get the average score.

avg_sc = int()
while avg_sc < number_of_scores:
    score = int(get_quiz_score())
    quiz_scores.append(score)
    total += score
    avg_sc += 1
print("Average score: ", average(total, number_of_scores))


# For the second loop, is where the quiz scores is assigned to a letter grade. Afterwards, it will be stored either in
# the grade letter A,B,C,D,F. The output will show the letter grade and the total number of scores with that grade.

grade_let = 0
while grade_let < len(quiz_scores):
    if quiz_scores[grade_let] >= 90:
        grade_A += 1
    elif 80 <= quiz_scores[grade_let] < 90:
        grade_B += 1
    elif 70 <= quiz_scores[grade_let] < 80:
        grade_C += 1
    elif 60 <= quiz_scores[grade_let] < 70:
        grade_D += 1
    elif quiz_scores[grade_let] < 60:
        grade_F += 1
    grade_let += 1
print("Number of A grades: ", grade_A)
print("Number of B grades: ", grade_B)
print("Number of C grades: ", grade_C)
print("Number of D grades: ", grade_D)
print("Number of F grades: ", grade_F)


