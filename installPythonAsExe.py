from tkinter import Tk,messagebox
from tkinter.filedialog import askopenfilename
import os
from pathlib import Path
import shutil

def isPythonFile(path):
	return path.as_posix().endswith("py")

def convertToExe(path):
	# command = "pyinstaller "+path.as_posix()+" --noconsole --onefile --distpath "+path.parent.as_posix()
	command = "pyinstaller "+path.as_posix()+" --noconsole --distpath "+path.parent.as_posix()
	os.system(command)
	os.remove(path.stem+".spec")
	shutil.rmtree(path.parent.joinpath("build"))

def install():
	filename = Path(askopenfilename())
	if isPythonFile(filename):
		convertToExe(filename)
	else:
		messagebox.showinfo("Error", "Not a python file!")
	

Tk().withdraw()
install()

