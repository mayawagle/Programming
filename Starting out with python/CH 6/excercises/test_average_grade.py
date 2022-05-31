#this program takes five test scores from the user and displays
#a letter grade for each score and then the average score

#define the main
def main():
    #get the scores
    score1 = float(input('Enter score 1: '))
    score2 = float(input('Enter score 2: '))
    score3 = float(input('Enter score 3: '))
    score4 = float(input('Enter score 4: '))
    score5 = float(input('Enter score 5: '))
    
    #format a table
    print('score\tletter grade')
    print('--------------------------')

    #write a loop and table
    for score in (score1,score2,score3,score4,score5):
        print(f'{score}\t{determine_grade(score)}')
    
    #calculate the average
    print(f'The average score is {format(calc_average(score1,score2,score3,score4,score5), ".2f")}.')


#define the calc_average function
def calc_average(score1,score2,score3,score4,score5):
    return (score1 + score2 + score3 + score4 + score5) / 5

#define the determine_grade function
def determine_grade(score):
    if 90 >= score and 100<= score:
        return 'A'
    elif 80 >= score and 89<= score:
        return 'B'
    elif 70 >= score and 79 <= score:
        return 'C'
    elif 60 >= score and 69 <= score:
        return 'D'
    elif score < 60:
        return 'F'
    else:
        return 'ERROR: Score not in range'

#define main
main()