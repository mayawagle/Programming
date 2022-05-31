#This program displays the contents of the file made
#in golf_scores_write.py

#define the main
def main():
    #open the file
    infile = open('scores.txt', "r")

    #do a priming read
    name = infile.readline()

    #initiate the while loop
    while name != "":
        #read the score
        score = infile.readline()

        #strip the newlines from the fields
        name = name.rstrip('\n')
        score = score.rstrip('\n')

        #display the record
        print(f'Name: {name}')
        print(f'score: {score}')
        print()

        #move onto the next record
        name = infile.readline()
    
    #close the file
    infile.close()

#call the main
main()