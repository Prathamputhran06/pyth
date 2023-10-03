h=int(input("enter the number"))
m=h
s=0
while(h>0):
	r=h%10
	s=s+(r**3)
	h=h//10
if(s==m):
	print("armstrong")
else:
	print("not")
