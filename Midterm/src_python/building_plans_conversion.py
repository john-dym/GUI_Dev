#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Mar 08, 2024 04:29:36 PM EST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import gui_tools

_location = os.path.dirname(__file__)

import building_plans_conversion_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40'
_default_win_size = "800x600"

class frmBuildingPlansConversion:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        app_size_pos = gui_tools.windows_geometry(top, _default_win_size)

        top.geometry(app_size_pos)
        # top.geometry(gui_tools.windows_geometry_pos(_default_win_size))
        top.minsize(120, 1)
        top.maxsize(2052, 1261)
        top.resizable(1,  1)
        top.title("Building Plans Conversion")
        top.configure(background="#c0c0ff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.ValueInput = tk.StringVar()
        self.selectedButton = tk.IntVar()

        self.btnExit = tk.Button(self.top)
        self.btnExit.place(relx=0.694, rely=0.817, height=56, width=177)
        self.btnExit.configure(activebackground="#d9d9d9")
        self.btnExit.configure(activeforeground="black")
        self.btnExit.configure(background="#c0c0ff")
        self.btnExit.configure(disabledforeground="#a3a3a3")
        self.btnExit.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.btnExit.configure(foreground="#000000")
        self.btnExit.configure(highlightbackground="#d9d9d9")
        self.btnExit.configure(highlightcolor="#000000")
        self.btnExit.configure(relief="ridge")
        self.btnExit.configure(text='''Exit''')

        self.btnClear = tk.Button(self.top)
        self.btnClear.place(relx=0.39, rely=0.817, height=56, width=177)
        self.btnClear.configure(activebackground="#d9d9d9")
        self.btnClear.configure(activeforeground="black")
        self.btnClear.configure(background="#c0c0ff")
        self.btnClear.configure(disabledforeground="#a3a3a3")
        self.btnClear.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.btnClear.configure(foreground="#000000")
        self.btnClear.configure(highlightbackground="#d9d9d9")
        self.btnClear.configure(highlightcolor="#000000")
        self.btnClear.configure(relief="ridge")
        self.btnClear.configure(text='''Clear''')

        self.btnConvert = tk.Button(self.top)
        self.btnConvert.place(relx=0.083, rely=0.817, height=56, width=177)
        self.btnConvert.configure(activebackground="#d9d9d9")
        self.btnConvert.configure(activeforeground="black")
        self.btnConvert.configure(background="#c0c0ff")
        self.btnConvert.configure(disabledforeground="#a3a3a3")
        self.btnConvert.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.btnConvert.configure(foreground="#000000")
        self.btnConvert.configure(highlightbackground="#d9d9d9")
        self.btnConvert.configure(highlightcolor="#000000")
        self.btnConvert.configure(relief="ridge")
        self.btnConvert.configure(text='''Convert''')

        self.lblFrameSelection = tk.LabelFrame(self.top)
        self.lblFrameSelection.place(relx=0.525, rely=0.45, relheight=0.275
                , relwidth=0.425)
        self.lblFrameSelection.configure(relief='groove')
        self.lblFrameSelection.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.lblFrameSelection.configure(foreground="#ffffff")
        self.lblFrameSelection.configure(text='''Convert Measurement''')
        self.lblFrameSelection.configure(background="#4b0083")
        self.lblFrameSelection.configure(highlightbackground="#d9d9d9")
        self.lblFrameSelection.configure(highlightcolor="#000000")

        self.Radiobutton1 = tk.Radiobutton(self.lblFrameSelection)
        self.Radiobutton1.place(relx=0.029, rely=0.303, relheight=0.212
                , relwidth=0.759, bordermode='ignore')
        self.Radiobutton1.configure(activebackground="#d9d9d9")
        self.Radiobutton1.configure(activeforeground="black")
        self.Radiobutton1.configure(anchor='w')
        self.Radiobutton1.configure(background="#4b0083")
        self.Radiobutton1.configure(compound='left')
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font="-family {Segoe UI} -size 18")
        self.Radiobutton1.configure(foreground="#ffffff")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="#000000")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''Inches to Meters''')
        self.Radiobutton1.configure(variable=self.selectedButton)

        self.Radiobutton2 = tk.Radiobutton(self.lblFrameSelection)
        self.Radiobutton2.place(relx=0.029, rely=0.606, relheight=0.212
                , relwidth=0.759, bordermode='ignore')
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(activeforeground="black")
        self.Radiobutton2.configure(anchor='w')
        self.Radiobutton2.configure(background="#4b0083")
        self.Radiobutton2.configure(compound='left')
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font="-family {Segoe UI} -size 18")
        self.Radiobutton2.configure(foreground="#ffffff")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="#000000")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''Meters to Inches''')
        self.Radiobutton2.configure(variable=self.selectedButton)

        self.HeaderFrame = tk.Frame(self.top)
        self.HeaderFrame.place(relx=0.0, rely=0.05, relheight=0.342
                , relwidth=1.0)
        self.HeaderFrame.configure(relief='flat')
        self.HeaderFrame.configure(borderwidth="2")
        self.HeaderFrame.configure(background="#c0c0ff")
        self.HeaderFrame.configure(highlightbackground="#d9d9d9")
        self.HeaderFrame.configure(highlightcolor="#000000")

        self.lblTitle = tk.Label(self.HeaderFrame)
        self.lblTitle.place(relx=0.375, rely=0.049, height=61, width=424)
        self.lblTitle.configure(activebackground="#d9d9d9")
        self.lblTitle.configure(activeforeground="black")
        self.lblTitle.configure(anchor='w')
        self.lblTitle.configure(background="#c0c0ff")
        self.lblTitle.configure(compound='left')
        self.lblTitle.configure(disabledforeground="#a3a3a3")
        self.lblTitle.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.lblTitle.configure(foreground="#000000")
        self.lblTitle.configure(highlightbackground="#d9d9d9")
        self.lblTitle.configure(highlightcolor="#000000")
        self.lblTitle.configure(text='''Converter App''')

        self.lblInstructions = tk.Label(self.HeaderFrame)
        self.lblInstructions.place(relx=0.4, rely=0.39, height=91, width=236)
        self.lblInstructions.configure(activebackground="#d9d9d9")
        self.lblInstructions.configure(activeforeground="black")
        self.lblInstructions.configure(anchor='nw')
        self.lblInstructions.configure(background="#c0c0ff")
        self.lblInstructions.configure(compound='left')
        self.lblInstructions.configure(disabledforeground="#a3a3a3")
        self.lblInstructions.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.lblInstructions.configure(foreground="#000000")
        self.lblInstructions.configure(highlightbackground="#d9d9d9")
        self.lblInstructions.configure(highlightcolor="#000000")
        self.lblInstructions.configure(text='''Enter a value and choose conversion''')

        self.Entry1 = tk.Entry(self.HeaderFrame)
        self.Entry1.place(relx=0.775, rely=0.537, height=50, relwidth=0.168)
        self.Entry1.configure(background="#4b0083")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 20 -weight bold")
        self.Entry1.configure(foreground="#ffffff")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="#000000")
        self.Entry1.configure(insertbackground="#000000")
        self.Entry1.configure(selectbackground="#d9d9d9")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=self.ValueInput)

        self.lblPic = tk.Label(self.HeaderFrame)
        self.lblPic.place(relx=0.0, rely=0.0, height=205, width=264)
        self.lblPic.configure(activebackground="#d9d9d9")
        self.lblPic.configure(activeforeground="black")
        self.lblPic.configure(background="#d9d9d9")
        self.lblPic.configure(compound='left')
        self.lblPic.configure(disabledforeground="#a3a3a3")
        self.lblPic.configure(font="-family {Segoe UI} -size 9")
        self.lblPic.configure(foreground="#000000")
        self.lblPic.configure(highlightbackground="#d9d9d9")
        self.lblPic.configure(highlightcolor="#000000")
        self.lblPic.configure(text='''building.jpg''')

def start_up():
    building_plans_conversion_support.main()

if __name__ == '__main__':
    building_plans_conversion_support.main()




