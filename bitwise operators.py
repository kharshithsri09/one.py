Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Bitwise operators
#AND (&)
a=3
b=4
a&b
0
bin(a)
'0b11'
bin(b)
'0b100'
a=2
b=6
a&b
2
bin(a)
'0b10'
bin(b)
'0b110'


#NOR (|)
a=2
b=6
a|b
6
a=4
b=8
a|b
12

#Negotiation
del
SyntaxError: invalid syntax
#xor
a=8
b=3
a^b
11
>>> a=3
>>> b=6
>>> a^b
5
>>> a=8
>>> b=9
>>> a^b
1
>>> #the same digits return 0 , opposite digits return 1
>>> 
>>> 
>>> #left shift
>>> a=4
>>> a<<2
16
>>> a=3
>>> a<<3
24
>>> a=6
>>> a<<2
24
>>> a=8
>>> a<<3
64
>>> 
>>> 
>>> #right shift
>>> a=5
>>> a>>2
1
>>> a=7
>>> a>>2
1
>>> a=8
>>> a>>3
1
>>> 
>>> 
>>> #not
>>> a=5
>>> ~a
-6
>>> a=11
>>> ~a
-12
>>> 
