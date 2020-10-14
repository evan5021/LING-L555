
import sys

c = sys.stdin.read()
list = []

dictPOS = {}
dictCO = {}

r = c

c = c.replace(', ', ' ')
c = c.replace(',', ' ')
c = c.replace(': ', ' ')
c = c.replace(':', ' ')
c = c.replace(' (', ' ')
c = c.replace('(', ' ')
c = c.replace(') ', ' ')
c = c.replace(')', ' ')
c = c.replace('. ', ' ')
c = c.replace('.', ' ')
c = c.replace("'", " ")
c = c.replace('"', '')
c = c.replace('-', ' ')
c = c.replace('  ', ' ')


lines = c.split('\n')
r = r.split('\n')

cookie = 1

print('# P \t count \t tag \t form')

for cookies in lines:
	if cookies == '':
		pass
	else:
		cookie += 1
		list = cookies.split(' ')

		u = 1


		for m in list:
			if m == '':
				pass
			else:
				u += 1
				word = m
				tempL = word.split('#')
				dictPOS[tempL[0]] = tempL[1]
				if word in dictCO:
					dictCO[word] += 1
				else:
					dictCO[word] = 1

dictTAGS = {'ADP' : 0, 'NOUN' : 0, 'DET' : 0, 'ADJ' : 0, 'PRON' : 0, 'VERB' : 0, 'INTJ' : 0, 'ADV' : 0, 'CCONJ' : 0}
total = 0
for key in dictPOS:
	total += 1
	tempKey = dictPOS[key]
	dictTAGS[tempKey] += 1

for key in dictTAGS:
	print(str( '%.2f' % (dictTAGS[key] / total)) + '\t' + str(dictTAGS[key]) + '\t' + key + '\t _')

for key in dictPOS:
	tempKey = key + '#' + dictPOS[key]
	tempNum = 0
	if tempKey in dictCO:
		tempNum += 1
	print((dictCO[tempKey] / tempNum), end = '')
	print('\t' + str(dictCO[tempKey]) + '\t' + dictPOS[key] + '\t' + key)
