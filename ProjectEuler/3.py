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
	max = x
	while(x<math.sqrt(600851475143)):
		if(primo(x) and 600851475143%x==0):
			max = x
		x+=2

	print(max)

__main__()