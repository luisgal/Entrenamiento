def palindromo(x):
	tam = len(x)
	for i in range((tam//2)+1):
		if(x[i] != x[tam-1-i]):
			return False
	return True

def __main__():
	max = 0
	for x in range(900,1000):
		for y in range(900,1000):
			if(palindromo(str(x*y))):
				max = x*y
	print(max)

__main__()