Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name="harshith"
>>> print(name)
harshith
>>> city="vja"
>>> print(city)
vja
>>> fname=("Harshith"0
...        
SyntaxError: '(' was never closed
>>> fname=("Harshith")
...        
>>> fname="Harshith"
...        
>>> lastname=n)
SyntaxError: unmatched ')'
>>> fname="Harshith"
>>> lname="K"
>>> print(fname+lname)
HarshithK
>>> print(fname,lname)
Harshith K
>>> print(fname+""+lname)
HarshithK
>>> country="india"
>>> print(country)
india
>>> 
>>> #Keyword : do not start a variable with number or a special character. we can only use "_" symbol.
>>> _a=50
>>> print(_a)
50
>>> _=40
>>> print(_)
40
>>> if = 200
SyntaxError: invalid syntax
>>> mailid="harshith@gmail.com"
>>> print(mailid)
harshith@gmail.com
>>> 
>>> 
>>> #multiple variables in one line of code
>>> a,b=3,7
print(a+b)
10
a=10,b=50
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=5;b=4
print(a+b)
9
a,b,c=(1,2,3)
print(a+b-c)
0
print(a+b+c)
6



a,b,c=100
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a,b,c=100
TypeError: cannot unpack non-iterable int object
a,b,c=100,200,300
print(a,b,c)
100 200 300
a=b=c=250
print(a,b,c)
250 250 250
print(a+b+c)
750


#we should not give spaces between keywords in exchange we can give the character underscore "_"
print(fname+lname)
HarshithK
f name="Harshith"
SyntaxError: invalid syntax
f_name="Harshith"
print(f_name)
Harshith
print(lname,fname)
K Harshith


a=4
print(a)
4
del(a)
print(a)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: '_a'?
#for deleting the variable we use the keyword ("del")
#for deleting the variable we use the keyword ("del")


#variables are case sensitive
#python is case sensitive
city="vja"
print(city)
vja
City="Vja"
print City
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(City)
Vja
CITY="VJA"
print(CITY)
VJA
