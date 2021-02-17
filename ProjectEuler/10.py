import math

def primo(x):
	if(x%2==0):
		return False
	for i in range(3,math.floor(math.sqrt(x))+1,2):
		if(x%i==0):
			return False
	return True

def __main__():
	x = 3
	sum = 2
	while(x<2000000):
		if(primo(x)):
			sum+=x
		x+=2

	print(sum)

__main__()