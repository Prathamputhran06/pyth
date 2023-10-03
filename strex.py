a='abcdefghijklmnopqrstuvwxyz'
def substitute(letter,n):
  i=a.index(letter)
  return a[(i+n)%26]
print(substitute(input("enter the alpha"),int(input("enter the shift"))))
