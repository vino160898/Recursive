#recursive in fibonacci series
def fibo(no):
	if no==1:
		return 1
	elif no==2:
		return 1
	else:
		return fibo(no-1)+fibo(no-2)

for no in range(5):
	print(fibo(no))
