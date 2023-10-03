s=input("str")
t=input("str1")
a=dict()
for i,j in zip(s,t):
	if i not in a.keys() and j not in a.values():
		a[i]=j
count=0
for i in range(len(s)):
	if a.get(s[i])==t[i]:
		count+=1                                                
		continue
	else:
		print(False)
		break
if len(s)==count:
	print(True) 
