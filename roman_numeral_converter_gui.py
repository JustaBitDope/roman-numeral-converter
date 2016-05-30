import roman_numeral_converter
from tkinter import *
from tkinter.ttk import *

class NumeralConverterGUI(object):
    
    def __init__(self, parent):
        self.parent = parent
        
        #Framework
        self.title_frame = Frame(self.parent)#, borderwidth=10)
        self.entry_frame = Frame(self.parent, borderwidth=10)
        self.bottomframe_L = Frame(self.parent)
        
        self.title_frame.grid(row=0, column=0, padx=10, pady=10)
        self.entry_frame.grid(row=1, column=0, padx=10, pady=0)
        self.bottomframe_L.grid(row=2, column=0)
        
        #Title Labels
        self.title = Label(self.title_frame, text="Roman Numeral Converter", font=("Trebuchet MS", "11"), justify=CENTER)
        self.title.pack()
                
        #Entries
        self.entry_1 = Entry(self.entry_frame, justify=CENTER, width=20, font=('times', '16', 'bold'))
        self.entry_1.pack(pady=10)
        
        #Buttons
        self.button_1 = Button(self.entry_frame, text="Convert", command=self.button_click())
        self.button_1.pack()
        
        #Output Variables
        self.thing = "hello"
        left_output = StringVar()
        left_output.set("yolt")
        ##right_output.set("yolo")
        
        #Output Labels
        label = Label(self.bottomframe_L, text=self.thing)
        label.pack()
        
    def button_click(self):
        print("Button clicked!")
        #self.thing = self.thing + "o"



window = Tk()
window.title("Roman Numeral Converter")
NumeralConverterGUI(window)
window.mainloop()