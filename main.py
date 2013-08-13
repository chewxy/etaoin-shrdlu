#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import encode

filename = sys.argv[1]
output = sys.argv[2]

def main():
	with open(filename, 'r') as f:
		s = f.read().lower()
	encoded = encode.encodeString(s)
	g = open(output, 'w')
	g.write(encoded)
	g.close()

if __name__ == '__main__':
	main()
