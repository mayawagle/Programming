#This program will calculate the total price of an item
#after the sales tax of the state and county

#Get the subtotal before tax
subtotal = float(input('What is the purchase before tax?: '))

#compute the state sales tax
state_tax = .04 * subtotal

#Compute the county sales tax
county_tax = .02 * subtotal

#compute the total purchase
total_purchase = subtotal + state_tax + county_tax

#print the results
print(f'The purchase before tax is ${subtotal} ')
print(f'The state sales tax amounts to ${state_tax}')
print(f'The county sales tax amounts to ${county_tax}')
print(f'The total sale after tax is ${total_purchase} ')







