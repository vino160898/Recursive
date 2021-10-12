#addition of n numbers in recursive
def add(no):
	if no==1:
		return 1
	else:
		return no+ add(no-1)
print(add(5))  #15
