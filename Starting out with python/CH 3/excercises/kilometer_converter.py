#This program converts kilometers to miles
#Ask for the kilometers
kilometers = float(input('Enter a distance in kilometers: '))

#Convert the distance to miles
miles = kilometers * 0.6214

#print miles
print(f"Your distance is {format(miles,'.2f')}")