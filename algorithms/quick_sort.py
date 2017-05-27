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


# name: partition_phase
# description: 
# param0 list: An unordered list of values
# returns: sorted_list 

def partition_phase(list):
	print "partition_phase invoked!"


# name: quicksort
# description: 
# param0 list: An unordered list of values
# returns: sorted_list 

#the first goal is to partition the list into two lists
#the last element is chosen as pivot
#the lefthand list contains all numbers less than the pivot
#the righthand list contains all numbers greater than the pivot
#Now move the pivot to its rightful place between the lists

def quicksort(list):
	print "this is your list",list
	
	#two counters i and j
	#choose the last element in the list as our pivot
	pivot = list[(len(list)-1)]

	# for number in list:
	i = -1
	j = 0

	for each_number in list:

		if pivot < list[j]:
			j = j+1
			print "since pivot is less than list[j], do nothing!"
		elif pivot > list[j]:
			print "pivot is greater than list[j], do work!"
			i = i+1
			tobeswapped = list[i]
			print "list[i]>>",list[i]
			print "list[j]>>",list[j]
			print "pivot",pivot

			list[i] = list[j]
			list[j] = tobeswapped
			j = j+1

			print "They should've swapped!",list

	print "after everything's said and done>>>",i
	print list[0:i+1]

	return list


sample_list = range(1,17)
random.shuffle(sample_list)

# quicksort(sample_list)
print quicksort([7,2,1,8,6,3,5,4])

#Additional Notes:
# Wikipedia - Quick Sort
# In the very early versions of quicksort, 
# the leftmost element of the partition would often be chosen as the pivot element. 
# Unfortunately, this causes worst-case behavior on already sorted arrays, 
# which is a rather common use-case. 
# The problem was easily solved by choosing either a random index for the pivot, 
# choosing the middle index of the partition or (especially for longer partitions) 
# choosing the median of the first, middle and last element of the partition for the pivot.
# This "median-of-three" rule counters the case of sorted (or reverse-sorted) input, 
# and gives a better estimate of the optimal pivot (the true median) 
# than selecting any single element, when no information about the ordering of the input is known.
