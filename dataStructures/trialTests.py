import unittest
import binarySearch


class TestStringMethods(unittest.TestCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(),['hello','world'])
		#check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)

	#check that the binary functions as intended
	def test_binary_search_tree(self):
		list = range(1,17)
		print(binarySearch.binarySearch(1,list))
		print(binarySearch.binarySearch(8,list))

if __name__ == '__main__':
	unittest.main()