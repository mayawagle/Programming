#This program calculate property tax

#define globals
PROPERTY_TAX = .64
#Define the main function
def main():
    real_value = float(input('What is the actual value of the property?:'))
    property_assessment = .60 * real_value
    print(f'the actual value of the property is ${format(real_value,".2f")}')
    print(f'The assessment value is ${format(property_assessment,".2f")} ')
    #call the property tax func
    calculate_property_tax(property_assessment)

#define property_tax func
def calculate_property_tax(property_assessment):
   property_tax = property_assessment / 100 * .64
   print(f'The property tax is ${format(property_tax,".2f")}')

#call the main
main()