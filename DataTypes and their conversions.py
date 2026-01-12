Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Data type conversions
#int
int(4)
4
int(7.8)
7
int("hi")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(4j+12)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(4j+12)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#the str and complex not converted.

#float
float(5)
5.0
float(7.0)
7.0
float("hiii")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float("hiii")
ValueError: could not convert string to float: 'hiii'
float(3+5j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(3+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#the str and complex not converted.

#string
str("5")
'5'
>>> str(6)
'6'
>>> str(9.0)
'9.0'
>>> str("Harsh")
'Harsh'
>>> str(4j+9)
'(9+4j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #all conversions are made because python is mostly based on string.
>>> 
>>> #complex
>>> complex(5)
(5+0j)
>>> complex(9.0)
(9+0j)
>>> complex("huuu")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex("huuu")
ValueError: complex() arg is a malformed string
>>> complex(6+9j)
(6+9j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #only the string was not converted.
>>> 
>>> #Boolean
>>> bool(5)
True
>>> bool(8.0)
True
>>> bool("hii")
True
>>> bool(4j+9)
True
>>> bool(True)
True
>>> bool(False)
False
