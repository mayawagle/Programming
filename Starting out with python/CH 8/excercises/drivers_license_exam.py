#this program reads the answers of the user from
#a text file to a list. It then determines the score 
#of the user based on the list of correct answers

#import mmodeules to be used
import random

#write the file of answers (using random answers to test)
outfile = open('user_answers.txt', 'w')
for num in range(20):
    answer_num = random.randint(1,5)
    if answer_num == 1:
        letter = 'A'
    elif answer_num == 2:
        letter = 'B'
    elif answer_num == 3:
        letter = 'C'
    else:
        letter = 'D'
    outfile.write(letter + '\n')
outfile.close()

#define the main
def main():
    #define the constant answer list
    correct_answers = ['B','D','A','A','C','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A']
   
    #read the users answers to a list
    infile = open('user_answers.txt', 'r')
    user_list = infile.readlines()


    #close the file 
    infile.close()

    
    #strip the newline characters from the list
    index = 0
    while index < len(user_list):
        user_list[index] = user_list[index].rstrip('\n')
        index += 1
   
    
    #determine how many answers the user got correct
    number_right = 0
    index = 0
    questions_wrong = []
    while index < len(user_list):
        if user_list[index] == correct_answers[index]:
            number_right += 1
        else:
            questions_wrong.append(index + 1)
        index += 1

    print(number_right)

    #determine if the user psssed
    if number_right >= 15:
        pass_fail = 'passed'
    else:
        pass_fail = 'failed'
    #print the results
    print(f'The student {pass_fail} the exam.')
    print(f'They answered {number_right} out of the 20 questions correctly.')
    if len(questions_wrong) > 0:
        print('The student answered these wuestions wrong:')
        print(questions_wrong)

#run the main
main()