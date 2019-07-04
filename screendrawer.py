import win32gui
import win32api

dc = win32gui.GetDC(0)
red = win32api.RGB(255, 0, 0)
win32gui.SetPixel(dc, 0, 0, red)


for x in range(1,2150):
	for y in range(-20,20):
		v = x+y
		if v<0:
			v=0
		win32gui.SetPixel(dc, v, x, red)
	
