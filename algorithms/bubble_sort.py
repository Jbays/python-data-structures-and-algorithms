import random

# Bubble Sort

# Bubble sort, sometimes referred to as sinking sort, 
# is a simple sorting algorithm that repeatedly steps through the list to be sorted, 
# compares each pair of adjacent items 
# and swaps them if they are in the wrong order.

def bubble_sort(list,counter):
	for num in list:

		left = num
		try:
			right = list[list.index(num)+1]
			
			if (left > right):
				counter = counter+1
				left_position = list.index(left)
				right_position = list.index(right)
				
				temp = list[left_position]

				list[left_position] = list[right_position]
				list[right_position] = temp

				print "this list should have shuffled once!", list
				bubble_sort(list,counter)

		except:
			print "# of required bubble-sorts",counter

sample_list = range(1,17)
random.shuffle(sample_list)

bubble_sort(sample_list,0)
