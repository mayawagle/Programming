#This program displays the number of names that
#are in the names.txt file
def main():
    #open the file
    infile = open('names.txt', 'r')

    #priming read
    line = infile.readline()

    names = 0
    #write the while loop
    while line != "":
        names += 1
        line = infile.readline()

    #close the file
    infile.close()

    #print the number of names
    print(f'There are {names} names in the file.')

#run the main
main()