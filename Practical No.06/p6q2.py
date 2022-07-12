#Program to count occurences of given word in a sentence
def countOccurrences(str, word):
	a = str.split(" ")
	count = 0
	for i in range(0, len(a)):
		if (word == a[i]):
			count = count + 1
	return count	
str ="GeeksforGeeks A computer science portal for geeks "
word ="portal"
print(countOccurrences(str, word))

