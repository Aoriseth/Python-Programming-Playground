from datetime import datetime, timedelta
import tkinter as tk
import sys

top = tk.Tk()
top.geometry("80x40+300+300")
top.resizable(0, 0)
top.overrideredirect(1)
entry = tk.Entry(top, justify='center')
entry.configure(font=("Times New Roman", 20, "bold"))
entry.pack()


def readTime():
	time = input("Current Time: ")
	return time

def parseTime(time):
	if len(time)>2:
		return datetime.strptime(time, '%H%M')
	elif len(time)==1:
		return datetime.strptime(time+"0", '%H%M')

def close(event):
    sys.exit() 

def calcOnEnter(event):
	time = entry.get()
	parsedTime = parseTime(time)+timedelta(hours=8,minutes=30)
	entry.delete(0, "end")
	entry.insert(0, parsedTime.strftime("%H:%M"))

top.bind('<Escape>', close)
top.bind('<Return>',calcOnEnter)

entry.focus_set()
top.mainloop()
