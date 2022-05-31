#Ask user to enter total square feet
total_square_feet = int(input('What is the total square feet?: '))

#divide by feet in acre
acres = total_square_feet/ 43560

#print("You have", acres, 'acres')
print(f"You have {format(acres,'.3f')} acres")
