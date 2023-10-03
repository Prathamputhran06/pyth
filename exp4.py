s=[]
sum=0
while(1):
	x=int(input())
	if x+sum<100:
		s.append(x)
	elif x+sum==100:
		s.append(x)
		print(s)
		break
	elif x+sum>100:
		print("number exceeds 100")
		continue
	sum=sum+x
