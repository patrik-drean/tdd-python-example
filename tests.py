import unittest
from fizz_buzz import *

class FizzBuzzTestCase(unittest.TestCase):

   def test_things(self): 
     self.assertEqual(return_1(), 1)
     
if __name__ == '__main__': 
   unittest.main() 