def is_isogram(str):
  str=str.upper()
  for cp in str:
    if not cp.isalpha():
      continue
    if str.count(cp)>1:
      return False
  return True
print(is_isogram(input('Enter the string\n')))
