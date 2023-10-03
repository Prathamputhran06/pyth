list=[eval(input()),eval(input()),eval(input())]
def count(i):
  a=[]
  while(i!=0):
    r=i%10
    i=i//10
    a.append(r)
  return a
def thousands(list):
  b=[]
  a=0
  c=0
  d=[]
  counter=0
  for i in list:
    b=b+count(i)
  b.sort()
  for j in range(len(b)):
    if b.count(j)>a:
      a=b.count(j)
      c=b[j]
    elif b.count(j)==a:
      d.append(j)
      counter+=1 
  if counter>1:
    d.sort()
    return d[len(d)-1]
  return c
#print(thousands(list))
def units(list):
  b=[]
  for i in list:
    b=b+count(i)
  b.sort()
  return b[len(b)-1]
#print(units(list))
def tens(list):
  b=[]
  for i in list:
    b=b+count(i)
  b.sort()
  return b[0]
#print(tens(list))
def hundreds(list):
  b=[]
  a=100
  c=0
  d=[]
  counter=0
  for i in list:
    b=b+count(i)
  b.sort()
  for j in range(len(b)):
    if b.count(j)==0:
      continue
    if b.count(j)<a:
      a=b.count(j)
      c=b[j]
    elif b.count(j)==a:
      d.append(j)
      counter+=1 
  if counter>1:
    d.sort()
    return d[0]
  return c
print(hundreds(list))
