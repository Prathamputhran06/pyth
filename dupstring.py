haystack="sadbutsad"
needle="sad"
n2=len(needle)
for i in range(len(haystack)):
    if(haystack[i:i+n2].__eq__(needle)):
        print(i)
        exit()
print(-1)
