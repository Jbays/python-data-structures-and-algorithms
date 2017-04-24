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
	sorted_list = []

	#the first item is always sorted
	sorted_list.append(list.pop())


	for num in list:
		index = len(sorted_list)-1

		if num > sorted_list[index]:
			print "back of the line!"
			sorted_list.append(num)
		else:


			for sorted_num in sorted_list:
				
				print "this is the number we're trying to sort",num
				print "this is the number up for comparison>>>",sorted_num

				# 4-23-2017
				# something about this conditional causes an infinite loop.
				# not sure what's wrong.  The logic is close to working.
				

				# if num < sorted_num:

				# 	sorted_list.insert((sorted_list.index(sorted_num)-1),num)

				# marker = sorted_list.index(sorted_num)
				# print "this is my marker",marker
				# print sorted_num

	print sorted_list
	return sorted_list
		

sample_list = range(1,17)
random.shuffle(sample_list)

insertion_sort(sample_list)