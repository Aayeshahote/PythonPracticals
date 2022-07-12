#Python program to sort tuples by total digits


def count_digs(tup):
	return sum([len(str(ele)) for ele in tup ])
test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
print("The original list is : " + str(test_list))
test_list.sort(key = count_digs)
print("Sorted tuples : " + str(test_list))

