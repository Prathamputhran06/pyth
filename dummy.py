'''a={1:1,2:2}
r=2
if r not in a:
	a[r]=1
else:
	a[r]+=1
print(a+a)
'''
'''
a={1:2,2:5}
c={1:3,2:10}
b={1:15,2:10}
for i,j in a.items() :
  print(i,j)
'''
b=[1,1,2,3,4,4]
d=[]
c=[]
for i in b:
  if i not in d:
    d.append(b.count(i))
    c.append(i)
print(d)
print(c)
