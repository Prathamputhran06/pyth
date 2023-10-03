def steps(num):
  count=0
  while(num!=1):
    if num%2==0:
      num=num/2
      count+=1
      continue
    num=(3*num)+1
    count+=1
  return count
print(steps(int(input())))


