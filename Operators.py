Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Operators
#Arithmetic
a=6
b=9
print(a+b)
15
print(a-b)
-3
print(a*b)
54
print(a/b)
0.6666666666666666
print(a//b)
0
print(a%b)
6
print(a**b)
10077696

#Assignment
a=3
b=5
print(b+=a)
SyntaxError: invalid syntax
b+=a

b
8
b-=2
b
6
b*=4
b
24
b//=2
b
12
b/=6
b
2.0
b**=3
b
8.0
*b=a
SyntaxError: starred assignment target must be in a list or tuple
#syntax print doesnot work. and prefix dont work.

#Comparision
a=4
b=8
a<b
True
a>b
False
a!=b
True
a==b
False
a=6
b=6
a==b
True
a<=b
True
a>=b
True

#Logical
a=3
b=9
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
>>> a<=b or b>=a
True
>>> a!=b or b==a
True
>>> a>b not b>a
SyntaxError: invalid syntax
>>> a!=b
True
>>> not true
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> not True
False
>>> not False
True
>>> 
>>> #Identify
>>> a=5
>>> if type(a) is int:
...     print("it is int")
... 
...     
it is int
>>> if type(a) is not int:
...     print("false")
... 
...     
>>> #Membership
...     
>>> a=2,3,4,5,6,7,8,9,10
>>> if 10 in a:
...     print("True")
... 
...     
True
>>> if 20 in a:
...     print("False")
... 
...     
>>> if 17 not in a:
...     print("true")
... 
...     
true
