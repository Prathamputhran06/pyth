import random
x=[]
y=[]
i=0
sum=0
sum1=0
def pattern(a):
    for i in range(len(a)):
        print('*'*a[i])
while(1):
    a=random.randint(1,25)
    if i%2==0:
        if a+sum<100:
            x.append(a)
        elif a+sum==100:
            x.append(a)
            print(x)
            print("a is the winner")
            pattern(x)
            break
        elif a+sum>100:
            continue
        sum=sum+a
    else:
        if a+sum1<100:
            y.append(a)
        elif a+sum1==100:
            y.append(a)
            print(y)
            print("b is the winner")
            pattern(y)
            break
        elif a+sum1>100:
            continue
        sum1=sum1+a
    i+=1
