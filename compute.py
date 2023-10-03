for i in range(1,1000):
  s=i
  while(s!=0):
    r=s%10
    s=s//10
    if r==3:
      break
  else:
    print(i)
