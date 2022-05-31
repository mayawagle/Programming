#This program reads a file of world series winners (WorldSeriesWinners.txt)
#into a list. It then prompts the user to enter a team and the it 
#displays how many times them team has won

#define the main
def main():
    #read the contents of the file into a list
    infile = open('WorldSeriesWinners.txt','r')
    winners = infile.readlines()
    infile.close()
    
    #strip the newline character
    index = 0
    while index < len(winners):
         winners[index] = winners[index].rstrip('\n')
         index+= 1
    
    #get the team the user wants to look up
    user_team = input('Enter the team you would like to look up: ')

    #look up the team and display results
    times = 0
    for item in winners:
        if item == user_team:
            times += 1
    
    if times < 1:
        print('The team you entered has not won a World Series between 1903 and 2009')
    else:
        print(f'The team you have enetered has won {times} times between 1903 and 2009.')


#run the main
main()