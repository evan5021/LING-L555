import sys
import pickle

class Parser:

	def __init__(self,name):
		self.lexicon = {}
		self.syntax = {}
		self.sentence = ''
		self.sentence_list = []
		self.sentence_tagged = []
		self.current_tree = []
		self.head = 'S'

#Functions

	def welcome_screen(self):
		print('The head is currently ' + self.head)
		value = input('Enter command. For help, enter \'help\':\n')
		if(value == 'lex'):
			p.begin_lexical_rules()
		elif(value == 'help'):
			p.help()
		elif(value == 'pparse'):
			p.parse_POS()
		elif(value == 'end'):
			p.end_screen()
		elif(value == 'parse'):
			p.parse()
		elif(value == 'savesyn'):
			p.save_syn()
		elif(value == 'loadsyn'):
			p.load_syn()
		elif(value == 'savelex'):
			p.save_lex()
		elif(value == 'loadlex'):
			p.load_lex()
		elif(value == 'deletelex'):
			p.delete_lex()
		elif(value == 'deletesyn'):
			p.delete_syn()
		elif(value == 'load'):
			p.load_syn()
			p.load_lex()
		elif(value == 'save'):
			p.save_syn()
			p.save_lex()
		elif(value == 'head'):
			p.change_head()
		elif(value == 'syn'):
			p.begin_syntactic_rules()
		elif(value == 'view'):
			p.view_lexical_rules()
			p.view_syntactic_rules()
		else:
			print('--Unrecognized Command--')
#			p.welcome_screen()
		p.welcome_screen()
			
	def help(self):
		print('To begin writing lexical rules, please enter \'lex\'\nTo try and parse a sentence with lexical rules, please enter \'pparse\'\nTo save lexical rules, please enter \'savelex\'\nTo load lexical rules, please enter \'loadlex\'\nTo save syntactic rules, please enter \'savesyn\'\nTo load a syntactic rules, please enter \'loadsyn\'\nTo end the program, please enter \'end\'\nTo begin writing syntactic rules, please enter \'syn\'\nTo change the head, please enter \'head\'\nTo load all, please enter \'load\'\nTo save all, please enter \'save\'\nTo delete current lexical entries, please enter \'deletelex\'\nTo delete current syntactic entries, please enter \'deletesyn\'\nTo parse, please enter \'parse\'\nTo view all rules, please enter \'view\'\n')
	def load_syn(self):
		f = open('saved_syn.txt', 'rb')
		self.syntax = pickle.load(f)
		f.close
		print('Loaded following syntax:\n')
		p.view_syntactic_rules()
		print()
		
	def load_lex(self):
		f = open('saved_lex.txt', 'rb')
		self.lexicon = pickle.load(f)
		f.close
		print('Loaded following lexicon:\n')
		p.view_lexical_rules()
		print()
		
	def save_syn(self):
		f = open('saved_syn.txt', 'wb')
		pickle.dump(self.syntax, f)
		f.close	
		
	def save_lex(self):
		f = open('saved_lex.txt', 'wb')
		pickle.dump(self.lexicon, f)
		f.close
	
	def delete_lex(self):
		self.lexicon = {}
		
	def delete_syn(self):
		self.syntax ={}
		
	def end_screen(self):
		exit()
	def begin_lexical_rules(self):
		value = input('If you would like to go back enter \'leave\' if you would like to view all lexical rules, enter \'view\', otherwise press enter\n')
		if value == 'leave':
			pass
		elif value == 'view':
			p.view_lexical_rules()
			p.begin_lexical_rules()
		else:
			value1 = input('Please enter part of speech:\n')
			value2 = input('Please enter word:\n')
			self.lexicon[value2] = value1
			p.begin_lexical_rules()

	def view_lexical_rules(self):
		for key, value in self.lexicon.items():
			print(key + " has part of speech " + value)

	def view_syntactic_rules(self):
		for key, value in self.syntax.items():
			print(value + ' has daughters ', end='')
			for item in key:
				print(item + ' ', end='')
			print()

	def parse_POS(self):
		value = input('Please enter the sentence you wish to be parsed:\n')
		str = value.split(' ')
		for item in str:
			POS = self.lexicon[item]
			print(POS + '(' + item + ') ', end='')
		print('\nFinished')

	def parse(self):
		value = input('Please enter the sentence you wish to be parsed:\n')
		self.sentence = value
		self.sentence_list = value.split(' ')
		print(self.sentence_list)
		
		for item in self.sentence_list:
			print(item)
			self.sentence_tagged[p.find_POS(item)] = item
			print(self.sentence_tagged)

	def begin_syntactic_rules(self):
		value = input('If you would like to go back enter \'leave\' if you would like to view all syntactic rules, enter \'view\', otherwise press enter\n')
		if value == 'leave':
			pass
		elif value == 'view':
			p.view_syntactic_rules()
			p.begin_syntactic_rules()
		else:
			value1 = input('Please enter mother:\n')
			value2 = input('Please enter daughters:\n')
			self.syntax[tuple(value2.split(' '))] = value1
			p.begin_syntactic_rules()
			
	def find_POS(self, str):
		return self.lexicon[str]

	def change_head(self):
		value = input('Please enter new head:\n')
		self.head = value
#		p.welcome_screen()









#Beginning input

p = Parser('Evan')
print('Welcome to Evan\'s Parser!')
p.welcome_screen()
p.end_screen()
