str=input("enter the string")
str=str.split(".")
str=str[::-1]
str1=[]
for i in str:
	str1.append(i)
	str1.append(".")
str1.pop()
str1=''.join(str1)
print(str1)
