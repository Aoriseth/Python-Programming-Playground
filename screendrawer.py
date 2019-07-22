import win32gui
import win32api
import ctypes
from math import ceil

dc = win32gui.GetDC(0)
red = win32api.RGB(255, 0, 0)

def getScreenWidthAndHeight():
	user32 = ctypes.windll.user32
	user32.SetProcessDPIAware()
	xs = win32api.GetSystemMetrics(0)-1
	ys = win32api.GetSystemMetrics(1)-1
	return xs,ys



def drawScreenDiagonal(maxWidth,maxHeight):
	ratio = maxHeight/maxWidth
	y=-1
	for x in range(0,maxWidth):
			y+=ratio
			if y>maxHeight:
				y=maxHeight
			print("drawing: x="+str(ceil(x))+" y="+str(ceil(y)))
			win32gui.SetPixel(dc, ceil(x), ceil(y), red)


def drawPolygon(maxWidth,maxHeight):
	win32gui.Rectangle(dc,100,100,maxWidth-100,maxHeight-100)

	
xs,ys = getScreenWidthAndHeight()
# drawPolygon(xs, ys)
drawScreenDiagonal(xs, ys)