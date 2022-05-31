#this program asks the the user for the 
#name of a file. It then displays the first
#5 lines of the file or all of the file if there is less than 5 lines

def main():
    #get the file name from the user
    file_name = input('What is the name of the file?: ')

    #open the file
    infile = open(file_name, 'r')

    #make a loop
    for x in range(0,5):
        # print(x)
        # line = infile.readline()
        print(infile.readline(), end="")
        # print(line)

    infile.close()
        
#run the main
main()