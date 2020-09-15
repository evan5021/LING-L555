import sys

sentences = []

text = sys.stdin.read()

sentences = text.split(". ")

final = ""

for line in sentences:
	line = line.replace("\n", "")
	if line != "":
		line += ".\n"
	final += line

print(final)
