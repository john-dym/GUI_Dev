#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Feb 26, 2024 08:29:43 PM EST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import payroll_calculator2_support

_bgcolor = '#ffffff'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("800x575+861+312")
        top.minsize(120, 1)
        top.maxsize(2756, 2033)
        top.resizable(1,  1)
        top.title("Payroll Every Two Weeks")
        top.configure(background=_bgcolor)
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.lblFICAOut = tk.StringVar()
        self.lblFederalTaxOut = tk.StringVar()
        self.lblNetIncomeOut = tk.StringVar()
        self.lblStateTaxOut = tk.StringVar()
        self.GrossPayInput = tk.StringVar()

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.452, relheight=0.565, relwidth=1.006)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#000000")

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.447, rely=0.338, height=36, width=130)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#0290fe")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="#000000")
        self.Button2.configure(text='''Clear''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.671, rely=0.585, height=31, width=94)
        self.Label4.configure(activebackground="#d9d9d9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="#000000")
        self.Label4.configure(text='''State Tax:''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.385, rely=0.585, height=31, width=94)
        self.Label3.configure(activebackground="#d9d9d9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="#000000")
        self.Label3.configure(text='''Federal Tax:''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.186, rely=0.338, height=36, width=130)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#0290fe")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''Compute Taxes''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.211, rely=0.738, height=41, width=234)
        self.Label5.configure(activebackground="#d9d9d9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="#000000")
        self.Label5.configure(text='''Net Paycheck Income:''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.199, rely=0.585, height=31, width=45)
        self.Label2.configure(activebackground="#d9d9d9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="#000000")
        self.Label2.configure(text='''FICA:''')

        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.286, rely=0.585, height=31, width=65)
        self.Label7.configure(activebackground="#d9d9d9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="#000000")
        self.Label7.configure(text='''Label''')
        self.Label7.configure(textvariable=self.lblFICAOut)
        self.lblFICAOut.set('''Label''')

        self.Label8 = tk.Label(self.Frame1)
        self.Label8.place(relx=0.534, rely=0.585, height=31, width=84)
        self.Label8.configure(activebackground="#d9d9d9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="#000000")
        self.Label8.configure(text='''Label''')
        self.Label8.configure(textvariable=self.lblFederalTaxOut)
        self.lblFederalTaxOut.set('''Label''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.547, rely=0.738, height=41, width=174)
        self.Label6.configure(activebackground="#d9d9d9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="#000000")
        self.Label6.configure(text='''Label''')
        self.Label6.configure(textvariable=self.lblNetIncomeOut)
        self.lblNetIncomeOut.set('''Label''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.236, rely=0.123, height=41, width=232)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''Enter Gross Pay:''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.683, rely=0.338, height=36, width=130)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(background="#0290fe")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button3.configure(foreground="#ffffff")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="#000000")
        self.Button3.configure(text='''Exit''')

        self.Label9 = tk.Label(self.Frame1)
        self.Label9.place(relx=0.795, rely=0.585, height=31, width=94)
        self.Label9.configure(activebackground="#d9d9d9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(compound='left')
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="#000000")
        self.Label9.configure(text='''Label''')
        self.Label9.configure(textvariable=self.lblStateTaxOut)
        self.lblStateTaxOut.set('''Label''')

        self.EntryGrossPay = tk.Entry(self.Frame1)
        self.EntryGrossPay.place(relx=0.534, rely=0.123, height=40
                , relwidth=0.216)
        self.EntryGrossPay.configure(background="white")
        self.EntryGrossPay.configure(disabledforeground="#a3a3a3")
        self.EntryGrossPay.configure(font="-family {Arial} -size 14")
        self.EntryGrossPay.configure(foreground="#000000")
        self.EntryGrossPay.configure(highlightbackground="#d9d9d9")
        self.EntryGrossPay.configure(highlightcolor="#000000")
        self.EntryGrossPay.configure(insertbackground="#000000")
        self.EntryGrossPay.configure(selectbackground="#d9d9d9")
        self.EntryGrossPay.configure(selectforeground="black")
        self.EntryGrossPay.configure(textvariable=self.GrossPayInput)

        self.HeaderFrame = tk.Frame(self.top)
        self.HeaderFrame.place(relx=0.0, rely=-0.017, relheight=0.478
                , relwidth=1.006)
        self.HeaderFrame.configure(relief='flat')
        self.HeaderFrame.configure(borderwidth="2")
        self.HeaderFrame.configure(background="#d9d9d9")
        self.HeaderFrame.configure(highlightbackground="#d9d9d9")
        self.HeaderFrame.configure(highlightcolor="#000000")

        self.Canvas1 = tk.Canvas(self.HeaderFrame)
        self.Canvas1.place(relx=-0.012, rely=-0.036, relheight=1.065
                , relwidth=0.513)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="#000000")
        self.Canvas1.configure(insertbackground="#000000")
        self.Canvas1.configure(selectbackground="#d9d9d9")
        self.Canvas1.configure(selectforeground="black")

        self.ProgramTitle = tk.Label(self.HeaderFrame)
        self.ProgramTitle.place(relx=0.509, rely=0.109, height=51, width=393)
        self.ProgramTitle.configure(activebackground="#d9d9d9")
        self.ProgramTitle.configure(activeforeground="black")
        self.ProgramTitle.configure(background="#d9d9d9")
        self.ProgramTitle.configure(compound='left')
        self.ProgramTitle.configure(disabledforeground="#a3a3a3")
        self.ProgramTitle.configure(font="-family {Cooper Black} -size 24 -weight bold")
        self.ProgramTitle.configure(foreground="#000000")
        self.ProgramTitle.configure(highlightbackground="#d9d9d9")
        self.ProgramTitle.configure(highlightcolor="#000000")
        self.ProgramTitle.configure(text='''Payroll Calculator''')

        self.ProgramDescription = tk.Label(self.HeaderFrame)
        self.ProgramDescription.place(relx=0.509, rely=0.4, height=61, width=393)

        self.ProgramDescription.configure(activebackground="#d9d9d9")
        self.ProgramDescription.configure(activeforeground="black")
        self.ProgramDescription.configure(background="#d9d9d9")
        self.ProgramDescription.configure(compound='left')
        self.ProgramDescription.configure(disabledforeground="#a3a3a3")
        self.ProgramDescription.configure(font="-family {Cooper Black} -size 18 -weight bold")
        self.ProgramDescription.configure(foreground="#000000")
        self.ProgramDescription.configure(highlightbackground="#d9d9d9")
        self.ProgramDescription.configure(highlightcolor="#000000")
        self.ProgramDescription.configure(text='''Paycheck Calculation''')

def start_up():
    payroll_calculator2_support.main()

if __name__ == '__main__':
    payroll_calculator2_support.main()




