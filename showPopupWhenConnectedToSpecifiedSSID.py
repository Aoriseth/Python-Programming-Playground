import subprocess
import regex
import schedule,time
import datetime

dictionary = {}

def getNetworkInformation():
	networkInfo = subprocess.check_output("netsh wlan show interfaces")
	return networkInfo.decode('utf-8')

def getNetworkName():
	query = regex.compile(r'(?<=\sSSID)(.+:\s)\K(.*)')
	networkName = query.search(getNetworkInformation())
	if networkName:
		return networkName.group(0).strip()
	else:
		return '<Not connected>'

def isWorkNetwork(networkname):
	if networkname=="CRONOS Wifi":
		return True
	else:
		return False

def checkNetworkNamePeriodically(networkname):
	if isWorkNetwork(networkname):
		print("Connected to Work Wifi")
		dateAndTime = datetime.datetime.now()
		date = dateAndTime.strftime('%Y-%m-%d')
		time = dateAndTime.strftime('%H:%M:%S')
		addConnectionToDatabase(date, time)
		print(dictionary)
	else:
		print("Checking network name.")
		print("Networkname is: ",networkname)
	 

def addConnectionToDatabase(date,time):
	if date not in dictionary:
		dictionary[date] = time

schedule.every(5).seconds.do(checkNetworkNamePeriodically,getNetworkName())



while True:
	schedule.run_pending()
	time.sleep(1)

