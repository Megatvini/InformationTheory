import unittest
from Polynomial import Polynomial


class TestPolynomialMethods(unittest.TestCase):
    def test_to_str0(self):
        p = Polynomial([], 2)
        self.assertEqual('0', str(p))

    def test_to_str1(self):
        p = Polynomial([0, 0], 2)
        self.assertEqual('0', str(p))

    def test_to_str2(self):
        p = Polynomial([1, 1], 2)
        self.assertEqual('1 + x', str(p))

    def test_to_str3(self):
        p = Polynomial([1, 0, 1], 2)
        self.assertEqual('1 + x^2', str(p))

    def test_to_str4(self):
        p = Polynomial([3, 3], 2)
        self.assertEqual('1 + x', str(p))

    def test_to_str5(self):
        p = Polynomial([1, 1, 1, 1, 1], 2)
        self.assertEqual('1 + x + x^2 + x^3 + x^4', str(p))

    def test_to_str6(self):
        p = Polynomial([1, 2, 3, 4, 5], 2)
        self.assertEqual('1 + x^2 + x^4', str(p))

    def test_to_str7(self):
        p = Polynomial([1, 2, 3, 4, 5], 5)
        self.assertEqual('1 + 2x + 3x^2 + 4x^3', str(p))

    def test_to_str8(self):
        p = Polynomial([2, 2, 3, 4, 5], 5)
        self.assertEqual('2 + 2x + 3x^2 + 4x^3', str(p))

    def test_add_0(self):
        p1 = Polynomial([1], 2)
        p2 = Polynomial([1], 2)
        res = p1 + p2
        self.assertEqual('0', str(res))

    def test_add_1(self):
        p1 = Polynomial([1, 1], 2)
        p2 = Polynomial([1], 2)
        res = p1 + p2
        self.assertEqual('x', str(res))

    def test_add_2(self):
        p1 = Polynomial([0, 1], 2)
        p2 = Polynomial([1], 2)
        res = p1 + p2
        self.assertEqual('1 + x', str(res))

    def test_add_3(self):
        p1 = Polynomial([0, 1, 2, 1, 1], 3)
        p2 = Polynomial([1, 1, 1, 2], 3)
        res = p1 + p2
        self.assertEqual('1 + 2x + x^4', str(res))

    def test_subs_0(self):
        p1 = Polynomial([1], 2)
        p2 = Polynomial([1], 2)
        res = p1 - p2
        self.assertEqual('0', str(res))

    def test_subs_1(self):
        p1 = Polynomial([1, 1], 2)
        p2 = Polynomial([1], 2)
        res = p1 - p2
        self.assertEqual('x', str(res))

    def test_subs_2(self):
        p1 = Polynomial([0, 1], 2)
        p2 = Polynomial([1, 0], 2)
        res = p1 - p2
        self.assertEqual('1 + x', str(res))

    def test_multiply0(self):
        p1 = Polynomial([1], 2)
        p2 = Polynomial([1], 2)
        res = p1 * p2
        self.assertEqual('1', str(res))

    def test_multiply1(self):
        p1 = Polynomial([1, 1], 2)
        p2 = Polynomial([1, 1], 2)
        res = p1 * p2
        self.assertEqual('1 + x^2', str(res))

    def test_multiply2(self):
        p1 = Polynomial([1, 1], 3)
        p2 = Polynomial([1, 1], 3)
        res = p1 * p2
        self.assertEqual('1 + 2x + x^2', str(res))

    def test_multiply3(self):
        p1 = Polynomial([0, 1], 3)
        p2 = Polynomial([1, 1], 3)
        res = p1 * p2
        self.assertEqual('x + x^2', str(res))

    def test_multiply4(self):
        p1 = Polynomial([1, 0, 1, 1], 3)
        p2 = Polynomial([1, 1], 3)
        res = p1 * p2
        self.assertEqual('1 + x + x^2 + 2x^3 + x^4', str(res))

    def test_multiply5(self):
        p1 = Polynomial([1, 0, 1, 1], 3)
        p2 = Polynomial([1, 1], 3)
        res = p1 * p2 * 2
        self.assertEqual('2 + 2x + 2x^2 + x^3 + 2x^4', str(res))

if __name__ == '__main__':
    unittest.main()
