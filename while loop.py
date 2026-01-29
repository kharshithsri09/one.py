#while loop

'''a=10
while a>1:
    print(a)'''


'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    a=a-1
    print(a)'''


'''a=10
while a>1:
print(a)    
    a=a-1'''#syntax error

'''a=10
while a>1:
    print(a)
    a+=1'''#infinity

'''a=1
while a<10:
    print(a)
    a+=1'''

'''a=20
while a>1:
    print(a)
    a-=1'''

#TASK USING WHILE FOR INFINTE EXECUTION

#Voting

'''while True:
    n=int(input("Enter your age :"))
    if n<=18:
        print("Not eligible for voting")
    else:
        print("Eligible for voting")'''

#even or odd

'''while True:
    n=int(input("Enter number :"))
    if n%2==0:
        print("even number")
    else:
        print("odd number")'''

#guest code for 5 names
'''while True:
    names=["Harshith","Satya","Sri","Sai","Ram"]
    a=input("Enter your name")
    if a in names:
        print("Welcome ",a)
    else:
        print("Welcome guest")'''


#TASK
'''while True:
    n=input("Enter an alphabet: ")
    a=("a","e","i","o","u")
    if n in a:
        print("It is an vowel")
    else:
        print("It is a consonant")'''

"""while True:
    n=int(input("Enter the budget :"))
    a={1200:"Red Velvet Cake",1000:"Chocolate Cake",800:"Choco Almond Cake",600:"Butterscotch Cake"}
    if n in a:
        print(a.value,"")
    else:
        print("not available")"""#to work on it 

'''while True:
    n=int(input("Enter the budget :"))
    if n==1200:
        print("Red Velvet Cake")
    elif n==1000:
        print("Chocolate Cake")
    elif n==800:
        print("Choco Almond Cake")
    elif n==600:
        print("Butterscotch Cake")
    else:
        print("No Cakes Available")'''

