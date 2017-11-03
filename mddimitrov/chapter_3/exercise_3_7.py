"""
Exercise 3.7
Test module
"""
import unittest


# pylint: disable=R0904
class Exercise37(unittest.TestCase):
    """
    i1 = 2
    i2 = 5
    i3 = -3
    d1 = 2.0
    d2 = 5.0
    d3 = -0.5
    Evaluate each of the following Python expressions.
    (a) i1 + i2
    (b) i1 / i2
    (c) i1 // i2
    (d) i2 / i1
    (e) i2 // i1
    (f) i1 * i3
    (g) d1 + d2
    (h) d1 / d2
    (i) d2 / d1
    (j) d3 * d1
    (k) d1 + i2
    (l) i1 / d2
    (m) d2 / i1
    (n) i2 / d1
    (o) i1/i2*d1
    (p) d1*i1/i2
    (q) d1/d2*i1
    (r) i1*d1/d2
    (s) i2/i1*d1
    (t) d1*i2/i1
    (u) d2/d1*i1
    (v) i1*d2/d1.
    """

    def setUp(self):
        """
        Setup six variables:
        i1, i2, i3
        d1, d2, d3
        Prepend my_ to keep PYLint happy.
        """
        self.my_i1, self.my_i2, self.my_i3 = 2, 5, -3
        self.my_d1, self.my_d2, self.my_d3 = 2.0, 5.0, -0.5

    def test_case_a(self):
        """Assert i1 + i2"""
        self.assertEqual(7, self.my_i1 + self.my_i2)

    def test_case_b(self):
        """Assert i1 / i2"""
        self.assertEqual(0.4, self.my_i1 / self.my_i2)

    def test_case_c(self):
        "Assert i1 // i2"""
        self.assertEqual(0, self.my_i1 // self.my_i2)

    def test_case_d(self):
        """Assert i2 / i1"""
        self.assertEqual(2.5, self.my_i2 / self.my_i1)

    def test_case_e(self):
        """Assert i2 // i1"""
        self.assertEqual(2, self.my_i2 // self.my_i1)

    def test_case_f(self):
        """Assert i1 * i3"""
        self.assertEqual(-6, self.my_i1 * self.my_i3)

    def test_case_g(self):
        """Assert d1 + d2"""
        self.assertEqual(7.0, self.my_d1 + self.my_d2)

    def test_case_h(self):
        """Assert d1 / d2"""
        self.assertEqual(0.4, self.my_d1 / self.my_d2)

    def test_case_i(self):
        """Assert d2 / d1"""
        self.assertEqual(2.5, self.my_d2 / self.my_d1)

    def test_case_j(self):
        """Assert d3 * d1"""
        self.assertEqual(-1.0, self.my_d3 * self.my_d1)

    def test_case_k(self):
        """Assert d1 + i2"""
        self.assertEqual(7.0, self.my_d1 + self.my_i2)

    def test_case_l(self):
        """Assert i1 / d2"""
        self.assertEqual(0.4, self.my_i1 / self.my_d2)

    def test_case_m(self):
        """Assert d2 / i1"""
        self.assertEqual(2.5, self.my_d2 / self.my_i1)

    def test_case_n(self):
        """Assert i2 / d1"""
        self.assertEqual(2.5, self.my_i2 / self.my_d1)

    def test_case_o(self):
        """Assert i1 / i2 * d1"""
        self.assertEqual(0.8, self.my_i1 / self.my_i2 * self.my_d1)

    def test_case_p(self):
        """Assert d1 * i1 / i2"""
        self.assertEqual(0.8, self.my_d1 * self.my_i1 / self.my_i2)

    def test_case_q(self):
        """Assert d1 / d2 * i1"""
        self.assertEqual(0.8, self.my_d1 / self.my_d2 * self.my_i1)

    def test_case_r(self):
        """Assert i1 * d1 / d2"""
        self.assertEqual(0.8, self.my_i1 * self.my_d1 / self.my_d2)

    def test_case_s(self):
        """Assert i2 / i1 * d1"""
        self.assertEqual(5.0, self.my_i2 / self.my_i1 * self.my_d1)

    def test_case_t(self):
        """Assert d1 * i2 / i1"""
        self.assertEqual(5.0, self.my_d1 * self.my_i2 / self.my_i1)

    def test_case_u(self):
        """Assert d2 / d1 * i1"""
        self.assertEqual(5.0, self.my_d2 / self.my_d1 * self.my_i1)

    def test_case_v(self):
        """Assert i1 * d2 / d1"""
        self.assertEqual(5.0, self.my_i1 * self.my_d2 / self.my_d1)


if __name__ == '__main__':
    unittest.main()
