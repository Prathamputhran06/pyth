a=input("enter the sentence").split()
c=input("word").split()
b=[]
for i in a:
	if i in c :
		b.append(i[::].upper())
		continue
	b.append(i)
print(' '.join(b))
