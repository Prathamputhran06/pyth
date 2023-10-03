str2=input("enter the number")
str2=list(str2)
str1=[]
for i in range(len(str2)):
    if str2[i] in '0123456789':
        str1.append(str2[i])
        continue
    else:
        if str2[len(str2)-i-1] in '0123456789':
            for j in str2[-1::-1]:
                if j in '0123456789':
                    continue
                else:
                    str1.append(str2[len(str2)-j-1])
print(str1)
