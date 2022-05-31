#March 28, 2022
#Asteroid game

#This program creates a class for a point object
#It then returns the x and y coordinate seperately and as a tuple

#define the class
class PointObject:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    #write the get methods
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
        
    def get_point(self):
        point = (self.__x,self.__y)
        return point
    

    def new_point(self,x,y):
        new_point = PointObject(x,y)
        
       

#def the main to test
def main():
    ex_point = PointObject(3,5)

    print(ex_point.get_x())
    print(ex_point.get_y())
    print(ex_point.get_point())


#run the main
main()
