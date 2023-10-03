='abcdefghijklmnopqrstuvwxyz'
def substitute(str,n):
  i=a.index(str)
  return a[(i+n)%26]
def encryption(text,key):
  en_string=''
  key=key*3
  for pos,cp in enumerate(text):
    key_cp=key[pos]
    n=a.index(key_cp)
    en_cp=substitute(cp,n)
    en_string=en_string+en_cp
  return en_string
print(encryption('jurassicpark','ankylosaur'))
def decryption(text,key):
  en_string=''
  key=key*3
  for pos,cp in enumerate(text):
    key_cp=key[pos]
    n=a.index(key_cp)
    en_cp=substitute(cp,-n)
    en_string=en_string+en_cp
  return en_string
print(decryption('jhbydgacjrrx','ankylosaur'))
