#This program will caluclate the total amount of a meal purchased at a restaurant

#Ask for the subtotal of the meal
subtotal = float(input('What is the subtotal of the meal?: '))

# calculate and print the tip
tip = .15 * subtotal
print(f'a 15% tip will cost ${tip}')

#caluclate and print the sales tax
sales_tax = .07 * subtotal
print(f'a sales tax of 7% will cost ${sales_tax}')

#Calculate and print the total
total = subtotal + tip + sales_tax
print(f'Your total is ${total}')