a=[int(input("enter the array1 elements\n")) for x in range(int(input("enter the array1 length\n")))]
b=[int(input("enter the array2 elements\n")) for x in range(int(input("enter the array2 length\n")))]
c=a+b
print(a,b,c)
if len(c)%2==0:
    b=c[int(len(c)/2)-1]+c[int((len(c)/2))]
else:
    b=c[int(len(c)/2)]
print(b)
