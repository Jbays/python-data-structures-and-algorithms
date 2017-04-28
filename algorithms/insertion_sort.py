import random
#Insertion Sort
#The insertion sort uses the principle of a marker moving along a list
#with a sorted side to the left side of the marker 
#and the unsorted side to the right of the marker.

# name: insertion_sort
# description: Searches for param0 inside param1
# param0 list: An unordered list of values
# returns: sorted list

def insertion_sort(sorted_list,list):
	if len(list) > 0:
		# the first number is automatically put into the sorted_list
		if len(sorted_list) == 0:
			sorted_list.append(list.pop())
			insertion_sort(sorted_list,list)
		elif len(sorted_list) > 0:
			to_be_sorted = list.pop()
			sorted_list = sort_unsorted_num(to_be_sorted,sorted_list)

			insertion_sort(sorted_list,list)
	else:
		print "this list should be sorted",sorted_list
		print "this list should be empty",list

def sort_unsorted_num(num,list):
	num_is_sorted = False
	for sorted_num in list:
		sorted_index = list.index(sorted_num)
		if num < sorted_num:
			list.insert(sorted_index,num)
			num_is_sorted = True
			break

	if num_is_sorted == False:
		list.append(num)

	return list

sample_list = range(1,17)
random.shuffle(sample_list)
print "this is before sorting!",sample_list
print "+++++++++++++++++++++++"

insertion_sort([],sample_list)