import unittest
from assignment.solution import sum_of_evens

class TestSumOfEvens(unittest.TestCase):
    
    def test_example_cases(self):
        # Test with mixed positive and negative numbers
        self.assertEqual(sum_of_evens([1, 2, 3, 4, 5]), 6)
        self.assertEqual(sum_of_evens([1, 3, 5, 7]), 0)
        self.assertEqual(sum_of_evens([]), 0)
        
    def test_negative_numbers(self):
        # Test with negative numbers
        self.assertEqual(sum_of_evens([-2, -4, -6]), -12)
        self.assertEqual(sum_of_evens([-1, -3, -5]), 0)
        
    def test_large_numbers(self):
        # Test with larger numbers in range
        self.assertEqual(sum_of_evens([1000, 1001, 2000]), 3000)
        self.assertEqual(sum_of_evens([999, 1001, 1003]), 0)
        
    def test_edge_cases(self):
        # Test with a list that contains only one number
        self.assertEqual(sum_of_evens([2]), 2)
        self.assertEqual(sum_of_evens([1]), 0)
        
        # Test with list containing both even and odd numbers
        self.assertEqual(sum_of_evens([0, 1, 2, 3, 4, 5]), 6)

if __name__ == '__main__':
    unittest.main()
