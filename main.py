from tkinter import *

class Converter:


    def __init__(self):

        # Set up GUI Frame
        self.temp_frame = Frame()
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Convertor",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and" \
                       "then press one of the buttons to convert" \
                       "it from centigrade to Fahrenheit."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wrap=250, width=45,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )

        self.temp_entry.grid(row=2, padx=10, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperture Convertor")
    Converter()
    root.mainloop()
