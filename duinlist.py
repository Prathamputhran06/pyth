s=[2,3,4,2,3,5,6]
for i in range(len(s)):
	for j in range(i+1,len(s)):
		if s[i]==s[j]:
			s.pop(j)
