#This program displays a triangle -like shape of hashtags

#Define the constants
NUM_STEPS = 6

#write the loop
for col in range(NUM_STEPS):
    print('#', end = "")
    for row in range(col + 1):
        print('',end = ' ')
    print('#')
  
