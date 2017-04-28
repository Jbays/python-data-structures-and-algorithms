import random

#Insertion Sort
#The insertion sort uses the principle of a marker moving along a list
#with a sorted side to the left side of the marker 
#and the unsorted side to the right of the marker.

# name: insertion_sort
# description: Should take scrambled values in list
##						 And unscramble then populate sorted_list with values
# param0 sorted_list: Initially empty
# param1 list: An unordered list of values
# returns: sorted_list 

def insertion_sort(sorted_list,list):

	#if list has values, continue sorting
	if len(list) > 0:
		# edge-case --> if sorted_list is empty,
		# then any value in sorted_list is sorted BY-DEFINITION
		if len(sorted_list) == 0:
			sorted_list.append(list.pop())
			insertion_sort(sorted_list,list)
		
		# general-case --> if sorted_list & list both have values!
		elif len(sorted_list) > 0:
			to_be_sorted = list.pop()

			#closure function to correctly place to_be_sorted in sorted_list 
			sorted_list = sort_unsorted_num(to_be_sorted,sorted_list)

			insertion_sort(sorted_list,list)
	
	#sorting is finished!
	else: 
		print "this list should be sorted",sorted_list
		print "this list should be empty",list

# name: sort_unsorted_num
# description: Determines where num belongs in list
##						 Inserts num, then returns list
# param0 num: A number
# param1 list: An ordered list of values
# returns: list

def sort_unsorted_num(num,list):
	num_is_sorted = False
	for sorted_num in list:
		sorted_index = list.index(sorted_num)
		if num < sorted_num:
			list.insert(sorted_index,num)
			num_is_sorted = True
			break

	# if num was NEVER found to be less than sorted_num
	# then num is the largest value in sorted_list
	if num_is_sorted == False:
		list.append(num)

	return list

sample_list = range(1,17)
random.shuffle(sample_list)
print "this is before sorting!",sample_list
print "+++++++++++++++++++++++"

insertion_sort([],sample_list)