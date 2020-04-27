from tkinter import *
from tkinter import ttk
from tkinter importfont
import time
import datetime

def quit(*args):
    root.destroy()


    def clock_time():

        time = datetime.datetime.new()
        time = (time.strftime("%H:%M:%S"))

        txt.set(time)

        root.after(1000, clock_time)