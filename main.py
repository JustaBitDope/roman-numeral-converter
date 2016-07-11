import logic
import tkinter as tk
import tkinter.ttk as ttk




class NumeralConverterGUI(object):
    
    def __init__(self, root):
        self.root = root
        self.number_to_numeral = True;
        
        # Window Settings
        root.minsize(350, 200)
        root.title("Roman Numeral Converter")
        root.iconbitmap("ancient-theatre.ico")
        root.bind('<Return>', self.convert)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        # Mainframe
        self.main = tk.Frame(self.root, bg="")
        self.main.columnconfigure(0, weight=0)
        self.main.columnconfigure(1, weight=1)
        self.main.columnconfigure(2, weight=0)

        self.main.rowconfigure(0, weight=0)
        self.main.rowconfigure(1, weight=1)
        self.main.rowconfigure(2, weight=2)
        self.main.grid(sticky="nsew")
        
        # TITLE
        self.t_var = tk.StringVar()
        self.t_var.set("Number to Numeral")
        self.t_frame = tk.Frame(self.main, bg="", borderwidth=5)
        self.t_frame.rowconfigure(0, weight=1)
        self.t_frame.columnconfigure(0, weight=1)
        self.t_frame.grid(row=0, column=1, sticky="nsew")
        self.title = ttk.Label(self.t_frame, textvariable=self.t_var, background="")
        self.title.grid()
        
        # SWITCH BUTTON
        self.photo = tk.PhotoImage(file="sort(32).png")
        self.switch = tk.Button(self.main, image=self.photo, width=2, height=1, command=self.switch)
        self.switch.grid(row=0, column=2)
        
        # rollover text?
        
        # TEXTBOX / BUTTON
        self.input_var = tk.StringVar()
        
        self.e_frame = tk.Frame(self.main, bg="", borderwidth=10)
        self.e_frame.columnconfigure(0, weight=1)
        self.e_frame.rowconfigure(0, weight=0)
        self.e_frame.rowconfigure(1, weight=0)
        self.e_frame.grid(row=1, column=1, sticky="ew", padx=10, pady=0)
        self.entry = ttk.Entry(self.e_frame, justify="center", width=20, textvariable=self.input_var)
        self.entry.grid()
        self.button = ttk.Button(self.e_frame, text="Convert", command=self.convert)
        self.button.grid(row=1)
        
        # OUTPUT
        self.o_var = tk.StringVar()
        self.o_frame = tk.Frame(self.main, bg="pink", borderwidth=5)
        self.o_frame.columnconfigure(0, weight=1)
        self.o_frame.rowconfigure(0, weight=1)
        self.o_frame.grid(row=2, column=1, sticky="nsew")
        self.output = ttk.Label(self.o_frame, textvariable=self.o_var, background="red")
        self.output.grid()
                
    def convert(self, event=None):
        print(" : "+self.input_var.get())
        
        text_in = self.input_var.get()
        text_out = ""
        
        if self.number_to_numeral:
            if logic.check_number_input(text_in):
                text_out = logic.number_to_numeral(int(text_in))
            else:
                text_out = "Invalid"
                
        else:
            if logic.check_numeral_input(text_in):
                text_out = logic.numeral_to_number(text_in)
            else:
                text_out = "Invalid"
        
        self.input_var.set("")
        self.o_var.set(text_out)
    
    def switch(self):
        if self.number_to_numeral:
            self.number_to_numeral = False
            self.t_var.set("Numeral to Number")
        else:
            self.number_to_numeral = True
            self.t_var.set("Number to Numeral")




if __name__ == "__main__":
    window = tk.Tk()
    NumeralConverterGUI(window)
    window.mainloop()