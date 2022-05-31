#This program assumes that there is a numbers.txt file
#it then calculates and displays the average

def main():
    #open the numbers.txt file
    infile = open('numbers.txt', "r")

    #write a loop to get the total
    total = 0
    numbers = 0

    #do a prime read 
    line = infile.readline()

    #write the loop
    while line != "":
        total += float(line)
        numbers += 1
        line = infile.readline()
    
    #close the file
    infile.close()
    
    #print the average
    print(f'The average is {format(total/numbers, ".2f")}.')
    
#call the main
main()

