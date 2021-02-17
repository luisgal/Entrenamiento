def __main__():
	f_1 = 1
	f_2 = 2
	f_3 = f_1 + f_2

	sum = 2
	
	while(sum < 4000000):
		f_1 = f_2
		f_2 = f_3
		f_3 = f_1 + f_2
		
		if(f_3%2==0):
			sum += f_3

	print(sum)

__main__()