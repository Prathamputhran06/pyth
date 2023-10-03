s=[1,3,5,7,9]
s.insert(3,[2,4,6,8])
for i in s:
	if type(s)==list:
		s.append(i[::])
print(s)
