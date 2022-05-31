#this program calculates the averag eof the values 
#in a list

def main():
    #create a list
    scores = [2.5,8.3,6.5,4,5.2]

    #create a variable to use as an accumulator
    total = 0

    #caculate the total of the list elements
    for value in scores:
        total += value
    
    #calculate the average of the elements
    average = total / len(scores)
    
    #display the total of the list elements
    print(f'The average of the elements is {average}')

#call the main
main()