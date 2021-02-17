def __main__():
	sum1 = 0
	sum2 = 0
	for x in range(1,101):
		sum1+=(x**2)
		sum2+=x

	sum2**=2
	print(sum2-sum1)

__main__()