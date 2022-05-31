#this program displays two labels with text

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
        self.label1.pack()
        self.label2.pack()

        #Enter the tkinter main loop
        tkinter.mainloop()

#create an instance of the MyGui class
my_gui = MyGui()