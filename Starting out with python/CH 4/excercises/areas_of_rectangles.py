#This program asks the user for the measurements of two rectangles
#It then tells the user which rectangle has a greater area
#or if the rectangles have the same area

#Define the main
def main():
    #ask for the measurements
    length_1 = float(input('What is the length of the first rectangle?: '))
    width_1 = float(input('What is the width of the first rectangle?: '))
    length_2 = float(input('What is the length of the second rectangle?: '))
    width_2 = float(input('What is the width of the second rectangle?: '))
    
    #find the areas of the rectangles
    area_1 = length_1 * width_1
    area_2 = length_2 * width_2

    #Find and print the results
    if area_1 > area_2:
        print('The first rectangle has a greater area.')
    elif area_1 < area_2:
        print('The second rectangle has a greater area.')
    else:
        print('The rectangles have the same area.')

#Call the main
main()
