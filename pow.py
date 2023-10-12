n=int(input())
count=0
temp=n
while n>=2 :
	n=n/2
	count+=1
if 2**count==temp:
	print("true")
else:
	print("false")
