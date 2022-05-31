#This code calculates the user's miles per gallon

#ask for the miles driven
miles_driven = float(input('How many miles were driven?: '))
#ask how many gallons were used
gallons_used = float(input('How many gallons were used?: '))
#calculate and print the mpg
mpg = miles_driven / gallons_used
print((f'your car uses {mpg} miles per gallon'))