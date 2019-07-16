import subprocess
import regex

def getNetworkInformation():
	networkInfo = subprocess.check_output("netsh wlan show interfaces")
	return networkInfo.decode('utf-8')

def getNetworkName():
	query = regex.compile(r'(?<=\sSSID)(.+:\s)\K(.*)')
	networkName = query.search(getNetworkInformation())
	if networkName:
		return networkName.group(0)
	else:
		return '<Not connected>'

print(getNetworkName())
	 

