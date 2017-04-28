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
		print "here is the sorted_list",sorted_list
		print "here is the list",list
		print "+++++++++++++++++++++++"

		# the first number is automatically put into the sorted_list
		if len(sorted_list) == 0:
			sorted_list.append(list.pop())
			insertion_sort(sorted_list,list)
		elif len(sorted_list) > 0:
			# print "sorted_list:",sorted_list
			# print "list:",list
			print "before list",list
			to_be_sorted = list.pop()
			print "after  list",list
			print "to_be_sorted:",to_be_sorted

			print "before sorted_list",sorted_list
			sorted_list = sort_unsorted_num(to_be_sorted,sorted_list)
			print "after  sorted_list",sorted_list



		

	else:
		print "this list should be sorted",sorted_list
		print "this list should be empty",list

def sort_unsorted_num(num,list):
	num_is_sorted = False
	for sorted_num in list:
		sorted_index = list.index(sorted_num)
		print sorted_num
		print sorted_index
		if num < sorted_num:
			list.insert(sorted_index,num)
			num_is_sorted = True
		break

	if num_is_sorted == False:
		list.append(num)

	# print list
	return list

	# 4-23-2017
	# something about this conditional causes an infinite loop.
	# not sure what's wrong.  The logic is close to working.
		
	# 4-28-2017
	# I can visualize this solution implemented with recursion.
	# Once one instance of sorting has occured,
	# Remove that number from the original list
	# And pass both sorted & unsorted list to the original function
		

sample_list = range(1,17)
random.shuffle(sample_list)
print "this is before sorting!",sample_list
print "+++++++++++++++++++++++"

insertion_sort([],sample_list)