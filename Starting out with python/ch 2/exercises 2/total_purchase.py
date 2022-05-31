#get the price of the items
item_1 = float(input('What is the price of the first item?: '))
item_2 = float(input('What is the price of the second item?: '))
item_3 = float(input('What is the price of the third item?: '))
item_4 = float(input('What is the price of the fourth item?: '))
item_5 = float(input('What is the price of the fifth item?: '))

#calculate then print the subtotal
subtotal = item_1 + item_2 + item_3 + item_4 + item_5
print (f'Your subtotal is {subtotal}')

#calculate the sales tax
sales_tax = .06 * subtotal
print(f"your sales tax is: { format (sales_tax, '.2f') }")

#calculate and print the total price
total_price = subtotal + sales_tax
# print(f'Your total is ${total_price}' )
print(f"Your total is ${format( total_price, '.2f')}" )