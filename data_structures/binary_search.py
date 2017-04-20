#Binary Search
#The binary search is used to find an item in an ORDERED list.

# name: binarySearch
# description: Searches for param0 inside param1
# param0 item: The value you wish to find
# param1 list: The ORDERED list of values you wish to search
# returns: If found, true.  Else returns false

def binarySearch(item,list):
	found = False
	bottom = 0
	top = len(list)-1
	counter = 0

	while bottom <= top and not found:
		counter = counter+1

		middle = (bottom+top)//2
		if list[middle]==item:
			found = True
		elif list[middle] < item:
			bottom = middle+1
		else:
			top = middle-1

	return (found,counter)