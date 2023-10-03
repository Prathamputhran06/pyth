def sqrt(r):
  if r<0:
    raise ValueError("number must be positive")
  return r**0.5
print(sqrt(int(input("enter the number"))))

