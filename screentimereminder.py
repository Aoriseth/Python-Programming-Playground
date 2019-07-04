import ctypes
from time import sleep
from threading import Thread


def showScreenTimeReminder():
	ctypes.windll.user32.MessageBoxW(0,"Test","Screen-Time-Reminder",0)


if __name__ == '__main__':
	Thread(target=showScreenTimeReminder).start()
	while True:
		sleep(1800)
		Thread(target=func).start()



