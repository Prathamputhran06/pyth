import random
y=set()
x=set()
for i in range(10):
	x.add(random.randint(15,45))
print(x)
for j in x:
	if j<35:
		y.add(j)
print(len(y))
print(y)
