d={'x':[80,75,85],'y':[75,65,90],'z':[75,65,90]}
for stu,marks in d.items():
	tot=sum(marks)
	avg=tot / len(marks)
	d[stu]={'total':tot,'average':avg}
top=max(d,key=lambda stu:d[stu]['total'])
print('marks:')
print(d)
print('topper',top)
