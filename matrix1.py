m=[[3,4,7,1],[3,4,1,8],[21,15,0,0],[8,1,6,9]]
l=[]
z=[]
s=len(m)
for i in range(len(m)):
  max=0
  for j in range(len(m[0])):
    if m[i][j]>=max:
      max=m[i][j]
      ind=j
  l.append(max)
  z.append(ind)
m2=list(zip(*m))
for k in range(len(m2)):
  
print(l)
