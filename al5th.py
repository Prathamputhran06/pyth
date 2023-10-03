'''def f_substitute(str):
  str1=''
  for i in str:
    if ord(i)+5>=117:
      str1+=chr(((ord(i)+5)%123)+97)
    if ord(i)+5<117:
      str1+=chr(ord(i)+5)
  return str1
print(f_substitute(input()))


'''
'''
##########################
def f_substitute(str):
  if ord(str)+5>=117:
    a=(ord(str)+5)%123+97
  if ord(str)+5<117:
    a=a=ord(str)+5
  return chr(a)
print(f_substitute('a'))
'''
####################################
a='abcdefghijklmnopqrstuvwxyz'
def f_substitute(str):
  i=a.index(str)
  return a[(i+5)%26]
print(f_substitute('z'))
