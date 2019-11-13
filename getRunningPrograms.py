import psutil
import tkinter

tk = tkinter.Tk()

def prepareWindow():
	tk.overrideredirect(True)
	text = tkinter.StringVar()
	label = tkinter.Label(tk,textvariable=text,font=("Helvetica",20))
	label.pack()
	tk.attributes('-topmost', True)
	tk.update()
	screen_width = tk.winfo_screenwidth()
	screen_height = tk.winfo_screenheight()
	tk.geometry("+"+str(screen_width-300)+"+"+str(screen_height-100))
	tk.withdraw()
	return text

def getProcesses():
	processes = []
	for process in psutil.process_iter():
		processes.append(process.name())
	return processes

def detectRunningHook(text):
	tk.after(5000,lambda: detectRunning(text))

def detectRunning(text):
	if 'Calculator.exe' in getProcesses():
		tk.deiconify()
		text.set("Detected Calculator")
	else:
		tk.withdraw()
	tk.after(5000,lambda: detectRunning(text))



textfield = prepareWindow()
detectRunningHook(textfield)
tk.mainloop()



