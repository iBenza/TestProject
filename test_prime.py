import unittest
import prime

class PrimeTest(unittest.TestCase):
    def test_with_less_than_2(self):
        self.assertFalse(prime.is_prime(-5))
        self.assertFalse(prime.is_prime(0))
        self.assertFalse(prime.is_prime(1))

    def test_with_non_primes(self):
        self.assertFalse(prime.is_prime(6))
        self.assertFalse(prime.is_prime(9))

    def test_with_primes(self):
        self.assertTrue(prime.is_prime(2))
        self.assertTrue(prime.is_prime(3))
        self.assertTrue(prime.is_prime(11))
