#!/usr/bin/env python
# -*- coding: utf-8 -*

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'etaoinshrdlucmfwypvbgkjqxz'
keyshift = key[1:] + key[:1]
pairs = zip(key, keyshift)

encRunes = '''Ꮬ,ⴾ,ኡ,Ꮡ,Ꮊ,Ǭ,փ,ⵓ,ლ,Ӽ,Ꭴ,Ⴃ,ᕜ,ᙢ,ᗎ,ɷ,ዯ,Փ,ⵙ,※,ⴿ,ᖝ,ֆ,Ꮻ,Ꭽ,ᕶ'''.split(',')