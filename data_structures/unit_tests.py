import unittest
import binarySearch


class TestStringMethods(unittest.TestCase):

	#check that the binary functions as intended
	def test_binary_search_tree(self):
		list = range(1,17)
		self.assertEqual(binarySearch.binarySearch(8,list),(True,1))
		self.assertEqual(binarySearch.binarySearch(1,list),(True,4))
		self.assertEqual(binarySearch.binarySearch(39,list),(False,5))
		self.assertEqual(binarySearch.binarySearch(-34,list),(False,4))


if __name__ == '__main__':
	unittest.main()