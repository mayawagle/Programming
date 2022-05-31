#This program tells the user hom many points they
#are awarded based on how many books they buy

#define the constants
one_book_points = 5
two_book_points = 15
three_book_points = 30
four_or_more_book_points = 60

#define the main
def main():
    #get the amount of books bought
    books_bought = int(input('Enter the amount of books bought: '))

    #write the if statements
    if books_bought <= 0:
        print('You have recieved 0 points.')
    else:
        if books_bought == 1:
            print(f'You have recieved {one_book_points} points.')
        else:
            if books_bought == 2:
                print(f'You have recieved {two_book_points} points')
            else:
                if books_bought == 3:
                    print(f'You have recieved {three_book_points} points')
                else:
                    if books_bought >= 4:
                        print(f'You have recieved {four_or_more_book_points} points')

            
#call the main
main()
