a = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
def reset(a,b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i==b:
                a[b][j]=0
    return a
def reset1(a,c):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if j==c:
                a[i][c]=0
                print(a)
                break
    return a
l1=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]==0:
            b=i
            c=j
            if a[i+1][j]==1:
                l1.append(j)
            print(c)
            print(a)
            reset(a,b)
            reset1(a,c)
            break
print(a)
