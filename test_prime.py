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

class NthPrimeTest(unittest.TestCase):
    def test_nth_prime(self):
        self.assertEqual(prime.nth_prime(0), 2)
        self.assertEqual(prime.nth_prime(1), 3)
        self.assertEqual(prime.nth_prime(2), 5)
        self.assertEqual(prime.nth_prime(10), 31)
        self.assertEqual(prime.nth_prime(100), 547)
