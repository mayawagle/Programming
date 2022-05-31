#this program uses the USPopulation.txt file and reads the contents into a list
#it then uses the list to determine the average annual change, year with the greatest
#increase in population and with the smallest increase

#define the main
import math


def main():
    #read the contents of the file to a list
    infile = open('USPopulation.txt', 'r')
    uspopulations = infile.readlines()
    infile.close

    #strip the newline characters/turn to int
    index = 0
    while index < len(uspopulations):
        uspopulations[index] = uspopulations[index].rstrip('\n')
        uspopulations[index] = int(uspopulations[index])
        index += 1
 
    #run a loop to get the changes into a list
    annual_changes = []
    index = 0
    while index < len(uspopulations) - 1:
        annual_changes.append(abs(uspopulations[index+1] - uspopulations[index]))
        index += 1
    
    total = 0
    #find the average annual change
    for num in annual_changes:
        total += num
    average = total / len(annual_changes)

    print(f'The average annual change in populations is {average}.')
    #find the year with the greatest increase in populations
    max = annual_changes[0]
    index = 0
    max_index = 0
    while index < len(annual_changes):
        if annual_changes[index] > max:
            max = annual_changes[index]
            max_index = index
        index+=1
    max_increase_year = 1950 + max_index + 1
    print(f'The greatest increase in population occurs in the year {max_increase_year}. ')
    
    #find the year with the greatest decrease in populations
    min= annual_changes[0]
    index = 0
    min_index = 0
    while index < len(annual_changes):
        if annual_changes[index] < min:
            min = annual_changes[index]
            min_index = index
        index+=1
    min_increase_year = 1950 + min_index + 1
    print(f'The greatest decrease in population occurs in the year {min_increase_year}')

#run the main
main()

