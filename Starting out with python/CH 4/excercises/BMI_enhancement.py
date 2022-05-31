#copy the original BMI program


#This program calcualtes and displays a person's BMI
def main():
    weight = float(input("What is your weight in pounds?: "))
    height = float(input("What is your height in inches?: "))
    BMI = weight * 703 / height**2
    print(f'Your BMI is {format(BMI,".2f")}')

    #find if the person is over,under or at optimal weight
    if BMI < 18.5:
        print('The person is underweight.') 
    else:
        if BMI >= 18.5 and BMI <= 25:
            print('The person is at optimal weight.')
        else:
            if BMI > 25:
                print('The person is overweight.')     

#Call the main
main()
  