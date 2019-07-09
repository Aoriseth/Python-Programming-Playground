from datetime import datetime


def getTime():
	today = datetime.today()
	formatted = today.strftime("%d %B")
	return formatted

print(getTime())