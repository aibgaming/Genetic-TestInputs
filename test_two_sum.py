# test_two_sum.py
import unittest
from two_sum import two_sum

class TestTwoSum(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
    
    def test_negative_numbers(self):
        self.assertEqual(two_sum([-2, -3, -7], -5), [0, 1])
    
    def test_no_solution(self):
        self.assertEqual(two_sum([1, 2, 3], 6), [])
    
    def test_large_input(self):
        self.assertEqual(two_sum(list(range(100000)), 199998), [99998, 99999])

if __name__ == "__main__":
    unittest.main()
