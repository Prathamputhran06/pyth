'''a=input("enter the string")
temp=0
for i in range(len(a)):
	if (ord(a[i])>ord(a[i+1])):
		temp=a[i]
		a[i]=a[i+1]
		a[i+1]=temp
print(a)'''
l=input().split()
print(sorted(l,key=str.lower))
