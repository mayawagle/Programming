#This program gives information regarding Joe's purchase of stock

#Store the given information
shares_purchased = 1000
dollars_per_share = 32.87
commission = 0.02
shares_sold = 1000
dollars_per_share_sold = 33.92

#The amount of money joe paid for the stock
paid_for_stock = shares_purchased * dollars_per_share
print(f'Joe paid ${paid_for_stock} for his shares')
#The amount of commission Joe paid his broker when he bought the stock
commision_for_stock = commission * paid_for_stock
print(f'Joe paid a commission of ${commision_for_stock}')
#The amount Joe sold the stock for
amount_sold_for = shares_sold * dollars_per_share_sold
print(f'Joe sold his stock for ${amount_sold_for},')
#The amount of commission Joe paid his broker when he sold the stock
commission_paid_2 = commission * amount_sold_for
#Display the amount of money that Joe had left when he sold the stock and paid his broker (both times). If this amount is positice, then Joe made a profit. If the amount is negative, then Joe lost money.
money_left = amount_sold_for - commission_paid_2
print(f'Joe has ${money_left} left')