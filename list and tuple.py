Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #list[]
>>> 
>>> a=[2,4.5,"python",True,False]
>>> print(a)
[2, 4.5, 'python', True, False]
>>> 
>>> type(a)
<class 'list'>
>>> 
>>> b=4,5
>>> print(b)
(4, 5)
>>> 
>>> type(b)
<class 'tuple'>
>>> 
>>> a=["python","java","c"]
>>> KeyboardInterrupt
>>> a.append("c++")
>>> a
['python', 'java', 'c', 'c++']
>>> 
>>> 
>>> a=["vja","vzg","hyd"]
>>> a.extend(["bng","chennai"])
>>> a
['vja', 'vzg', 'hyd', 'bng', 'chennai']
>>> a.extend(["bng","chennai"])
>>> a
['vja', 'vzg', 'hyd', 'bng', 'chennai', 'bng', 'chennai']
>>> #extend
>>> 
>>> #insert()
>>> 
>>>  a=["ds","ai","ml"]
...  
SyntaxError: unexpected indent
>>> a=["ds","ai","ml"]
>>> a.insert(1,"python")
>>> a
['ds', 'python', 'ai', 'ml']
>>> a.insert(3,"c")
>>> a
['ds', 'python', 'ai', 'c', 'ml']
>>> 
#index

a=["apple","banana","grapes"]
a.index("banana")
1

#sort

b=["mango","grapes","apple","berry","kiwi"]
b.sort()
b
['apple', 'berry', 'grapes', 'kiwi', 'mango']

c=[6,9,3,0,1,5,10]
c.sort()
c
[0, 1, 3, 5, 6, 9, 10]

#reverse()

a=["hi","hello","how","are","you"]
a.reverse()
a
['you', 'are', 'how', 'hello', 'hi']

b=[5,7,9,2,0,1,]
a.reverse()
a
['hi', 'hello', 'how', 'are', 'you']

b=[5,7,9,2,0,1,]
b.reverse()
b
[1, 0, 2, 9, 7, 5]

#pop

a=["java","python","c","ds"]
a.pop()
'ds'
a
['java', 'python', 'c']
a.pop()
'c'

#remove()

a=["pooja","anitha","sindhu"]
a..remove("anitha")
SyntaxError: invalid syntax
a.remove("anitha")
a
['pooja', 'sindhu']

#copy()

a.copy()
['pooja', 'sindhu']
b=a.copy()
b
['pooja', 'sindhu']

#clear()

 a=["ml","ai","html","css"]
 
SyntaxError: unexpected indent
a=["ml","ai","html","css"]
a.clear()
a
[]
a.append("hi")
a
['hi']

#len()

a=["css","js","bs"]
len(a)
3
b="css"
len(b)
3

a=["css"]
len(a)
1

#count()

a=["black","white","red"]
a.count("black")
1

#task

a=["c","c++","java"]
a.extend(["python","ml"])
a
['c', 'c++', 'java', 'python', 'ml']
a.extend(["ds"])
a
['c', 'c++', 'java', 'python', 'ml', 'ds']

#tuple()

a=(4,5.7,"python",4+9j,True,False)
print(a)
(4, 5.7, 'python', (4+9j), True, False)
type(a)
<class 'tuple'>
len(a)
6
a.count(True)
1
a.count("True")
0
a.index(True)
4
