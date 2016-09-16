from math import sqrt as sqrt

def isprime(x):
	for i in range(2,int(sqrt(x))+1):
		if x % i == 0:
			return False
	return True

def pseries(count):
	i = 0
	while(1):
		i += 1
		print("Checking " + str(i))
		res = True
		for j in range(i,i+count):
			if isprime(j):
				res = False
		if res == True:
			return i
