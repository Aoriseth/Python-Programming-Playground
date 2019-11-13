import os
import re

def collapseSavourAndGratitude(file):
	data = open(file).read()
	toKeep = re.search("(?<=\*Savour\*)[\S\s]+(?=\n\*Ex)",data)
	result = re.sub("\*Savour\*[\S\s]+(?=\*Exe)","\n",data)
	if toKeep:
		toKeep = toKeep.group(0)
	else:
		toKeep = ''
	# print(toKeep)
	result = re.sub("(\n\n)(?=\*Slee)",toKeep + "\n",result)
	return result
		
files = os.listdir()
files = filter(lambda x:os.path.isfile(x),files)
os.mkdir('updated')
for file in files:
	if file.endswith('.md'):
		output = open('updated/'+ file,'w')
		output.writelines(collapseSavourAndGratitude(file))