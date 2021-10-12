#addition of digit in recursive
def sum_of_digit(no):
	if no==0:
		return 0
	no2=int(no//10)
	return no %10+sum_of_digit(no2)
print(sum_of_digit(12))  #3
