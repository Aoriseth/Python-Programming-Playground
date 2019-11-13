import json

file = open('sample-data.json')

sampleData = json.load(file)


def parseFields(sampleData):
	for field, value in sampleData.items():
		print('<div class="card">')
		print('<h3>',field,': ',value,'</h3>')
		if isinstance(value,dict):
			parseFields(value)
		print('</div>')
			

print('<div class="column">')
parseFields(sampleData)
print('</div>')