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
					print(str(u) + '\t' + m + '\t_\t_\t_\t_\t_\t_\t_\t_\t_\t_')
					u += 1
