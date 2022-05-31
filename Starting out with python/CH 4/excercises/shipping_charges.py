#this program gets the weight of the package then displays
#the shipping charges

#define the constants
TWO_POUNDS_OR_LESS = 1.10
BETWEEN_TWO_AND_SIX = 2.20
BETWEEN_SIX_AND_TEN = 3.70
OVER_TEN = 3.80

#define the main
def main():
    #find the weight of the packet
    weight = float(input('What is the weight of the package?: '))

    #find the rate per pound
    if weight <= 2:
        rate_per_pound = TWO_POUNDS_OR_LESS
    else:
        if weight > 2 and weight < 6:
            rate_per_pound = BETWEEN_TWO_AND_SIX
        else:
            if weight > 6 and weight < 10:
                rate_per_pound = BETWEEN_SIX_AND_TEN
            else:
                if weight > 10:
                    rate_per_pound = OVER_TEN

    #calculate the shipping charges
    shipping_charge = weight * rate_per_pound
    print(f'The total shipping charge is ${format(shipping_charge, ".2f")}')

#call the main
main()


