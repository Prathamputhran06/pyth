x = input('some text : ')
x={a for a in x.split(",")}
b=set()
c=set()
for i in x:
	if i[0]=='a':
		b.add(i)
	elif i[0]=='b':
		c.add(i)
print(b,c)
