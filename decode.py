#!/usr/bin/env python
# -*- coding: utf-8 -*

from lib import *
import encode

encRunes = [x.decode("utf-8") for x in encRunes]

runeDict = {}
for c in range(0, len(encRunes)):
	runeDict[encRunes[c]] = pairs[c]

def shortestDistance(firstRune, secondRune):
	l = key
	firstIndex = l.index(firstRune)
	secondIndex = l.index(secondRune)
	return min((firstIndex - secondIndex) % len(l), (secondIndex - firstIndex) % len(l))


def decode(inputString):
	'''
	Making the decision which to choose is surprisingly more difficult than expected. 
	For example, Ꮬ can mean 'e', or 't'. The following logic tries to determine which it is 
		by basically reversing the steps (sorta) of the encoder

	The print statements are useful for debugging
	'''
	outputString = ""
	utf = inputString.decode("utf-8")
	nextHint = None
	for i in range(0, len(utf)):
		print "Initial NextHint: ", nextHint
		nextRuneIndex = i + 1
		nextRune = None
		
		while nextRune is None:
			try:
				nextRune = utf[nextRuneIndex]
			except IndexError:
				nextRuneIndex = 0
				nextRune = utf[nextRuneIndex]
			if nextRune not in encRunes:
				nextRuneIndex += 1
				nextRune = None
		rune = utf[i]
		if rune not in encRunes:
			outputString += rune
			continue


		pair = runeDict[rune]
		nextPair = runeDict[nextRune]
		print "Rune pairs: ", pair
		print "Next pair: ",  nextPair
		
		dd = {
			(0,0): None,
			(0,1): None,
			(1, 0): None,
			(1, 1): None,
		}

		pairings = ((0, 0), (0, 1), (1, 0), (1, 1))

		x = [encode.getEncRune(pair[k[0]], nextPair[k[1]]).decode("utf-8") for k in pairings]

		dd = {k:encode.getEncRune(pair[k[0]], nextPair[k[1]]).decode("utf-8") for k in pairings}

		for k, v in dd.items():
			if v == rune:
				dd[k] = 1
			else:
				dd[k] = 0
		
		dd = {k: v * shortestDistance(pair[k[0]], nextPair[k[1]]) for k, v in dd.items()}
		print dd
		for k, v in dd.items():
			if v == 0:
				dd[k] = 1000
		print dd
		nextHintIndex = -1
		if nextHint is not None:
			for hint in pair:
				if hint == nextHint:
					nextHintIndex = pair.index(hint)
		print dd
		for i in range(0,2):
			if nextHintIndex >= 0:
				if dd[(i, nextHintIndex)] != 1000:
					dd[(i, nextHintIndex)] -= 7 # 7 seems to be a good number to reduce by

		sd =  sorted(dd, key=dd.get)
		print dd	
		print sd
		outputString += pair[sd[0][0]]
		nextHint = nextPair[sd[0][1]]

		
		print nextHint
		print "_____\n"
	return outputString

def main():
	s = "ⵓᕶӼᎤኡ ɷኡⵓᎤӼ"
	print decode(s)


if __name__ == '__main__':
	main()
