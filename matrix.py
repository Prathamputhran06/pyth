m=[[3,4,7,1],[3,4,1,8],[21,0,0,0],[8,1,6,9]]
r=len(m)
c=len(m[0])
l=[]
for i in range(len(m)):
  max=0
  for j in range(c):
    if m[i][j]>max:
      max=m[i][j]
  l.append(max)
print(l)
m2=list(zip(*m))
l2=[]
for s in range(r):
  max=0
  for k in range(c):
    if m2[s][k]>max:
      max=m2[s][k]
  l2.append(max)
print(l2)
d=[]
for a,b in zip(l,l2):
  if a>=b:
    d.append(a)
print(d,len(d))
