# Python3 code to demonstrate list

# concatenation using naive method

test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

for i in test_list2 :
	test_list1.append(i)

print ("Concatenated list using naive method : "
							+ str(test_list1))


# concatenation using + operator

test_list3 = [1, 4, 5, 6, 5]
test_list4 = [3, 5, 7, 2, 5]

test_list3 = test_list3 + test_list4

print ("Concatenated list using + : "
				+ str(test_list3))

