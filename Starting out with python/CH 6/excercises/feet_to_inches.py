#This program converts a number of feet to inches

#define the main
def main():
    #get the number of feet
    feet = float(input('Enter the number of feet: '))

    #print the result using the feet_to_inches function
    print(f'{feet} feet is {feet_to_inches(feet)} inches.')

#define feet_to_inches
def feet_to_inches(feet):
    return feet * 12

#call the main
main()