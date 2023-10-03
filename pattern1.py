import random
l=[]
for i in range(1,10):
	l.append(random.randint(1,10) )
print(l)
for i in l:
	print("*"*i)
