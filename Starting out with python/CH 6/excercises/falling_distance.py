#this function tells the user the distance an object has fallen in
#intervals of 1 second

#define the constants
SECONDS = 10

#define the main
def main():
    #format a table
    print('seconds\tdistance(m)')
    print('---------------------------')

    #write the for loop
    for num in range (1,SECONDS):
        print(f'{num}\t{format(falling_distance(num), ".2f")}')

#define the falling_distance funciton
def falling_distance(falling_time):
    distance = 0.5 * 9.8 * (falling_time ** 2)
    return distance

#call the main
main()