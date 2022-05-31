my_variable_number = 1234
# str = "hey this is just my string." + my_variable_number # this breaks the code, we can only add strings to strings. my_variable_number is an int not a string.
#str = "hey this is just my string. " + str(my_variable_number) + " this was my number."
str = f"hey this is just my string. {my_variable_number} this was my number." # this is string interpolation. google "python string interpolate example"
print(str)
print(str)
print(str)
