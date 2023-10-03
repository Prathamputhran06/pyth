'''Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter.

The function should return 0 if a non-integer is passed in.'''


def add_it_up(num):
    if type(num)!=int or (num<0):
        return 0
    else:
        sum=0
        for i in range(0,num+1):
            sum+=i
        return sum
print(add_it_up(input("Enter the Number\n")))
