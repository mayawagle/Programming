#This program tells the user the total price of the boxes they want with
#the discount if there is one

#define the constants
TEN_TO_19 = .20
TWENTY_TO_49 = .30
FIFTY_TO_99 = .40
HUNDRED_OR_MORE = .50

#define the main
def main():
    #get the number of boxes
    boxes = int(input('How many boxes would you like to purchase?: '))
    undiscounted_total = 99 * boxes
    #determine the discount
    if boxes < 10:
        print(f'There is no discount. Your total is {format(undiscounted_total)}')
    else:
        if boxes >= 10 and boxes<= 19:
            discount = TEN_TO_19 * undiscounted_total
            total =undiscounted_total - discount
            print(f'The discount is ${format(discount,".2f")}')
            print(f'The total amount after the discount is ${format(total,".2f")} ')
        else:
            if boxes >= 20 and boxes<= 49:
                discount = TWENTY_TO_49 * undiscounted_total
                total =undiscounted_total - discount
                print(f'The discount is ${format(discount,".2f")}')
                print(f'The total amount after the discount is ${format(total,".2f")} ')
            else:
                if boxes >= 50 and boxes<= 99:
                    discount = FIFTY_TO_99 * undiscounted_total
                    total =undiscounted_total - discount
                    print(f'The discount is ${format(discount,".2f")}')
                    print(f'The total amount after the discount is ${format(total,".2f")} ')
                else:
                    if boxes >= 100:
                        discount = HUNDRED_OR_MORE * undiscounted_total
                        total =undiscounted_total - discount
                        print(f'The discount is ${format(discount,".2f")}')
                        print(f'The total amount after the discount is ${format(total,".2f")} ')


#call the main
main()