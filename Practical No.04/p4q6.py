#left alligned number pattern
def contnum(n):
	num = 1
	for i in range(0, n):
		for j in range(0, i+1):
			print(num, end=" ")
			num = num + 1
		print("\r")
n = 5
contnum(n)

