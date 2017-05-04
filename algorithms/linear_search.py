#Linear Search
#The linear search is used to find an item in a list. 

#INSTRUCTIONS:
#The items do not have to be in order. 
#To search for an item, 
#start at the beginning of the list and continue searching until either the end of the list is reached or the item is found.

myList = [1,4,6,8,10,35,8753,0,-20]

# name: Linear Search
# description - Searches through aList for a match with searchItem
##							If match found, prints "winner winner chicken dinner"
# param0 searchList: The list of values you wish to searchItem
# param1 searchItem: The item you wish to find
# returns: If match found, prints winner,winner chickenDinner!
##				 Else prints rejection

def linearSearch(aList,searchItem):
	print "You are searching for this value>>>",searchItem
	for eachEntry in aList:
		if eachEntry == searchItem:
			print "winner,winner,chickenDinner!"
			print "linearSearch found", eachEntry, "at index", aList.index(eachEntry)
		else:
			print searchItem, "is not equal to", eachEntry

# Searches for the second parameter inside the first
linearSearch(myList,0)