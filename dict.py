price={'x':50,'y':43,'z':65}
quan={'x':2,'y':5,'z':3}
sum=0
for it,ru in price.items():
	for it1,qu in quan.items():
		if it==it1:
			sum+=ru*qu
print(sum)
