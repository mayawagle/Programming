#This program demonstrates two functions that have
#local variables with the same name

def main():
    #call the texas function
    texas()
    #call the CA function
    california()

#Definition of the texas function. It creates a 
#local variable named birds
def texas():
    birds = 5000
    print(f'Texas has {birds} birds.')

def california():
    birds = 8000
    print(f'California has {birds} birds.')

#Call the main function
main()
