n=input("enter the string")
a=[]
al=0
count=0
for i in range(len(n)):
    if n[i] not in a and n.count(n[i])>count:
        a.append(n[i])
        count=n.count(n[i])
        al=i
    if n[i]not in a and n.count(n[i])==count:
        if ord(n[i])>ord(n[al]):
            count=n.count(n[i])
            al=i
        else:
            count=n.count(n[al])
            al=al
n=list(n)
b=n[al]
for j in range(len(n)):
    if b==n[j]:
        n[j]='t'
c=''
for k in n:
    c+=k
print(c)
