s=[2,0,0,1,0,0,2,2]
count=7
#s=[a for a in input()]
for i in range(len(s)):
	if s[i]==1:
		for j in range(len(s)):
			if s[j]==2:
				if i<j:
					if j-i<count:
						count=j-i
				elif i>j:
					if i-j<count:
						count=i-j
print(f"{count}:jasdhfjkah")  
