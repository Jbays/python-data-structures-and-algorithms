import random

# Bubble Sort

# Bubble sort, sometimes referred to as sinking sort, 
# is a simple sorting algorithm that repeatedly steps through the list to be sorted, 
# compares each pair of adjacent items 
# and swaps them if they are in the wrong order.

# For example, we want to sort the list below:

# 1
# 12, 5, 7, 18, 11, 6, 12, 4, 17, 1

def bubble_sort(list,counter):
	print "here's the input list>>>>>>>>>>", list
	
	for num in list:

		left = num
		try:
			right = list[list.index(num)+1]
			
			if (left > right):
				# print "Left is greater than right!  Swap your variables!"
				counter = counter+1
				left_position = list.index(left)
				right_position = list.index(right)
				temp = left_position

				print list[left_position]
				print list[right_position]

				# list[left_position] = list[right_position]
				# list[right_position] = temp

				return bubble_sort(list,counter)
		except:
			print "# of required bubble-sorts",counter
			print "this list should be sorted>>>>>",list

sample_list = range(1,17)
random.shuffle(sample_list)

bubble_sort(sample_list,0)
