import random
b=[]
for i in  range(20):
	b.append(random.randint(0,20))
print(b)
a=int(input("enter the number "))
for i in range(len(b)):
	if b[i]==a:
		print(i,)
