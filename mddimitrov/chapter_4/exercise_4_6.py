"""
Exercise 4.6
Test module
"""
import unittest


class Exercise46(unittest.TestCase):
    """
    Exercise 4.6:
    x, y, z = 3, 5, 7
    evaluate the following Boolean expressions:
    (a) x == 3
    (b) x < y
    (c) x >= y
    (d) x <= y
    (e) x != y - 2
    (f) x < 10
    (g) x >= 0 and x < 10
    (h) x < 0 and x < 10
    (i) x >= 0 and x < 2
    (j) x < 0 or x < 10
    (k) x > 0 or x < 10
    (l) x < 0 or x > 10.
    """

    def setUp(self):
        """
        Setup three variables - my_x, my_y, my_z.
        Keep PYLint happy by prepending my_ in variables.
        """
        self.my_x, self.my_y, self.my_z = 3, 5, 7

    def test_case_a(self):
        """Assert x == 5."""
        self.assertTrue(self.my_x == 3)

    def test_case_b(self):
        """Assert x < y."""
        self.assertTrue(self.my_x < self.my_y)

    def test_case_c(self):
        "Assert x >= y."""
        self.assertFalse(self.my_x >= self.my_y)

    def test_case_d(self):
        """Assert x <= y."""
        self.assertTrue(self.my_x <= self.my_y)

    def test_case_e(self):
        """Assert x != y - 2."""
        self.assertFalse(self.my_x != self.my_y - 2)

    def test_case_f(self):
        """Assert x < 10."""
        self.assertTrue(self.my_x < 10)

    def test_case_g(self):
        """Assert x >= 0 and x < 10."""
        self.assertTrue(self.my_x >= 0 and self.my_x < 10)

    def test_case_h(self):
        """Assert x < 0 and x < 10."""
        self.assertFalse(self.my_x < 0 and self.my_x < 10)

    def test_case_i(self):
        """Assert x >= 0 and x < 2."""
        self.assertFalse(self.my_x >= 0 and self.my_x < 2)

    def test_case_j(self):
        """Assert x < 0 or x < 10."""
        self.assertTrue(self.my_x < 0 or self.my_x < 10)

    def test_case_k(self):
        """Assert x > 0 or x < 10."""
        self.assertTrue(self.my_x > 0 or self.my_x < 10)

    def test_case_l(self):
        """Assert x < 0 or x > 10."""
        self.assertFalse(self.my_x < 0 or self.my_x > 10)


if __name__ == '__main__':
    unittest.main()
