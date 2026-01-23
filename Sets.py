Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set{} unordered (semimutable)
a={3,5.6,"python",5+9j,True,False}
print(a)
{False, True, (5+9j), 3, 5.6, 'python'}
type(a)
<class 'set'>
a={4,6,8,8,65,5,5}
print(a)
{65, 4, 5, 6, 8}
#set dont allows repeated values

#issubset()
a={1,2,3,4,5,6,7,8}
b={4,5,6,7}
b.issubset(a)
True
a.issubset(b)
False

#issuperset()
a={5,4,6,7}
b={1,2,3,4,5,6}
a.issuperset(b)
False
b.issuperset(a)
False
a={4,5,6,7,8,9}
b={7,8,9}
a.issuperset(b)
True
b.issuperset(a)
False


#Union()
a={7,8,9,4,5,7,3,}
b={1,3,4,5,7,6}
a.union(b)
{1, 3, 4, 5, 6, 7, 8, 9}

#intersection()
a={1,2,3,4,5,8}
b={2,3,4,54}
a.intersection(a)
{1, 2, 3, 4, 5, 8}
b.intersection(b)
{2, 3, 4, 54}


#difference
a={3,4,5,6,7}
b={1,2,3,4,4,5,5,5,6,6,67,7}
a.difference(b)
set()
a={3,4,5,6,7}
b={1,2,3,4,5,6,7,8}
a.difference(b)
set()


#difference()
a={3,4,5,6,7,8}
b={1,2,3,4,5,6,7}
a.difference(b)
{8}
b.difference(a)
{1, 2}


#update()
a={1,3,5,7,9}
b={2,4,6,8,10}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b
{2, 4, 6, 8, 10}

#takes the latest update variable to merge.

#symmetric difference()
a={10,20,30,40,50,60}
b={20,30,50,90}
a.symmetric_difference(a)
set()
b.symmetric_difference(a)
{90, 40, 10, 60}


#difference_update()

a={4,5,6,7,8,9,10}
b={1,2,3,4,5,6,7,8}
a.difference_update(b)
a
{9, 10}
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8}

#intersectionupdate()
a={5,6,7,8,9}
b={2,3,4,5,6,7}
a.intersection_update(b)
a
{5, 6, 7}
b.intersection_update(a)
b
{5, 6, 7}

#symmetric difference update()
a={2,3,4,5,6}
b={1,2,3,4,5,6,7,8}
a.symmetric_difference_update(b)
a
{1, 7, 8}
b.symmetric_difference_update(a)
b
{2, 3, 4, 5, 6}
>>> 
>>> #pop()
>>> a={6,7,8,9,10,11}
>>> b={1,2,4,5,6,7,12}
>>> a.pop()
6
>>> a
{7, 8, 9, 10, 11}
>>> a.remove(11)
>>> a
{7, 8, 9, 10}
>>> b.remove(7,12)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    b.remove(7,12)
TypeError: set.remove() takes exactly one argument (2 given)
>>> b.remove(12)
>>> b
{1, 2, 4, 5, 6, 7}
>>> 
>>> 
>>> #copy()
>>> a={3,4,5,6,7}
>>> a.copy()=b
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> b=a.copy()
>>> b
{3, 4, 5, 6, 7}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(40)
>>> b
{40}
>>> b.add(20)
>>> b
{40, 20}
>>> 
>>> #len()
>>> a={4,5,6,7,8}
>>> len(a)
5
>>> a.count(b)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    a.count(b)
AttributeError: 'set' object has no attribute 'count'

a.index(b)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    a.index(b)
AttributeError: 'set' object has no attribute 'index'

#discard()
a={4,5,6}
a.discard(6)
a
{4, 5}

#disjoint()
a={1,3,55,7}
b={1,3,6,8}
a.isdisjoint(b)
False
a={1,2,3}
b={4,5,6}
a.isdisjoint(b)
True
