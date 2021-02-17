def divisible(num):
	for x in range(1,21):
		if(num%x!=0):
			return False
	return True

def __main__():
	x = False
	num = 0
	while(not x):
		num+=20
		x = divisible(num)
	print(num)

__main__()