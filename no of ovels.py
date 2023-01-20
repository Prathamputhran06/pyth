a=['google','bleed','blood']
b={}
for i in a:
    for j in range (len(i)-1):
        if i[j] not in b:
            if i[j] == i[j+1]:
                b[i[j]]=1
        else:
            if i[j] == i[j+1]:
                b[i[j]]+=1
print(b)
