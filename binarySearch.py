#Binary Search
#The binary search is used to find an item in an ORDERED list.

myList = [2, 5, 7, 12, 14, 21, 28, 31, 36]

# name: binarySearch
# description:
# param0 searchList: The ORDERED list of values you wish to search
# param1 searchItem: The value you wish to find
# returns: 


def binarySearch(aList,searchItem,counter):
	counter+=1

	print "You are searching for this value>>>",searchItem
	listMidpoint = len(aList)/2
	midPointVal = aList[listMidpoint]

	splitLists = split_list(aList)
	print splitLists
	print "this is the midPointValue",aList[listMidpoint]

	#case 1: match
	if searchItem == midPointVal:
		print "match!"
		print "number of searches",counter

	else:
		print "no match -- will continue search!"
		
		#case 2: searchItem is greater
		if searchItem > midPointVal:
			print "searchItem is greater than midPointVal"
			binarySearch(splitLists[1],searchItem,counter)

		#case 3: searchItem is lesser
		elif searchItem < midPointVal:
			print "searchItem is less than midPointVal"
			binarySearch(splitLists[0],searchItem,counter)

		#case 4: not found
		else:
			print "your value is not present"
			print "Searched list this many times>>>>",counter


def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]
		
# Searches for the second parameter inside the first
binarySearch(myList,99,0)