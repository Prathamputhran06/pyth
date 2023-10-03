S=input("enter the string\n").lower()
a='abcdefghijklmnopqrstuvwxyz'
number=0
for i in S:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        number+=a.index(i)+1
print(number)
sum=0
while(True):
    while(number!=0): 
        sum+=number%10
        number=number//10
    if sum<10:
        break
print(sum)

