import math

def divisors():
	div = 1
	x = 1
	tr = 1
	while(True):
		x+=1
		tr+=x
		div=0
		for i in range(1,math.floor(math.sqrt(tr))+1):
			if(tr%i==0):
				div+=1
		div*=2

		if(div>500):
			return tr

def __main__():
	print(divisors())


__main__()