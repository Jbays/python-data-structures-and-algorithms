#Binary Search
#The binary search is used to find an item in an ORDERED list.

myList = [2, 5, 7, 12, 14, 21, 28, 31, 36]

# name: binarySearch
# description: Searches for param0 inside param1
# param0 item: The value you wish to find
# param1 list: The ORDERED list of values you wish to search
# returns: If found, true.  Else returns false


def binarySearch(item,list):
	found = False
	bottom = 0
	top = len(list)-1

	while bottom <= top and not found:
		middle = (bottom+top)//2
		if myList[middle]==item:
			found = True
		elif myList[middle] < item:
			bottom = middle+1
		else:

			top = middle-1

	print found
	return found

binarySearch(12,myList)