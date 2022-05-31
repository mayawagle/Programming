#This program converts the speeds 60 KPH
#Throught 130 KPH (in 10 KPH increments) to MPH

#Global constants
START = 60
END = 131
INCREMENT = 10
CONVERSION_FACTOR = 0.6214

def main():
    #print the table headings
    print('KPH\tMPH')
    print('--------------')

    #print the speeds
    for kph in range(START, END, INCREMENT):
        mph = kph * CONVERSION_FACTOR
        print(kph, '\t', format(mph, '.1f'))

#call the main
main()