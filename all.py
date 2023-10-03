'''a='alvas'
for i in range(len(a)+1):
    print( )
    for j in range(i):
        print(a[j],end=' ')'''
######################################################
'''a='how are you'
for i in range(len(a)):
    if(i==' '):
        print(a(i+1).capitalize())
    else:
        print(a[i])'''
#######################################################
'''a='how are you'
a.split()
for i in a:
    print(a)'''
######################################################
'''a=input("enter the sentence").split()
c=input("word").split()
b=[]
for i in a:
    if i in c :
        for j in range(len(i)):
            b.append(a[j].upper())
            j+=2
b.append(i)
print(b)'''
#####################################################
'''print(ord('a'))
print(chr(97))'''

##################################################
'''ramanujan number
a=int(input("enter the number"))
count=0
for i in range(1,a+1):
    for j in range(1,a+1):
        if ((i**3)+(j**3))==a:
            count+=1
if count>=2:
    print("ramanujan number")
else:
    print("not")
   '''
#####################################################
'''y=int(input("enter the year"))
if(y%400==0) or (y%100!=0) and (y%4==0):
    print("leap")
else:
    print("not leap")
   '''
######################################################
a1=int(input("angle 1"))
a2=int(input("angle 2"))
a3=int(input("angle 3"))
if(a1+a2+a==180):
    print("valid")
else:
    print("invalid")

    
    
