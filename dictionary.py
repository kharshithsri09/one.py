Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict (mutable and dont allow duplicates like sets.

a={"name":"harsh","college":"vishnu","year":2026}
print(a)
{'name': 'harsh', 'college': 'vishnu', 'year': 2026}
type(a)
<class 'dict'>
b={"name","year","month"}
type(b)
<class 'set'>

#keys(),values(),items()

a={"name":"harsh","college":"vishnu","year":2026}
a.keys()
dict_keys(['name', 'college', 'year'])
a.values(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.values(a)
TypeError: dict.values() takes no arguments (1 given)
a.values()
dict_values(['harsh', 'vishnu', 2026])
a.items()
dict_items([('name', 'harsh'), ('college', 'vishnu'), ('year', 2026)])

#accessinng an element

a={"name":"harsh","college":"vishnu","year":2026}
a["name"]
'harsh'
a["college"]
'vishnu'

#update

a={"name":"harsh","college":"vishnu","year":2026}
a.update({"month":"june"})
a
{'name': 'harsh', 'college': 'vishnu', 'year': 2026, 'month': 'june'}
#can also give multiple pairs

a.update({"min":2,"friend":"harshith"})
a
{'name': 'harsh', 'college': 'vishnu', 'year': 2026, 'month': 'june', 'min': 2, 'friend': 'harshith'}

#set default()
a={"course":"python"}
a
{'course': 'python'}
a.setdefault("institute","codegnan")
'codegnan'
a
{'course': 'python', 'institute': 'codegnan'}

#pop() and popitem()
a={"food":"biryani","fruit":"mango"}
a.pop("food")
'biryani'
a
{'fruit': 'mango'}
a.popitem()
('fruit', 'mango')
a
{}


#copy and len and clear()
a={"name":"harsh","college":"vishnu","year":2026}
a.copy()
{'name': 'harsh', 'college': 'vishnu', 'year': 2026}
b=a.copy()
b
{'name': 'harsh', 'college': 'vishnu', 'year': 2026}
len(a)
3
a.clear()
a
{}

#get

a={"name":"harsh","college":"vishnu","year":2026}
a.get("college")
'vishnu'

#it dont allows duplicate keys
a={"name":"harsh","college":"vishnu"}
print(a)
{'name': 'harsh', 'college': 'vishnu'}
a={"name":"harsh","college":"vishnu","college1:krishna"}
SyntaxError: ':' expected after dictionary key
a={"name":"harsh","college":"vishnu","college1":"krishna"}
print(a)
{'name': 'harsh', 'college': 'vishnu', 'college1': 'krishna'}
>>> a={"idno":[10,20,30],"name":["harsh","surya","chandu"]}
>>> a
{'idno': [10, 20, 30], 'name': ['harsh', 'surya', 'chandu']}
>>> a.keys()
dict_keys(['idno', 'name'])
>>> a.values()
dict_values([[10, 20, 30], ['harsh', 'surya', 'chandu']])
>>> a.items()
dict_items([('idno', [10, 20, 30]), ('name', ['harsh', 'surya', 'chandu'])])
>>> #to insert multiple values in one pair
>>> 
>>> 
>>> 
>>> #list task
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a1=a[:5]
>>> a11
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a11
NameError: name 'a11' is not defined. Did you mean: 'a1'?
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[6:]
>>> a2
[6, 3, 7, 0]
>>> a2=a[5:]
>>> a2
[4, 6, 3, 7, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> c=a2+a1
>>> c
[7, 6, 4, 3, 0, 1, 2, 5, 8, 9]
>>> a1.reverse()
>>> c=a2+a1
>>> c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
