import sys



c = sys.stdin.read()
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
		print('\n # sent_id = ' + str(cookie) + '\n # text = ' + r[cookie - 1])
		cookie += 1
		list = cookies.split(' ')

		u = 1

		try:
			list.remove('\n')
		except:
			for m in list:
				if m == '':
					pass
				else:
					print(str(u) + '\t' + m + '\t_\t_\t_\t_\t_\t_\t_\t_\t_\t', end = '')					
					word = m
					word = ' ' + word + ' '
					map = {}
					map[' '] = ' '
					map['a'] = 'a'
					map['b'] = 'б'
					map['c'] = 'к'
					map['d'] = 'д'
					map['e'] = 'э'
					map['f'] = 'ф'
					map['g'] = 'г'
					map['h'] = 'х'
					map['i'] = 'и'
					map['j'] = 'ж'
					map['k'] = 'к'
					map['l'] = 'л'
					map['m'] = 'м'
					map['n'] = 'н'
					map['o'] = 'o'
					map['p'] = 'п'
					map['q'] = 'к'
					map['r'] = 'р'
					map['s'] = 'c'
					map['t'] = 'т'
					map['u'] = 'у'
					map['v'] = 'в'
					map['w'] = 'в' #maybe make this different
					map['x'] = 'кc'
					map['y'] = 'й'
					map['z'] = 'з'
					bimap = {}
					bimap['ch'] = 'ш'
					bimap['oi'] = 'уэ'
					bimap['ou'] = 'у'
					bimap['gn'] = 'њ'
					#bimap['er'] = 'э'
					bimap['ez'] = 'э'
					bimap['ce'] = 'с'
					map['é'] = 'э'
					map['è'] = 'э'
					map['œ'] = 'o'
					map['ê'] = 'э'
					bimap['ng'] = 'нж'
					bimap['x '] = ''
					bimap['r '] = ''
					bimap['s '] = ''
					bimap['e '] = ''
					#bimap['es'] = ''
					bimap[' h'] = ''
					map[''] = ''
					map[''] = ''
					map[''] = ''
					
					try:
						for i in range (len(word) - 1):
							temp = ''
							temp = temp + word[i]
							temp = temp + word[i + 1]
							try:
								word = word.replace(temp, bimap[temp])
							except:
								pass
					except:
						pass
					for letter in word:
						if letter in map:
							word = word.replace(letter, map[letter])
					
					print(word)			
					u += 1
