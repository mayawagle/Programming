#This program translates a number between 1-10 into a roman numeral
#Constants for translation
ROMAN_ONE = 'I'
ROMAN_TWO = 'II'
ROMAN_THREE = 'III'
ROMAN_FOUR = 'IV' 
ROMAN_FIVE = 'V'
ROMAN_SIX = 'VI'
ROMAN_SEVEN = 'VII'
ROMAN_EIGHT = 'VIII'
ROMAN_NINE = 'IX'
ROMAN_TEN = 'X'


#define the main
def main():
    #get the number from the user
    number = int(input('Enter a number 1-10: '))
    #write if statements
    if number == 1:
        print(ROMAN_ONE)
    else:
        if number == 2:
         print(ROMAN_TWO)
        else:
            if number == 3:
                print(ROMAN_THREE)
            else:
                if number == 4:
                    print(ROMAN_FOUR)
                else:
                    if number == 5:
                        print(ROMAN_FIVE)
                    else:
                        if number == 6:
                            print(ROMAN_SIX)
                        else:
                            if number == 7:
                                print(ROMAN_SEVEN)
                            else:
                                if number == 8:
                                    print(ROMAN_EIGHT)
                                else:
                                    if number == 9:
                                        print(ROMAN_NINE)
                                    else:
                                        if number == 10:
                                            print(ROMAN_TEN)
                                        else:
                                            if number < 1 or number > 10:
                                                print('This number is not in the range' )

#Call the main
main()