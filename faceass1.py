str=input("enter the string\n")
str=list(str)
stack=[]
for i in str:
	if i in 'abcdefghijklmnopqrstuvwxyz':
		stack.append(i)
for j in range(len(str)):
	if str[j] in 'abcdefghijklmnopqrstuvwxyz':
		str[j]=stack.pop()
str=''.join(str)
print(str)
