a={}
b=input("enter the string")
for i in b:
	if i not in a:
		a[i]=1
	elif i in a:
		a[i]+=1
print(a)
