a1=int(input("a1"))
a2=int(input("a2"))
a3=int(input("a3"))
if(a1<90)and(a2<90)and(a3<90):
	print("actute angle triangle")
elif(a1>90)or(a2>90)or(a3>90):
	print("obtuse  angle triangle")
elif(a1==90)or(a2==90)or(a3==90):
        print("right  angle triangle")

