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

# name: Quicksort
# description: 
# param0 list: An unordered list of values
# returns: sorted_list 

def Quicksort(list):
	print "before sorting",list
	end = list[(len(list)-1)]
	second = list[1]


	list.remove(second)

	print "end",end
	print "second",second


	if end < second:
		# put behind
		list.append(second)
	else:
		# else put in front
		list.insert((len(list)-1),second)

	#Do this process for half the list's length
	#Now break the list in half.

	#the first half 

	#There is a more generalizable rule at work.


	print "after sorting",list





sample_list = range(1,17)
random.shuffle(sample_list)

Quicksort(sample_list)

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
