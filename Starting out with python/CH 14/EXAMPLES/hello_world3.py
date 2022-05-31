#this program uses the side = 'left' argument with 
#the pack method to change the layout of the widgets

import tkinter

class MyGui:
    def __init__(self):
        #create a main window widget
        self.main_window = tkinter.Tk()

        #create two label widgets
        self.label1 = tkinter.Label(self.main_window, \
                                    text = 'Hello World!')
        self.label2 = tkinter.Label(self.main_window, \
                            text = 'This is my GUI program.')
        
        ##call both the label widgets' pack method
        self.label1.pack(side ='left')
        self.label2.pack(side ='left')

        #Enter the tkinter main loop
        tkinter.mainloop()

#create an instance of the MyGui class
my_gui = MyGui()