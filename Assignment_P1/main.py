# Assignment P1
# John Morales
# Tkinter Reference: https://docs.python.org/3/library/tkinter.html
# Tkdocs first example: https://tkzdocs.com/tutorial/firstexample.html

from tkinter import *
from tkinter import ttk
from functools import partial

def Reveal_French_Number(dict, dict_key, label_output):
    label_output.config(text=dict[dict_key], background='lightgreen')

#Constants
TITLE = "French Numbers"
MAIN_TEXT = "Do you know the French words for the numbers 1 through 5?"
INSTRUCTIONS = "Click the buttons below to see them."
FRENCH_NUMBERS = {1:"un",
                  2:"deux",
                  3:"trois",
                  4:"quatre",
                  5:"cinq"}

#Main window setup
root = Tk()
root.title(TITLE)
root.configure()

frm = ttk.Frame(root, padding=20)
frm.grid()

#Used to center all other widgets
column_span = len(FRENCH_NUMBERS)

#First Line
ttk.Label(frm, text=MAIN_TEXT).grid(column=0, row=0, columnspan=column_span)

#Second Line
ttk.Label(frm, text=INSTRUCTIONS).grid(column=0, row=1, columnspan=column_span)

#Forth Line
french_number_label = ttk.Label(frm, text="")
french_number_label.grid(row=3, columnspan=column_span)

#Create buttons based on how big the dictionary
x = 0
for dict_key in FRENCH_NUMBERS:
    # partial function used to pass arguments for each button: https://stackoverflow.com/a/22290388
    ttk.Button(frm, text=dict_key, command=partial(Reveal_French_Number, FRENCH_NUMBERS, dict_key, french_number_label)).grid(column=x, row=2)
    x += 1

#Fifth line Exit Button
ttk.Button(frm, text="Exit", command=root.quit).grid(row=4, columnspan=column_span)

root.mainloop()