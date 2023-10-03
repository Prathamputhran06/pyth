n=int(input())
l=[0]
for i in range(1,n+1):
  if i%2==0:
    l.append((i*i)-2)
  elif i%3==0:
    l.append((i*i)-1)
print(l)
