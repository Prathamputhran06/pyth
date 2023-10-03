xa=[1,-2,-3,4,5,-7]
b=[]
c=[]
for i in range(len(a)):
	if a[i]>0:
		b.append(a[i])
	else:
		c.append(a[i])
print(b,c)
