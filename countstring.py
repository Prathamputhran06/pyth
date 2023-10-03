s='heyyou123'
alpha=0
num=0
for i in s:
	if 'a'<=i<='z':
		alpha+=1
	elif '0'<=i<='9':
		num+=1
print(alpha,num)
