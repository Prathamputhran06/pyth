n=str(input())
l="abcdefghijklmnopqrstuvwxyz"
for i in l:
    if i not in n:
        print(i)
        break
