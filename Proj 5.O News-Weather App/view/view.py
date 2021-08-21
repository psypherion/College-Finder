# -----------Importing Libraries --------------- #

import tkinter
from tkinter.constants import *
from tkinter.ttk import *
from tkinter import StringVar, IntVar


class View(tkinter.Toplevel):
    def __init__(self, controller):
        super().__init__()
        
        self.geometry("400x400")
        
        self.controller = controller
        self.bind('<Return>', self.controller.handle_button_search)
        
        #---------Variables ----------#
        self.var_search = StringVar()
        self.var_temp = StringVar()
        self.var_location = StringVar()
        self.var_conditions = StringVar()
        self.var_feels_like = StringVar()
        self.var_wind_speed = StringVar()
        self.var_wind_direction = StringVar()
        self.var_unit = IntVar()
        
        self.mainframe = Frame(self)
        self.mainframe.pack()
        self.search_bar()
        self.info()
        self.details()
        self.controls()
        
        
    def search_bar(self):
        self.frame_search_bar = Frame(self.mainframe)
        self.location_search = Entry(self.frame_search_bar, textvariable = self.var_search)
        self.button_search = Button(self.frame_search_bar, text="Search", command=self.controller.handle_button_search)
        
        self.location_search.pack(side=LEFT)
        self.button_search.pack(padx=4)
        self.frame_search_bar.pack()
        
    def info(self):
        self.frame_info = Frame(self.mainframe)
        self.label_temp = Label(self.frame_info, textvariable = self.var_temp)
        self.label_location = Label(self.frame_info, textvariable = self.var_location)
        
        self.label_temp.pack(pady = 5)
        self.label_location.pack()
        self.frame_info.pack()
        
        
    def details(self):
        self.frame_details = Frame(self.mainframe)
        label_condition_left = Label(self.frame_details, text="Current Condition : ")
        label_feels_like_left = Label(self.frame_details, text = "Feels Like : ")
        label_wind_speed_left = Label(self.frame_details, text = "Wind Speed : ")
        label_wind_direction_left = Label(self.frame_details, text = "Wind Direction : ")
        
        label_condition_right = Label(self.frame_details, textvariable = self.var_conditions)
        label_feels_like_right = Label(self.frame_details, textvariable=self.var_feels_like)
        label_wind_speed_right = Label(self.frame_details, textvariable=self.var_wind_speed)
        label_wind_direction_right = Label(self.frame_details, textvariable=self.var_wind_direction)
        
        label_condition_left.grid(row=0, column=0, pady=5, sticky=W)
        label_condition_right.grid(row=0, column=1, pady=5, sticky=E)
        
        label_feels_like_left.grid(row=1, column=0, pady=5, sticky=W)
        label_feels_like_right.grid(row=1, column=1, pady=5, sticky=E)
        
        label_wind_direction_left.grid(row=2, column=0, pady=5, sticky=W)
        label_wind_direction_right.grid(row=2, column=1, pady=5, sticky=E)
        
        label_wind_speed_left.grid(row=3, column=0, pady=5, sticky=W)
        label_wind_speed_right.grid(row=3, column=1, pady=5, sticky=E)
        
        
        self.frame_details.pack()
        
        
    def controls(self):
        self.frame_control = Frame(self.mainframe)
        radio_fahren = Radiobutton(self.frame_control, text="Farhenheit", variable= self.var_unit, value=1, command = self.controller.update_gui)
        radio_celsius = Radiobutton(self.frame_control, text="Celsius", variable=self.var_unit, value=2, command = self.controller.update_gui)
        
        radio_fahren.pack(side=LEFT, padx=8, pady=5)
        radio_celsius.pack(side=RIGHT, padx=8, pady=5)
        
        radio_celsius.invoke()
        
        self.frame_control.pack()
        
    def main(self):
        self.mainloop()
        
    
    
    
