for i in range(1,1001):
	s=0
	a=i
	while(i!=0):
		r=i%10
		s=s+(r**3)
		i=i//10
	if(s==a):
		print(a)
		continue
	else:
		continue
