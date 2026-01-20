Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a="machine learning"
>>> 
>>> a[1:7:2]
'ahn'
>>> a[2:14:3]
'cnlr'
>>> a[3:15:2]
'hn eri'
>>> a[1:11:4]
'ane'
>>> 
>>> #negative striding
>>> 
>>> a="python course"
>>> a[-1:-9:-3]
'eu '
>>> a[-2:-12:-4]
'sch'
>>> a[-3:-13:-2]
'ro ot'
>>> a[-4:-10:-3]
'u '
>>> 
>>> #rules
>>> a[7:3:1]
''
>>> a[::-1]
'esruoc nohtyp'
>>> a[::1]
'python course'
>>> a[1::]
'ython course'
>>> a[0::]
'python course'
>>> a[-12:-3:-2]
''
>>> 
>>> #string methods
>>> 
>>> #len=no of characters in a string
>>> a="harshith"
>>> len(a)
8
>>> b="vishnu society"
>>> len(b)
14
c=""
len(c)
0
d="  "
len(d)
2

a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("n")
2
a.count(" ")
3
a.count("i")
3
a.count(k)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.count(k)
NameError: name 'k' is not defined
a.count('k')
2
#count method

#find a string

a="code"
a.find('e')
3
a.find('o')
1

b=("codegnan")
b.find('n')
5

#escape sequences
#\n->new line
#\t->tab space
a="name\nmobile num:\nmailid:\tcity"
print(a)
name
mobile num:
mailid:	city
print("name:harshith/nmobile num:8688079227\t@mailid\ncity:vja")
name:harshith/nmobile num:8688079227	@mailid
city:vja
print("name:harshith\nmobile num:8688079227\t@mailid\ncity:vja")
name:harshith
mobile num:8688079227	@mailid
city:vja
print("name:harshith\nmobile num:8688079227\t@mailid:harsh@gmail.com\ncity:vja")
name:harshith
mobile num:8688079227	@mailid:harsh@gmail.com
city:vja

#replace
a="work until you succeed"
a.replace("wait","work")
'work until you succeed'
b="try and try till u die"
b.replace("try" "work")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    b.replace("try" "work")
TypeError: replace() takes at least 2 positional arguments (1 given)
b.replace("try","work")
'work and work till u die'

#upper
a='hello'
a.upper()
'HELLO'
b='hiiii'
b='HIII'
b.lower()
'hiii'
#lower case

a="python"
a.capitalize()
'Python'

a='python course'
a.title()
'Python Course'

a='python course'
a.startswith("p")
True
a.endswith('n')
False
a.endswith('e')
True
a.isupper()
False
a.islower()
True
a.isdigit()
False
b="3939"
b.isdigit()
True

#isalpha
#isalnum
a="hello worls"
a.isalpha()
False
a="helloworld"
a.isalpha()
True
b="harsh575"
b.isalnum()
True
c="harsh"
c.isalnum()
True


#strip used to remove white spaces
#lstrip(),rstrip(),strip()
a="            harsh      "
a.lstrip()
'harsh      '
a.rstrip()
'            harsh'
a.strip()
'harsh'

#split()
a="python django c c++"
a.split()
['python', 'django', 'c', 'c++']
a="i am learning python fullstcak course"
a.split()
['i', 'am', 'learning', 'python', 'fullstcak', 'course']

#join
a="python",'c','java'
"".join(a)
'pythoncjava'
" ".join(a)
'python c java'

#concatintion()
#concatenation()
fname="harshith"
lname="k"
print(fname+lname)
harshithk
print(fname+" "+lname)
harshith k


print(fname.title()+" "+lname.title())
Harshith K
print((fname+" "+lname).title())
Harshith K
