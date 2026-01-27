#conditions
#if-elif

'''a=5
b=7
if a<b:
    print("true")
elif b>a:
    print("false")'''

#if two conditions are true, it only takes the first condition as output

'''a=5
b=7
if a==b:
    print("true")
elif b>a:
    print("false")'''

'''a=5
b=7
if a>b:
    print("true")
elif b<a:
    print("false")
elif a!=b:
    print("not equal")'''

#logical operators

'''a=10
b=20
if a<b and b>a:
    print("true")
elif a>b and b<a:
    print("false")'''

'''a=10
b=20
if a<b and b>a:
    print("true")
elif a!=b or a==b:
    print("false")
elif not a<b and b>=a:
    print("not equal")'''

'''a=4
if type(a) is not int:
    print("true")
elif type(a) is int:
    print("false")'''

#membership
'''a=3,4,5,6,7,8
if 8 in a:
    print("true")
elif 10 not in a:
    print("false")'''

#if-elif-else

'''a=10
b=20
if a>b:
    print("greater")
elif a==b:
    print("equal")
else:
    print("true")'''

'''a=10
b=20
if a<b:
    print("greater")
elif a==b:
    print("equal")
else:
    print("true")'''

#using logical operators

'''a=10
b=20
if a>b and b<a:
    print("greater")
elif a!=b or b==a:
    print("true")
elif not a<b and b>=a:
    print("false")
else:
    print("fl")'''

#multiple if

'''a=6
b=12
if a<b:
    print("less")
if b>a:
    print("greater")'''

#used to get all the conditions true

#using logical operators

'''a=10
b=5
if a>b and b<a:
    print("True")
if a!=b or a==b:
    print("equal or not equal")
if not b>a and a>b:
    print("False")'''

#idenfication operators

'''a=4
b="string"
if type(b) is not int:
    print("false")
if type(a) is int:
    print("true")'''

#membership

'''a=3,4,5,6,7,8
if 8 in a:
    print("true")
if 10 not in a:
    print("false")'''

#nested-if
'''a=4
b=8
if a<b:
    print("less")
    if b>a:
        print("greater")'''

"""a=4
b=8
if a==b:
    print("less")
    if b>a:
        print("greater")"""#the nested loop ends at first condition if it is false

'''a=4
b=8
if a>b:
    print("less")
    if b>a:
        print("greater")'''

'''a=4
b=8
if a<b:
    print("less")
    if b==a:
        print("greater")
    else:
        print("false")'''

'''a=4
b=8
if a==b:
    print("less")
    if b>a:
        print("greater")
    else:
        print("false")
else:
    print("true")'''


'''a=4
b=8
if a<b:
    print("less")
    if b==a:
        print("greater")
    elif a!=b:
        print("not equal")'''


#TASK

#voting

'''n=int(input("Enter your age :"))
if n<=18:
    print("Not eligible for voting")
else:
    print("Eligible for voting") '''

#even or odd

'''n=int(input("Enter your age :"))
if n%2==0:
    print("even number")
else:
    print("odd number")'''

#guest code

'''n=input("Enter your name")
if n=="Harshith":
    print("Welcome ",n)
else:
    print("Welcome guest",n)'''

#guest code for 5 names

'''names=["Harshith","Satya","Sri","Sai","Ram"]
a=input("Enter your name")
if a in names:
    print("Welcome ",a)
else:
    print("Welcome guest")'''





