import nmap

nm = nmap.PortScanner()

print('----------------------------------------------------')
nm.scan(hosts='192.168.10.0/24', arguments='-n -sP -PE -PA21,23,80,3389')


for host in nm.all_hosts():
	print('----------------------------------------------------')
	print('Host : %s (%s)' % (host, nm[host].hostname()))
	print('State : %s' % nm[host].state())
	print(nm[host])