#This program calcualtes and displays a person's BMI
def main():
    weight = float(input("What is your weight in pounds?: "))
    height = float(input("What is your height in inches?: "))
    BMI = weight * 703 / height**2
    print(f'Your BMI is {format(BMI,".2f")}')

#Call the main
main()