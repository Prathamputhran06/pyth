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
