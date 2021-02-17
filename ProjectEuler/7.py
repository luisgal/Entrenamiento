import math

def primo(x):
	if(x%2==0):
		return False
	for i in range(3,math.floor(math.sqrt(x))+1,2):
		if(x%i==0):
			return False
	return True

def __main__():
	x = 1 #uno por el dos
	prim = 1
	while(x!=10001):
		prim+=2
		if(primo(prim)):
			x+=1
			
	print(prim)

__main__()