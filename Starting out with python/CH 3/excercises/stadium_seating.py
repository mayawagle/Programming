#This program calculates the income generated from ticket sales
def main():
    price_per_classA = 15
    price_per_classB = 12
    price_per_classC = 9
    tickets_sold_A = int(input('How many class A tickets were sold?: '))
    tickets_sold_B = int(input('How many class B tickets were sold?: '))
    tickets_sold_C = int(input('How many class C tickets were sold?: '))
    income_generated = (price_per_classA * tickets_sold_A) + (price_per_classB * tickets_sold_B) + (price_per_classC * tickets_sold_C)
    print(f'The income generated from ticket sales is ${income_generated}')

main()