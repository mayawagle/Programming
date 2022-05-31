def main():
    #calculate calories from fat
    fat_grams = float(input('How many fat grams do you consume a day?'))
    calories_from_fat = fat_grams * 9
    print(f'You recieve {calories_from_fat} calories a day from fat')
    #Caluclate calories from carbs
    carb_grams = float(input('How many carb grams do you consume a day?'))
    calories_from_carbs = carb_grams * 9
    print(f'You recieve {calories_from_carbs} calories a day from carbs')

#call the main
main()