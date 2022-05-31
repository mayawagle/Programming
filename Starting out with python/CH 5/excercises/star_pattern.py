#This program displays an upside down pyramid of stars

#define the constants
BASE_LENGTH = 7

for row in range(BASE_LENGTH):
    for col in range(BASE_LENGTH - row):
        print('*', end = ' ')
    print()