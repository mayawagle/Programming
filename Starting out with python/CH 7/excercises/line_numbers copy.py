#This program gets the file name from a user
#it then displays the contents of the file
#with each line preceeded with a line number
#followed by a colon

#define the main
def main():
    #get the name of the file
    # file_name = input('Enter the filename:')
    
    #open the file
    file_name = "names.txt"
    infile = open(file_name, 'r')
    number = 1
    for line in infile:
        # line = line.strip('\n')
        line = line.strip('\n')
        print(f'line {number}: {line}')
        number += 1
    #close the file
    infile.close()

#run the main
main()