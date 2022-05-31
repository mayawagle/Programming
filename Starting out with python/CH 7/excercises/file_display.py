#This program assumes there is a numbers.txt file on the 
#disk. It then displays the numbers in this "file"

def main():
    #open the file
    infile = open('numbers.txt', 'r')

    #read the file
    file_contents = infile.read()

    #close the file
    infile.close()

    #print file contents
    print(file_contents)
    
#call the main
main()