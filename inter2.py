s=input()
for i in range(len(s)):
	if s[i]=='M':
		if i>0:
			s=s[:i]+s[i-1]+s[i+1:]
		elif s[0]=='M':
			s=s[2:]
'''	if s[i]=='N':
                if i<(len(s)-1):
                        s=s[:i-1]+s[i+1]+s[i+1:]
#                elif i==0:
#                        s=s[i+1:]'''

print(s)
