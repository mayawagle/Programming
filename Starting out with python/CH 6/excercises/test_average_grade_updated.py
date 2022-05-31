#this program takes five test scores from the user and displays
#a letter grade for each score and then the average score

NUMBER_OF_SCORES = 5
#define the main
def main():
    #initiate sum variable
    sum = 0
    #get the scores, print gread, add to running total
    score1 = float(input('Enter score 1: '))
    print(score1)
    print(f'The letter grade is {determine_grade(score1)}')
    sum += score1
    score2 = float(input('Enter score 2: '))
    print(f'The letter grade is {determine_grade(score2)}')
    sum += score2
    score3 = float(input('Enter score 3: '))
    print(f'The letter grade is {determine_grade(score3)}')
    sum += score3
    score4 = float(input('Enter score 4: '))
    print(f'The letter grade is {determine_grade(score4)}')
    sum += score4
    score5 = float(input('Enter score 5: '))
    print(f'The letter grade is {determine_grade(score5)}')
    sum += score5

    #print the average score
    print(f'The average score is {format(calc_average(sum,NUMBER_OF_SCORES), ".2f")}')


#define the calc_average function
def calc_average(sum,num_of_values):
    return sum/ num_of_values

#define the determine_grade function
def determine_grade(score):
    if 90 <= score and 100>= score:
        return 'A'
    elif 80 <= score and 89>= score:
        return 'B'
    elif 70 <= score and 79 >= score:
        return 'C'
    elif 60 <= score and 69 >= score:
        return 'D'
    elif score < 60:
        return 'F'
    else:
        return 'ERROR: Score not in range'

#define main
main()