#This program takes each player's name and golf score and writes it to a file
#namef golf.txt
#the program then reads the records from the golf.txt file and displays them

#define the main
def main():
    #get the number of scores to create
    num_scores = int(input('How many employee records do you want to create?: '))

    #open a file for writing
    scores_file = open("scores.txt", 'w')

    #initiate a loop to get data and write it to the file
    for count in range(1,num_scores + 1):
        #get the data
        print()
        print(f'Enter the data of player {count}')
        name = input("Name: ")
        golf_score = input("Golf score: ")

        #write the data as a record to the file
        scores_file.write(name + '\n')
        scores_file.write(golf_score + '\n')
    #close the file
    scores_file.close()
    print('Golf scores written to scores.txt.')

#run the main
main()
