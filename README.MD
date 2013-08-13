This is a toy language encoding example.

It takes: "Hello World" and makes it into "ⵓᕶӼᎤኡ ɷኡⵓᎤӼ"

Now, this is not a 1 to 1 mapping. Instead, it maps 2 alphabets to 1 rune, specifically in this order:
<table>
<thead>
	<th>Pairs of letters</th>
	<th>Rune</th>
</thead>
<tbody>
<tr><td>('e', 't')</td><td>Ꮬ</td></tr>
<tr><td>('t', 'a')</td><td>ⴾ</td></tr>
<tr><td>('a', 'o')</td><td>ኡ</td></tr>
<tr><td>('o', 'i')</td><td>Ꮡ</td></tr>
<tr><td>('i', 'n')</td><td>Ꮊ</td></tr>
<tr><td>('n', 's')</td><td>Ǭ</td></tr>
<tr><td>('s', 'h')</td><td>փ</td></tr>
<tr><td>('h', 'r')</td><td>ⵓ</td></tr>
<tr><td>('r', 'd')</td><td>ლ</td></tr>
<tr><td>('d', 'l')</td><td>Ӽ</td></tr>
<tr><td>('l', 'u')</td><td>Ꭴ</td></tr>
<tr><td>('u', 'c')</td><td>Ⴃ</td></tr>
<tr><td>('c', 'm')</td><td>ᕜ</td></tr>
<tr><td>('m', 'f')</td><td>ᙢ</td></tr>
<tr><td>('f', 'w')</td><td>ᗎ</td></tr>
<tr><td>('w', 'y')</td><td>ɷ</td></tr>
<tr><td>('y', 'p')</td><td>ዯ</td></tr>
<tr><td>('p', 'v')</td><td>Փ</td></tr>
<tr><td>('v', 'b')</td><td>ⵙ</td></tr>
<tr><td>('b', 'g')</td><td>※</td></tr>
<tr><td>('g', 'k')</td><td>ⴿ</td></tr>
<tr><td>('k', 'j')</td><td>ᖝ</td></tr>
<tr><td>('j', 'q')</td><td>ֆ</td></tr>
<tr><td>('q', 'x')</td><td>Ꮻ</td></tr>
<tr><td>('x', 'z')</td><td>Ꭽ</td></tr>
<tr><td>('z', 'e')</td><td>ᕶ</td></tr>
</tbody>
</table>

Part of the fun was writing the encoding, and the rules, but most of the fun had come from writing the decoder. It's hard, given the rules of the encoder.

# Licence #
The MIT License (MIT)

Copyright (c) 2013 Xuanyi Chew

Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.