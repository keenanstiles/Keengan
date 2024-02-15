from tkinter import *


class Converter:

    def __init__(self):
        # common format for all buttons
        # arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#ffffff"

        # gui frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid(row=0)

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg=button_fg,
                                     font=button_font, width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

    @staticmethod
    def to_help():
        DisplayHelp()


class DisplayHelp:

    def __init__(self):
        background = "#ffe6cc"

        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300, height=200,
                                bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background,
                                        text="help / inffo",
                                        font=(Arial, "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature " \
                "you wish to convert and then choose to convert " \
                "to either degrees celsius or " \
                "fahrenheit.. \n\n" \
        "Note that -237 degrees C " \
        ""


if __name__ == "__main__":
    root = Tk()
    root.title("Temperture Convertor")
    Converter()
    root.mainloop()








