def square(number):
  if number<1 or number>64:
    raise ValueError("Square number out of range")
  return 2**(number-1)
def total():
  sum=0
  for i in range(1,65):
    sum+=square(i)
  return sum
print(total())
'''alternate solution
def totol()
  return 2**64-1'''
