import unittest
from factorization import Factorization


class TestFactorization(unittest.TestCase):
    def setUp(self) -> None:
        self.factorization = Factorization()

    def test_get_factorization(self):
        self.assertEqual(self.factorization.factorization(1), [])
        self.assertEqual(self.factorization.factorization(2), [2])
        self.assertEqual(self.factorization.factorization(3), [3])
        self.assertEqual(self.factorization.factorization(4), [2, 2])
        self.assertEqual(self.factorization.factorization(5), [5])
        self.assertEqual(self.factorization.factorization(6), [2, 3])
        self.assertEqual(self.factorization.factorization(7), [7])
        self.assertEqual(self.factorization.factorization(8), [2, 2, 2])
        self.assertEqual(self.factorization.factorization(9), [3, 3])
        self.assertEqual(self.factorization.factorization(10), [2, 5])
        self.assertEqual(self.factorization.factorization(11), [11])
        self.assertEqual(self.factorization.factorization(2*2*3*3*5*5*5*7), [2, 2, 3, 3, 5, 5, 5, 7])