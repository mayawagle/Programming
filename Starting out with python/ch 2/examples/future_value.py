#Get the desired future value
future_value = float(input('Enter the desired future value: '))

#Get the annual interest rate
rate = float(input('Enter the annual intetrest rate: '))

#Get the number of yearts that the money will appreciate
years = int(input('enter the number of years the money will grow: '))

#Calculate the amount needed to deposit
present_value = future_value / (1.0 + rate) ** years

#display the amount needed to deposit
print('You will need to deposit the amount: ', present_value)