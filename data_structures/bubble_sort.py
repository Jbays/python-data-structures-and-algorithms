import random

# Bubble Sort

# Bubble sort, sometimes referred to as sinking sort, 
# is a simple sorting algorithm that repeatedly steps through the list to be sorted, 
# compares each pair of adjacent items 
# and swaps them if they are in the wrong order.

# For example, we want to sort the list below:

# 1
# 12, 5, 7, 18, 11, 6, 12, 4, 17, 1

def bubble_sort(list):
	print list
	counter = 0
	for num in list:
		counter=counter+1


sample_list = range(1,17)
random.shuffle(sample_list)

bubble_sort(sample_list)
