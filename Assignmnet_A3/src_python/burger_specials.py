#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Feb 09, 2024 08:48:26 PM EST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import burger_specials_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class frmBurgers:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("800x590+1304+354")
        top.minsize(120, 1)
        top.maxsize(3632, 3581)
        top.resizable(1,  1)
        top.title("Burger Specials")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top

        self.Canvas1 = tk.Canvas(self.top)
        self.Canvas1.place(relx=0.55, rely=0.102, relheight=0.424
                , relwidth=0.325)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="#000000")
        self.Canvas1.configure(insertbackground="#000000")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#d9d9d9")
        self.Canvas1.configure(selectforeground="black")

        self.lblHeading = tk.Label(self.top)
        self.lblHeading.place(relx=0.275, rely=0.017, height=33, width=352)
        self.lblHeading.configure(activebackground="#d9d9d9")
        self.lblHeading.configure(activeforeground="black")
        self.lblHeading.configure(background="#d9d9d9")
        self.lblHeading.configure(compound='left')
        self.lblHeading.configure(cursor="fleur")
        self.lblHeading.configure(disabledforeground="#a3a3a3")
        self.lblHeading.configure(font="-family {Tahoma} -size 16 -weight bold")
        self.lblHeading.configure(foreground="#000000")
        self.lblHeading.configure(highlightbackground="#d9d9d9")
        self.lblHeading.configure(highlightcolor="#000000")
        self.lblHeading.configure(text='''Farm Burger Specials''')

        self.picPrime = tk.Canvas(self.top)
        self.picPrime.place(relx=0.1, rely=0.102, relheight=0.424
                , relwidth=0.325)
        self.picPrime.configure(background="#d9d9d9")
        self.picPrime.configure(borderwidth="2")
        self.picPrime.configure(highlightbackground="#d9d9d9")
        self.picPrime.configure(highlightcolor="#000000")
        self.picPrime.configure(insertbackground="#000000")
        self.picPrime.configure(relief="ridge")
        self.picPrime.configure(selectbackground="#d9d9d9")
        self.picPrime.configure(selectforeground="black")

        self.btnVeggie = tk.Button(self.top)
        self.btnVeggie.place(relx=0.663, rely=0.576, height=35, width=128)
        self.btnVeggie.configure(activebackground="#d9d9d9")
        self.btnVeggie.configure(activeforeground="black")
        self.btnVeggie.configure(background="#d9d9d9")
        self.btnVeggie.configure(disabledforeground="#a3a3a3")
        self.btnVeggie.configure(foreground="#000000")
        self.btnVeggie.configure(highlightbackground="#d9d9d9")
        self.btnVeggie.configure(highlightcolor="#000000")
        self.btnVeggie.configure(text='''Veggie''')

        self.btnExit = tk.Button(self.top)
        self.btnExit.place(relx=0.425, rely=0.898, height=35, width=128)
        self.btnExit.configure(activebackground="#d9d9d9")
        self.btnExit.configure(activeforeground="black")
        self.btnExit.configure(background="#d9d9d9")
        self.btnExit.configure(disabledforeground="#a3a3a3")
        self.btnExit.configure(foreground="#000000")
        self.btnExit.configure(highlightbackground="#d9d9d9")
        self.btnExit.configure(highlightcolor="#000000")
        self.btnExit.configure(text='''Exit Window''')

        self.btnSelectMeal = tk.Button(self.top)
        self.btnSelectMeal.place(relx=0.42, rely=0.576, height=35, width=128)
        self.btnSelectMeal.configure(activebackground="#d9d9d9")
        self.btnSelectMeal.configure(activeforeground="black")
        self.btnSelectMeal.configure(background="#d9d9d9")
        self.btnSelectMeal.configure(disabledforeground="#a3a3a3")
        self.btnSelectMeal.configure(foreground="#000000")
        self.btnSelectMeal.configure(highlightbackground="#d9d9d9")
        self.btnSelectMeal.configure(highlightcolor="#000000")
        self.btnSelectMeal.configure(text='''Select Meal''')

        self.lblInstructions = tk.Label(self.top)
        self.lblInstructions.place(relx=0.275, rely=0.673, height=19, width=360)
        self.lblInstructions.configure(activebackground="#d9d9d9")
        self.lblInstructions.configure(activeforeground="black")
        self.lblInstructions.configure(background="#d9d9d9")
        self.lblInstructions.configure(compound='center')
        self.lblInstructions.configure(disabledforeground="#a3a3a3")
        self.lblInstructions.configure(font="-family {Tahoma} -size 9")
        self.lblInstructions.configure(foreground="#000000")
        self.lblInstructions.configure(highlightbackground="#d9d9d9")
        self.lblInstructions.configure(highlightcolor="#000000")
        self.lblInstructions.configure(text='''Choose a burger and then click the Select Meal button''')

        self.btnPrime = tk.Button(self.top)
        self.btnPrime.place(relx=0.163, rely=0.576, height=35, width=128)
        self.btnPrime.configure(activebackground="#d9d9d9")
        self.btnPrime.configure(activeforeground="black")
        self.btnPrime.configure(background="#d9d9d9")
        self.btnPrime.configure(disabledforeground="#a3a3a3")
        self.btnPrime.configure(foreground="#000000")
        self.btnPrime.configure(highlightbackground="#d9d9d9")
        self.btnPrime.configure(highlightcolor="#000000")
        self.btnPrime.configure(text='''Prime Beef''')

        self.lblConfirmation = tk.Label(self.top)
        self.lblConfirmation.place(relx=0.393, rely=0.714, height=19, width=172)
        self.lblConfirmation.configure(activebackground="#d9d9d9")
        self.lblConfirmation.configure(activeforeground="black")
        self.lblConfirmation.configure(background="#d9d9d9")
        self.lblConfirmation.configure(compound='left')
        self.lblConfirmation.configure(disabledforeground="#a3a3a3")
        self.lblConfirmation.configure(font="-family {Tahoma} -size 9")
        self.lblConfirmation.configure(foreground="#000000")
        self.lblConfirmation.configure(highlightbackground="#d9d9d9")
        self.lblConfirmation.configure(highlightcolor="#000000")
        self.lblConfirmation.configure(text='''Enjoy your burger special''')

def start_up():
    burger_specials_support.main()

if __name__ == '__main__':
    burger_specials_support.main()




