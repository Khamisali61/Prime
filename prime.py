def prime(n):
	for num in range(1, n):
		prime = True
		for i in range(2, num):
			if(num%i==0):
				prime = False
				
		if prime:
			print num
			
if __name__ == "__main__":
	prime()