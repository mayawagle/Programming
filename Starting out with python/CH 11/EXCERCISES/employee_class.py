#March 23
#Chapter 11 pg 479

#This program creates an employee class that holds the
#following attributes: name, id num, dept and job title. It then creates 3
#instances of the class

class Employee:
    def __init__(self, name,ID_num,dept,job):
        self.__name = name
        self.__ID_num = ID_num
        self.__dept = dept
        self.__job = job

    #define the getters
    def get_name(self):
        return self.__name

    def get_IDnum(self):
        return self.__ID_num
        
    def get_dept(self):
        return self.__dept

    def get_job(self):
        return self.__job
    
    #define the setters
    def set_name(self, name):
        self.__name = name
    
    def set_IDnum(self, ID_num):
        self.__ID_num = ID_num
    
    def set_dept(self, dept):
        self.__dept = dept
    
    def set_job(self, job):
        self.__job = job

    def __str__(self):
        return f"""Name: {self.__name}
ID: {self.__ID_num}
Department: {self.__dept}
Title: {self.__job}\n"""




#define the main
if __name__ == "__main__":
    employee1 = Employee('Susan Meyers',47899,'Accounting','VP')
    employee2 = Employee('Mark Jones',39119,'IT', 'Programmer')
    employee3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'engineer')

    print('Employee 1 info:')
    print(employee1.get_name())
    print(employee1.get_IDnum())
    print(employee1.get_dept())
    print(employee1.get_job())
    print()

    print('Employee 2 info:')
    print(employee2.get_name())
    print(employee2.get_IDnum())
    print(employee2.get_dept())
    print(employee2.get_job())
    print()

    print('Employee 3 info:')
    print(employee3.get_name())
    print(employee3.get_IDnum())
    print(employee3.get_dept())
    print(employee3.get_job())
    print()

    print(employee1)

