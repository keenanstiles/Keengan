from tkinter import *
from functools import partial


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

    def to_help(self):
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):
        background = "#ffe6cc"
        self.help_box = Toplevel()

        partner.to_help_button.config(state=DISABLED)

        # yadda yadda more stuf to make help button active again if no
        # window present
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help,partner))

        self.help_frame = Frame(self.help_box, width=300, height=200,
                                bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background,
                                        text="help / info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature " \
                    "you wish to convert and then choose to convert " \
                    "to either degrees celsius or " \
                    "fahrenheit.. \n\n" \
                    "Note that -237 degrees C " \
                    "(-459 F) is absolute zero (the coldest possible " \
                    "temperature), try no convert less then this and youll get an error message \n\n " \
                    "go to the history tab to download recent calculations into a text file"
        self.help_text_label = Label(self.help_frame, bg=background,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="dismiss", bg="#CC6600",
                                     fg="#ffffff",
                                     command=partial(self.close_help,
                                                     partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes help dialouge
    def close_help(self, partner):
        # put help button back to normal
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Temperture Convertor")
    Converter()
    root.mainloop()

