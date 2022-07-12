#Python program to compute difference between 2 lists

list_1 = [5, 10, 15, 20, 25, 30]
list_2 = [10, 20, 30, 40, 50, 60]

difference_1 = set(list_1).difference(set(list_2))
difference_2 = set(list_2).difference(set(list_1))

list_difference = list(difference_1.union(difference_2))
print(list_difference)
