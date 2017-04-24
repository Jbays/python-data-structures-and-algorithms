import random
#Insertion Sort
#The insertion sort uses the principle of a marker moving along a list
#with a sorted side to the left side of the marker 
#and the unsorted side to the right of the marker.

# name: insertion_sort
# description: Searches for param0 inside param1
# param0 list: An unordered list of values
# returns: sorted list

def insertion_sort(list):

	marker = 0

	for num in list:
		print num
		

	
	# print list

sample_list = range(1,17)
random.shuffle(sample_list)

insertion_sort(sample_list)