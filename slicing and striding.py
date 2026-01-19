Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Slicing
>>> a="codegnan"
>>> a[0:3]
'cod'
>>> a[0:4]
'code'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> a[2:6]
'degn'
>>> a[0:8]
'codegnan'
>>> a[0:]
'codegnan'
>>> 
>>> a="beautiful is better than ugly"
>>> a[13:19]
'better'
>>> a[0:8]
'beautifu'
>>> a[0:9]
'beautiful'
>>> a[25:]
'ugly'
>>> 
>>> b="vizag is a city of destiny"
>>> b[19:]
'destiny'
>>> b[11:15]
'city'
>>> b[0:5]
'vizag'
>>> 
>>> 
>>> #Negative slicing
>>> 
>>> a="time is very precious"
>>> a[-9:]
' precious'
>>> a[-8:]
'precious'
>>> a[-13:-10]
'ver'
a[-13:-9]
'very'
a[-21:-17]
'time'
b="every day is a learning"
b[-8:]
'learning'
b[-17:-14]
'day'
b[-23:-18]
'every'
b[-13:-11]
'is'
.
SyntaxError: invalid syntax

#striding
a=[::]
SyntaxError: invalid syntax
a="data science"
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'

b="cloud computing"
b[::6]
'cci'
b[::3]
'cucpi'
b[::4]
'cdmi'
a[5:9]
'scie'
a[:6]
'data s'
a[8:]
'ence'
