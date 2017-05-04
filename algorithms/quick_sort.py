import random

# Quicksort is a very efficient sorting algorithm invented by C.A.R. Hoare. 

# It has two phases:

# 1. the partition phase
# 2. the sort phase

# Most of the work is done in the partition phase - it works out where to divide the work. 
# The sort phase simply sorts the two smaller problems that are generated in the partition phase.

# This makes Quicksort a good example of the divide and conquer strategy for solving problems. 
# This is similar in principle to the binary search. 
# In the quicksort, we divide the array of items to be sorted into two partitions 
# and then call the quicksort procedure recursively to sort the two partitions, 
# ie we divide the problem into two smaller ones and conquer by solving the smaller ones.

# name: insertion_sort
# description: 
# param0 list: An unordered list of values
# returns: sorted_list 

def insertion_sort(list):
	print list	


sample_list = range(1,17)
random.shuffle(sample_list)

insertion_sort(sample_list)