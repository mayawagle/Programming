#April 12, 2022
#Program 10-4 page 408-409

#This program demonstrates object pickling
import pickle

#main function
def main():
    again = 'y' #to control loop repitition

    #open a file for binary writing
    output_file = open('info.dat', 'wb')

    #get data until the user wants to stop
    while again.lower() == 'y':
        #Get the data about a person and save it
        save_data(output_file)

        #Does the user want to enter more data?
        again = input('Enter more data?: (y/n): ')
    
    #close the file
    output_file.close()

#The save_data function gets data about a person, 
#stores it in a dictionary, and then pickles the 
#dictionary to the specified file
def save_data(file):
    #create an empty dictionary
    person = {}

    #Get data for a person an store
    #it in the dictionary
    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))

    #Pickle the dictionary
    pickle.dump(person, file)

#Call the main function
main()
    