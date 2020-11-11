import sys
import re

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

for key in dictPOS:
	tempKey = key + '#' + dictPOS[key]
	tempNum = 0
	if tempKey in dictCO:
		tempNum += 1


list = []

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

for cookies in lines:
	if cookies == '':
		pass
	else:
		newStr = ''
		allWord = []
		allWord = r[cookie - 1].split(' ')
#		print(allWord)
#		print('')
		allWords = []
		for i in allWord:
			allWords.append(i.split('#'))
#		print(allWords)
		for i in range(len(allWords)):
			newStr = newStr + ' ' + allWords[i][0]
		newStr = newStr.strip(' ')
		print('\n # sent_id = ' + str(cookie) + '\n # text = ' + newStr)
		cookie += 1
		list = cookies.split(' ')

		u = 1
		allPOS = ['ADP', 'NOUN', 'DET', 'ADJ', 'PRON', 'VERB', 'INTJ', 'ADV', 'CONJ']
		try:
			list.remove('\n')
		except:
			for m in list:
				if m == '':
					pass
				else:
					num = 0
					type = ''
					for k in range (len(allPOS)):
						keys = allWords[u-1][0] + '#' + allPOS[k]
						if keys in dictCO:
							if dictCO[keys] > num:
								num = dictCO[keys]
								type = allPOS[k]
					print(str(u) + '\t' + allWords[u-1][0] + '\t_\t' + type + '\t_\t_\t_\t_\t_\t_')
					u += 1
