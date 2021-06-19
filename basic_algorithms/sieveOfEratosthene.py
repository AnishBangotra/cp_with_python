#print all primes smaller than or equal to n.
def sieveOfEratosthenes(n):
	#Creating a boolean array upto length n and initialize all entries of it as true.
	#We change value to false if i goes not a prime else true.
	prime = [True for i in range(n+1)]
	p = 2
	while (p*p <= n):
		if prime[p] == True:
			#change multiples of p
			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1
	#printing
	for p in range(2, n+1):
		if prime[p]:
			print(p)

#for value of n
sieveOfEratosthenes(n)