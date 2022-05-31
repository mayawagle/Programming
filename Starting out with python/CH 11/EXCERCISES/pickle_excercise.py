#April 14, 2022
#excercise for myself (not from book)

#This program writes a dictionary of names and
#pickles it to a binary file. It then prints the 
#content in binary before translating it
#back to a readable dictionary

#import pickle
import pickle

#define the main
def main():
    people = {'maya':18, 'billy':2, 'michael':100}
    #write the dictionary
    # for count in range(3):
    #     name = input('Enter name: ')
    #     age = input('Enter the age: ')
    #     print()

    #     people[name] = age
    #     # people['name'] = name
    #     # people['age'] = age

    #pickle the dictionary
    output_file = open('people.data', 'wb')
    pickle.dump(people,output_file)
    output_file.close()
    #Print the list in binary
    infile = open('people.data', 'rb')
    line = infile.readline()
    for l in line:
        print(line)
    
    # while line != '':
    #     line = infile.readline()
    #     print(line)
    #Print the unpickled list
    infile = open('people.data', 'rb')
    pb = pickle.load(infile)
    print(pb)

    output_file.close()
#run the main
main()
