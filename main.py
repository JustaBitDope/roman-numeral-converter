import logic
import tkinter as tk
import tkinter.ttk as ttk

class NumeralConverterGUI(object):
    
    number_to_numeral = True;
    
    def __init__(self, parent):
        self.parent = parent
        self.parent.minsize(350, 200)
        self.parent.title("Roman Numeral Converter")
        self.parent.iconbitmap("ancient-theatre.ico")
        
        # Mainframe
        self.main_frame = tk.Frame(self.parent, 
                                   bg="#ff0fff")
        self.main_frame.pack(fill="both", expand=1)
        
        # TITLE
        self.title_frame = tk.Frame(self.main_frame, 
                                    bg="#993388", 
                                    borderwidth=5)
        self.title = tk.Label(self.title_frame, 
                              text="Roman Numeral Converter", 
                              #font=("Raleway", "16"), 
                              justify="center", 
                              bg="#993388")
        self.title_frame.pack(fill="x", padx=10, pady=10)
        self.title.pack()
        
        # TEXTBOX / BUTTON
        self.input_var = tk.StringVar()
        self.entry_frame = tk.Frame(self.main_frame, 
                                    bg="#ffffff",
                                    borderwidth=10 
                                    )
        self.entry_1 = ttk.Entry(self.entry_frame, 
                                 justify="center", 
                                 width=20, 
                                 #font=('Raleway', '16'),
                                 textvariable=self.input_var)
        self.button_1 = ttk.Button(self.entry_frame, 
                                   text="Convert", 
                                   command=self.button_click, 
                                   default="normal")
        self.entry_frame.pack(fill="y", expand=1, padx=10, pady=0)
        self.entry_1.pack(pady=10)
        self.button_1.pack()
        
        # OUTPUT
        self.output_var = tk.StringVar()
        self.output_frame = tk.Frame(self.main_frame, 
                                     bg="#ffffff", 
                                     borderwidth=5)
        self.label = ttk.Label(self.output_frame, 
                               #font=('Raleway', '16'),
                               textvariable=self.output_var)
        self.output_frame.pack(fill="y", expand=1)
        self.label.pack()
                
    def button_click(self):
        print("Button clicked!")
        print(" : "+self.input_var.get())
        
        text_in = self.input_var.get()
        text_out = ""
        
        if logic.check_number_input(text_in):
            text_out = logic.number_to_numeral(int(text_in))
        
        self.input_var.set("")
        self.output_var.set(text_out)


if __name__ == "__main__":
    window = tk.Tk()
    NumeralConverterGUI(window)
    window.mainloop()