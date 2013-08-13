#!/usr/bin/env python
# -*- coding: utf-8 -*

from lib import *

runeDict = {}
for c in range(0, len(encRunes)):
	print pairs[c], encRunes[c]
	runeDict[pairs[c]] = encRunes[c]

letterDict = {}
for x in range(1, len(key)):
	letterDict[key[x]] = (pairs[x-1], pairs[x])
letterDict['e'] = (pairs[-1], pairs[0])  # easy way of rotating

def getEncRune(rune, nextRune):
	'''
	if rune is 't'
		pairs looks something like this:
			[('e','t'), ('t','a')]
	which EncRune to use will depend on the distance of nextRune to 'e' or 'a'
	'''
	pairs = letterDict[rune]
	i = key.index(nextRune)
	a = key.index(pairs[0][0])
	b = key.index(pairs[1][1])
	if abs(i-a) >= abs(i-b):
		return runeDict[pairs[0]]
	else:
		return runeDict[pairs[1]]

def encodeString(inputString):
	outputString = ''
	for i in range(0, len(inputString)):
		nextRuneIndex = i + 1
		nextRune = None
		while nextRune is None:
			try:
				nextRune = inputString[nextRuneIndex]
			except IndexError:
				nextRuneIndex = 0
				nextRune = inputString[nextRuneIndex]

			if nextRune not in alphabet:
				nextRuneIndex += 1
				nextRune = None	
	
		rune = inputString[i]
		if rune not in alphabet:
			outputString += rune
			continue
		

		outputString += getEncRune(rune, nextRune)
	return outputString


def main():
	s = "hello world"
	x = encodeString(s.lower())
	print x

if __name__ == '__main__':
	main()
