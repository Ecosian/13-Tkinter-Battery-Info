from tkinter import *
from tkinter import ttk
import psutil
import threading
import os
from tkinter import messagebox

window = Tk()
window.title("Battery Info")
window.geometry("240x90+555+0")
window.resizable(0,0)
window.iconbitmap('battery.ico')
ticking=False
threadRunning=True

def getBatteryInfo():
    global percentBar
    global plugStateVar
    global chargePercentVar
    global threadRunning
    
    if(threadRunning):
        t = threading.Timer(1.0, lambda:getBatteryInfo())
        t.start()
        battery = psutil.sensors_battery()
        plugged= battery.power_plugged
        percent = battery.percent
        
        if plugged==True:
            plugStateVar.set("Charging")
        else:
            plugStateVar.set("Not Charging")
        
        percentBar["value"]=percent
        chargePercentVar.set(percent)
            
def on_closing():
    global window
    global threadRunning
    if messagebox.askokcancel("Response", "Are You Sure You Want To Quit?"):
        threadRunning=False
        window.destroy()

plugStateVar=StringVar()
plugStateVar.set("")
chargePercentVar = StringVar()
chargePercentVar.set(0)
titleLabel= Label(window,text="Status")
titleLabel.pack()

percentBar = ttk.Progressbar(window,length=200, orient="horizontal", mode="determinate")
percentBar.pack()
percentBar["maximum"]=100
percentBar["value"]=0

plugStateLabel=Label(window, textvariable=plugStateVar)
plugStateLabel.pack()

chargePercentLabel = Label(window,textvariable=chargePercentVar)
chargePercentLabel.pack()

getBatteryInfo()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
