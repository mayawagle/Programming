#This program tells the user a secondary color that is made
#mixing the two primary colors they give

#define the main
def main():
    #get the two colors
    primary_one = str(input('Enter a primary color: '))
    primary_two = str(input('Enter another primary color: '))

    #write if statements
    if (primary_one == 'red' and primary_two == 'blue') or (primary_one == 'blue' and primary_two == 'red'):
        print('purple') 
    elif (primary_one == 'red' and primary_two == 'yellow') or (primary_one == 'yellow' and primary_two == 'red'):
        print('orange') 
    elif (primary_one == 'yellow' and primary_two == 'blue') or (primary_one == 'blue' and primary_two == 'yellow'):
        print('green') 
    elif primary_one == primary_two:
        print('The colors are the same so they do not make a secondary color')
    else:
        print('The colors entered are not primary colors')

#run the main
main()