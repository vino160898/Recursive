def isprime(no,div):
	if no%div==0:
		return False
	else:
		div=div+1
		return isprime(no,div)
print(isprime(10,2))
