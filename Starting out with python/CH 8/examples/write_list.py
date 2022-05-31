#This program writes a list of strings to a file

def main():
    #create a list of strings
    cities = ['New york', 'Boston', 'Atlanta', 'Dallas']

    #open a file for writing
    outfile = open('cities.txt', 'w')

    #write the list to the file
    for item in cities:
        outfile.write(item + '\n')
    
    #close the file
    outfile.close()

#call the main
main()