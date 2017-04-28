import random
#Insertion Sort
#The insertion sort uses the principle of a marker moving along a list
#with a sorted side to the left side of the marker 
#and the unsorted side to the right of the marker.

# name: insertion_sort
# description: Searches for param0 inside param1
# param0 list: An unordered list of values
# returns: sorted list

def insertion_sort(list,sorted_list):
	sorted_list = []

	#the first item is always sorted
	sorted_list.append(list.pop())

	# the first number is automatically put into the sorted_list


	for to_be_sorted in list:
		print "this is the number we're trying to sort",to_be_sorted
		index = len(sorted_list)-1

		if to_be_sorted > sorted_list[index]:
			print "back of the line!"
			sorted_list.append(to_be_sorted)
			list.remove(to_be_sorted)
			insertion_sort(list)

		else:
			

			for already_sorted in sorted_list:
				sorted_index = len(sorted_list)-1
				

				# print "this is number we're trying to insert>>",to_be_sorted
				print "compare to_be_sorted against this already_sorted>>>>>",already_sorted



				if to_be_sorted < already_sorted:
					print "this is the index for the sorted number",sorted_index
					#eight is less than eleven.
					#therefore insert before eleven
					#And to insert before eleven, we must know eleven's index
					#Then insert before eleven's index

					#This should sort the number we're trying to sort
					sorted_list.insert(sorted_index,to_be_sorted)
					list.remove
					print "this is the list",list
					print "this is the sorted list",sorted_list

					insertion_sort(list)





				# 4-23-2017
				# something about this conditional causes an infinite loop.
				# not sure what's wrong.  The logic is close to working.
				
				# 4-28-2017
				# I can visualize this solution implemented with recursion.
				# Once one instance of sorting has occured,
				# Remove that number from the original list
				# And pass both sorted & unsorted list to the original function

			



				# if to_be_sorted < already_sorted:

				# 	sorted_list.insert((sorted_list.index(already_sorted)-1),to_be_sorted)

				# marker = sorted_list.index(already_sorted)
				# print "this is my marker",marker
				# print already_sorted

	print "here is your sorted list>>>>>>",sorted_list
	return sorted_list
		

sample_list = range(1,17)
random.shuffle(sample_list)
print "this is before sorting!",sample_list

insertion_sort(sample_list)