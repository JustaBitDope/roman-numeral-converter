import roman_numeral_converter
from tkinter import *
from tkinter.ttk import *

class NumeralConverterGUI(object):
    
    def __init__(self, parent):
        
        self.parent = parent
        
        #Framework
        self.title_frame = Frame(self.parent, relief=GROOVE, borderwidth=10)
        self.entry_frame = Frame(self.parent, borderwidth=10)
        ##self.subframe_R = Frame(self.parent, borderwidth=10)
        self.bottomframe_L = Frame(self.parent)
        ##self.bottomframe_R = Frame(self.parent)
        
        self.title_frame.grid(row=0, column=0, padx=10, pady=10)
        self.entry_frame.grid(row=1, column=0, padx=10, pady=0)
        ##self.subframe_R.grid(row=1, column=1, padx=10, pady=10)
        self.bottomframe_L.grid(row=2, column=0)
        ##self.bottomframe_R.grid(row=2, column=1)
        
        #Title Labels
        self.title = Label(self.title_frame, text="            Roman Numeral Converter            ", font="Cambria 20 bold", justify=CENTER)
        #self.label_1 = Label(self.entry_frame, text="Number to Numeral", font="Calibri 10 underline")
        ##self.label_2 = Label(self.subframe_R, text="Numeral to Number", font="Calibri 10 underline")
        self.title.pack()
        #self.label_1.pack()
        ##self.label_2.pack()
                
        #Entries
        self.entry_1 = Entry(self.entry_frame, justify=CENTER, width=50, font=('times', '20', 'bold'))
        ##self.entry_2 = Entry(self.subframe_R, justify=CENTER)
        self.entry_1.pack(pady=10)
        ##self.entry_2.pack()
        
        #Buttons
        self.button_1 = Button(self.entry_frame, text="Convert")
        ##self.button_2 = Button(self.subframe_R, text="Convert")
        self.button_1.pack()
        ##self.button_2.pack()
        
        #Output Variables
        left_output = StringVar()
        ##right_output = StringVar()
        left_output.set("yolt")
        ##right_output.set("yolo")
        
        #Output Labels
        label_L = Label(self.bottomframe_L, text="noooooooooope")
        ##label_R = Label(self.bottomframe_R, textvariable=right_output)
        label_L.pack()
        ##label_R.pack()



window = Tk()
NumeralConverterGUI(window)
window.mainloop()