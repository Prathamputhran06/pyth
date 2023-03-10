a = ['python', 'programming', 'easy', 'enemy']
b = {}
c = []

for i in a:
    if i[0] not in b:
        b[i[0]] = [i]
    else:
        b[i[0]] += [i]
        
print(b)
print(c)

