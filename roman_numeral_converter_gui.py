import roman_numeral_converter
import tkinter as tk
import tkinter.ttk as ttk

class NumeralConverterGUI(object):
    
    def __init__(self, parent):
        self.parent = parent
        self.parent.minsize(300, 200)
        
        #Framework
        self.title_frame = tk.Frame(self.parent, bg="red", borderwidth=5)
        self.entry_frame = tk.Frame(self.parent, borderwidth=10, bg="green")
        self.output_frame = tk.Frame(self.parent, bg="red", borderwidth=5)
        
        self.title_frame.grid(row=0, column=0, padx=10, pady=10)
        self.entry_frame.grid(row=1, column=0, padx=10, pady=0)
        self.output_frame.grid(row=2, column=0)
        
        #String Variables
        self.entry_var = tk.StringVar()
        self.entry_var.set("welp this is cool")
        self.output = tk.StringVar()
        self.output.set("yolt")        
        
        #Title Labels
        self.title = ttk.Label(self.title_frame, text="Roman Numeral Converter", font=("Trebuchet MS", "11"), justify="center")
        self.title.pack()
        
        #Entries
        self.entry_1 = ttk.Entry(self.entry_frame, justify="center", 
                             width=20, font=('times', '16', 'bold'),
                             textvariable=self.entry_var)
        self.entry_1.pack(pady=10)
        
        #Buttons
        self.button_1 = ttk.Button(self.entry_frame, text="Convert", command=self.button_click)
        self.button_1.pack()
        
        #Output Labels
        self.label = ttk.Label(self.output_frame, textvariable=self.entry_var)
        self.label.pack()
        
    def button_click(self):
        print("Button clicked!")
        print(" : "+self.entry_var.get())
        self.entry_var.set("")
        self.output.set(self.output.get() + "o")



window = tk.Tk()
window.title("Roman Numeral Converter")
window.iconbitmap("ancient-theatre.ico")
NumeralConverterGUI(window)
window.mainloop()