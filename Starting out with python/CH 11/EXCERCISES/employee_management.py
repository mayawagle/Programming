#April 13
#Chapter 11 pg 480

#This program stores employee objects in a dictionary 
#using the employee class from excercise 4. It then presents a 
#menu that lets the user preform actions

from employee_class import Employee

#Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#copy the main function from the birthdays example
def main():
    #create an empty dictionary
    employees = {}

    #Initialize a variable for the user's choice
    choice = 0

    while choice != QUIT:
        #get the user's menu choice
        choice = get_menu_choice()

        #process the choice
        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice == DELETE:
            delete(employees)

#The get_menu_choice function displays the menu 
#and gets a validated choice from the user
def get_menu_choice():
    print()
    print('Employee Information')
    print('---------------------')
    print('1. Look up an employee')
    print('2. Add a new employee')
    print('3. Change employee information')
    print('4. Delete an employee')
    print('5. Quit the program')
    print()

    #get the user's choice
    choice = int(input('Enter your choice: '))

    #validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))
    #return the user's choice
    return choice

#The look_up function looks up an employee in the employee dictionary

def look_up(employees):
    #get a name to look up 
    number = int(input("Enter an employee's number: "))

    #Look it up in the dictionary
    print(employees.get(number, 'Not found.'))

#The add function adds a new employee into the 
#employee dictionary
def add(employees):
  #Get the employee's information
  name = input("Enter the employee's name: ")
  ID_num = int(input("Enter the employee's ID_num: "))
  dept = input("Enter the employee's dept: ")
  job = input("Enter the employee's job: ")

  #create an employee object
  employee = Employee(name,ID_num,dept,job) 
  #If the name does not exist, add it.
  if ID_num not in employees:
     employees[ID_num] = employee
  else:
     print('That employee already exists in the dictionary.')

#The change function changes an existing
#entry in the employees dictionary
def change(employees):
    #get an employee # to look up
    number = int(input("Enter the employee's number: "))
    if number in employees:
        #Get the new information
        name = input("Enter the employee's name: ")
        dept = input("Enter the employee's dept: ")
        job = input("Enter the employee's job: ")

        
        employees[number] = Employee(name,number,dept,job)
    else:
        print('That number is not found.')

#The delete funciton deletes an employee from the employee
#dictionary
def delete(employees):
    #get a employee #to look up
    number = int(input("Enter the employee's number: "))

    #if the number is found, delete the entry
    if number in employees:
        del employees[number]
    else:
        print('That name is not found.')



#call the main 
main()



# for debugging
# employee1 = Employee('Susan Meyers',47899,'Accounting','VP')
# employee2 = Employee('Mark Jones',39119,'IT', 'Programmer')
# employee3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'engineer')

# employees={}
# employees[employee1.get_IDnum()] = employee1
# employees[employee2.get_IDnum()] = employee2
# employees[employee3.get_IDnum()] = employee3


# for e in employees:
#     print(e)
#     print(employees[e])

