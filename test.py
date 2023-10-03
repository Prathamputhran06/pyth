def prime(limit):
  l=[a for a in range(2,limit)]
  for i in l:
    for j in range(i,limit,i):
      a=l.index(j)
      l[a]=0
  return l
print(prime(10))

'''def prime(limit):
    l = [a for a in range(2, limit)]
    for i in l:
        if i != 0:
            for j in range(i * 2, limit, i):
                l[j - 2] = 0
    return [x for x in l if x != 0]

print(prime(10))
'''
