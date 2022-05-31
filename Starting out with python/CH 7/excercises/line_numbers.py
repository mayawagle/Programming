#This program gets the file name from a user
#it then displays the contents of the file
#with each line preceeded with a line number
#followed by a colon

#define the main
def main():
    #get the name of the file
    file_name = input('Enter the filename:')
    #open the file
    infile = open(file_name, 'r')
    number = 1
    for line in infile:
        line = line.strip('\n')
        line = line.strip('\n')
        print(line)
        print(f'line{number}: {infile.readline()}', end='')
        number += 1
    #close the file
    infile.close()

#run the main
main()