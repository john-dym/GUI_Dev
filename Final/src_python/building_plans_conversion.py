#Final - Building Plans Conversion
#Author: John Morales - https://github.com/john-dym
#Class: GUI Development

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
_default_win_size = "800x800"
_building_image_path = "images/building.png"

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
        self.SelectedButton = tk.IntVar(value=1)

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
        self.btnExit.configure(command=quit)

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
        self.btnClear.configure(command=self.b_clear)

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
        self.btnConvert.configure(command=self.b_convert)

        self.lblFrameSelection = tk.LabelFrame(self.top)
        self.lblFrameSelection.place(relx=0.525, rely=0.4, relheight=0.175, relwidth = 0.425)
        self.lblFrameSelection.configure(relief='groove')
        self.lblFrameSelection.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.lblFrameSelection.configure(foreground="#ffffff")
        self.lblFrameSelection.configure(text='''Convert Measurement''')
        self.lblFrameSelection.configure(background="#4b0083")
        self.lblFrameSelection.configure(highlightbackground="#d9d9d9")
        self.lblFrameSelection.configure(highlightcolor="#000000")

        self.RdButtonInToMeters = tk.Radiobutton(self.lblFrameSelection)
        self.RdButtonInToMeters.place(relx=0.029, rely=0.303, relheight=0.212
                                      , relwidth=0.759, bordermode='ignore')
        self.RdButtonInToMeters.configure(activebackground="#d9d9d9")
        self.RdButtonInToMeters.configure(activeforeground="black")
        self.RdButtonInToMeters.configure(anchor='w')
        self.RdButtonInToMeters.configure(background="#4b0083")
        self.RdButtonInToMeters.configure(compound='left')
        self.RdButtonInToMeters.configure(disabledforeground="#a3a3a3")
        self.RdButtonInToMeters.configure(font="-family {Segoe UI} -size 18")
        self.RdButtonInToMeters.configure(foreground="#ffffff")
        self.RdButtonInToMeters.configure(highlightbackground="#d9d9d9")
        self.RdButtonInToMeters.configure(highlightcolor="#000000")
        self.RdButtonInToMeters.configure(justify='left')
        self.RdButtonInToMeters.configure(text='''Inches to Meters''')
        self.RdButtonInToMeters.configure(variable=self.SelectedButton)
        self.RdButtonInToMeters.configure(value=1)
        self.RdButtonInToMeters.configure(selectcolor='black')

        self.RdButtonMetersToInch = tk.Radiobutton(self.lblFrameSelection)
        self.RdButtonMetersToInch.place(relx=0.029, rely=0.606, relheight=0.212
                                        , relwidth=0.759, bordermode='ignore')
        self.RdButtonMetersToInch.configure(activebackground="#d9d9d9")
        self.RdButtonMetersToInch.configure(activeforeground="black")
        self.RdButtonMetersToInch.configure(anchor='w')
        self.RdButtonMetersToInch.configure(background="#4b0083")
        self.RdButtonMetersToInch.configure(compound='left')
        self.RdButtonMetersToInch.configure(disabledforeground="#a3a3a3")
        self.RdButtonMetersToInch.configure(font="-family {Segoe UI} -size 18")
        self.RdButtonMetersToInch.configure(foreground="#ffffff")
        self.RdButtonMetersToInch.configure(highlightbackground="#d9d9d9")
        self.RdButtonMetersToInch.configure(highlightcolor="#000000")
        self.RdButtonMetersToInch.configure(justify='left')
        self.RdButtonMetersToInch.configure(text='''Meters to Inches''')
        self.RdButtonMetersToInch.configure(variable=self.SelectedButton)
        self.RdButtonMetersToInch.configure(value=2)
        self.RdButtonMetersToInch.configure(selectcolor="black")

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
        self.lblTitle.configure(text='''Converter App 2''')

        self.lblInstructions = tk.Label(self.HeaderFrame)
        self.lblInstructions.place(relx=0.4, rely=0.45, height=91, width=246)
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
        self.lblInstructions.configure(text='''Enter a value and \nchoose conversion''')

        self.lblOutput = tk.Label(self.top)
        self.lblOutput.place(relx=0.05, rely=0.683, height=61, width=714)
        self.lblOutput.configure(activebackground="#d9d9d9")
        self.lblOutput.configure(activeforeground="black")
        self.lblOutput.configure(anchor='e')
        self.lblOutput.configure(background="#c0c0ff")
        self.lblOutput.configure(compound='left')
        self.lblOutput.configure(disabledforeground="#a3a3a3")
        self.lblOutput.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.lblOutput.configure(foreground="#000000")
        self.lblOutput.configure(highlightbackground="#d9d9d9")
        self.lblOutput.configure(highlightcolor="#000000")
        self.lblOutput.configure(text='''''')

        self.EntryValue = tk.Entry(self.HeaderFrame)
        self.EntryValue.place(relx=0.775, rely=0.537, height=50, relwidth=0.168)
        self.EntryValue.configure(background="#4b0083")
        self.EntryValue.configure(disabledforeground="#a3a3a3")
        self.EntryValue.configure(font="-family {Courier New} -size 20 -weight bold")
        self.EntryValue.configure(foreground="#ffffff")
        self.EntryValue.configure(highlightbackground="#d9d9d9")
        self.EntryValue.configure(highlightcolor="#000000")
        self.EntryValue.configure(insertbackground="#000000")
        self.EntryValue.configure(selectbackground="#d9d9d9")
        self.EntryValue.configure(selectforeground="black")
        self.EntryValue.configure(textvariable=self.ValueInput)
        self.EntryValue.configure(justify="center")
        self.EntryValue.bind("<Return>", lambda e: self.b_convert())

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
        gui_tools.image_to_label(_building_image_path, self.lblPic, (264,205))

    def b_clear(self):
        #Clears input and output
        self.ValueInput.set("")
        self.SelectedButton.set(1)
        self.lblOutput.configure(text="")

    def b_convert(self):
        value = self.validate_input()

        if value:
            self.calculate_and_output(value)

    def validate_input(self):
        input = self.ValueInput.get()
        input_match = gui_tools.validate_float_input(input)

        if input_match:
            #input is a float
            float_value = float(self.ValueInput.get())

            if float_value >= 0:
                return float_value
            else:
                self.negative_number_error()
                return None
        else:
            self.invalid_number_input_error()
            return None

    def convert_input(self):
        if gui_tools.validate_float_input(self.ValueInput.get()):
            return float(self.ValueInput.get())

    def calculate_and_output(self, float_value):
        entry_value = self.EntryValue.get()
        display = ""
        converted_value = 0.0
        if self.SelectedButton.get() == 1:  #Inches to Meters
            converted_value = self.inch_to_meter(float_value)
            display = f"{entry_value} inches is {converted_value:.3f} meters."
        elif self.SelectedButton.get() == 2: #Meters to inches
            converted_value = self.meter_to_inch(float_value)
            display = f"{entry_value} meters is {converted_value:.3f} inches."

        self.lblOutput.configure(text=display)

    def invalid_number_input_error(self):
        title = "Invalid input Error"
        message = "Please enter a valid number."
        gui_tools.error_message(title, message)
        self.b_clear()

    def negative_number_error(self):
        title = "Negative Number Error"
        message = "Please enter a positive number."
        gui_tools.error_message(title, message)
        self.b_clear()

    def inch_to_meter(self, inch_value):
        return inch_value * 0.0254

    def meter_to_inch(self, meter_value):
        return meter_value * 39.3701

def start_up():
    building_plans_conversion_support.main()

if __name__ == '__main__':
    building_plans_conversion_support.main()



