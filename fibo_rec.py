#recursive in fibonacci series
def fibo(no):
	if no<=1:
		return no
	else:
		return fibo(no-1)+fibo(no-2)

for no in range(5):
	print(fibo(no))
