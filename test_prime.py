import unittest
from prime import generate_prime

class PrimeTest(unittest.TestCase):
	def test_five_prime(self):
        self.assertTrue(prime(5))

	def is_prime(self, n):
        pass

    def obtain_prime_factors(self, n):
        pass	
	
	def test_is_prime(self):
        self.assertTrue(prime(2))
        self.assertTrue(prime(3))
        self.assertFalse(prime(4))
        self.assertTrue(prime(5))
        self.assertFalse(prime(9))
        self.assertFalse(prime(10))
        self.assertTrue(prime(13))
		
	def test_is_zero_not_prime(self):
		self.assertFalse(prime(0))
	
	def test_negative_number(self):
		self.assertFalse(prime(-1))
		self.assertFalse(prime(-2))
		self.assertFalse(prime(-3))
		self.assertFalse(prime(-4))
		self.assertFalse(prime(-5))
		self.assertFalse(prime(-6))
		self.assertFalse(prime(-7))
		self.assertFalse(prime(-8))
		self.assertFalse(prime(-9))
		
	def test_four_non_prime(self):
		self.assertFalse(prime(4), msg='Four is not prime!')	
		
	
	
if __name__ == '__main__':
    unittest.main()