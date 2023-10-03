for i in range(30):
	for j in range(i):
		for k in range(j):
			if (i**2==j**2+k**2):
				print((i,j,k))
