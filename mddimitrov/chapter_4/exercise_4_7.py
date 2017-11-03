"""
Exercise 4.7
Test module
"""
import unittest


# pylint: disable=R0904
class Exercise47(unittest.TestCase):
    """
    x, y = 3, 5
    b1, b2, b3, b4 = True, False, x == 3, y < 3
    evaluate the following Boolean expressions:
        (a) b3
        (b) b4
        (c) not b1
        (d) not b2
        (e) not b3
        (f) not b4
        (g) b1 and b2
        (h) b1 or b2
        (i) b1 and b3
        (j) b1 or b3
        (k) b1 and b4
        (l) b1 or b4
        (m) b2 and b3
        (n) b2 or b3
        (o) b1 and b2 or b3
        (p) b1 or b2 and b3
        (q) b1 and b2 and b3
        (r) b1 or b2 or b3
        (s) not b1 and b2 and b3
        (t) not b1 or b2 or b3
        (u) not (b1 and b2 and b3)
        (v) not (b1 or b2 or b3)
        (w) not b1 and not b2 and not b3
        (x) not b1 or not b2 or not b3
        (y) not (not b1 and not b2 and not b3)
        (z) not (not b1 or not b2 or not b3).
    """

    def setUp(self):
        """
        Setup six variables - my_x, my_y,
        my_b1, my_b2, my_b3, my_b4.
        Keep PYLint happy by prepending my_ in variables.
        """
        self.my_x, self.my_y = 3, 5
        self.my_b1, self.my_b2 = True, False
        self.my_b3, self.my_b4 = self.my_x == 3, self.my_y < 3

    def test_case_a(self):
        """Assert b3"""
        self.assertTrue(self.my_b3)

    def test_case_b(self):
        """Assert b4"""
        self.assertFalse(self.my_b4)

    def test_case_c(self):
        "Assert not b1"""
        self.assertFalse(not self.my_b1)

    def test_case_d(self):
        """Assert not b2"""
        self.assertTrue(not self.my_b2)

    def test_case_e(self):
        """Assert not b3"""
        self.assertFalse(not self.my_b3)

    def test_case_f(self):
        """Assert not b4"""
        self.assertTrue(not self.my_b4)

    def test_case_g(self):
        """Assert b1 and b2"""
        self.assertFalse(self.my_b1 and self.my_b2)

    def test_case_h(self):
        """Assert b1 or b2"""
        self.assertTrue(self.my_b1 or self.my_b2)

    def test_case_i(self):
        """Assert b1 and b3"""
        self.assertTrue(self.my_b1 and self.my_b3)

    def test_case_j(self):
        """Assert b1 or b3"""
        self.assertTrue(self.my_b1 or self.my_b3)

    def test_case_k(self):
        """Assert b1 and b4"""
        self.assertFalse(self.my_b1 and self.my_b4)

    def test_case_l(self):
        """Assert b1 or b4"""
        self.assertTrue(self.my_b1 or self.my_b4)

    def test_case_m(self):
        """Assert b2 and b3"""
        self.assertFalse(self.my_b2 and self.my_b3)

    def test_case_n(self):
        """Assert b2 or b3"""
        self.assertTrue(self.my_b2 or self.my_b3)

    def test_case_o(self):
        """Assert b1 and b2 or b3"""
        self.assertTrue(self.my_b1 and self.my_b2 or self.my_b3)

    def test_case_p(self):
        """Assert b1 or b2 and b3"""
        self.assertTrue(self.my_b1 or self.my_b2 and self.my_b3)

    def test_case_q(self):
        """Assert b1 and b2 and b3"""
        self.assertFalse(self.my_b1 and self.my_b2 and self.my_b3)

    def test_case_r(self):
        """Assert b1 or b2 or b3"""
        self.assertTrue(self.my_b1 or self.my_b2 or self.my_b3)

    def test_case_s(self):
        """Assert not b1 and b2 and b3"""
        self.assertFalse(not self.my_b1 and self.my_b2 and self.my_b3)

    def test_case_t(self):
        """Assert not b1 or b2 or b3"""
        self.assertTrue(not self.my_b1 or self.my_b2 or self.my_b3)

    def test_case_u(self):
        """Assert not (b1 and b2 and b3)"""
        self.assertTrue(not (self.my_b1 and self.my_b2 and self.my_b3))

    def test_case_v(self):
        """Assert not (b1 or b2 or b3)"""
        self.assertFalse(not (self.my_b1 or self.my_b2 or self.my_b3))

    def test_case_w(self):
        """Assert not b1 and not b2 and not b3)"""
        self.assertFalse(not self.my_b1 and not self.my_b2 and not self.my_b3)

    def test_case_x(self):
        """Assert not b1 or not b2 or not b3)"""
        self.assertTrue(not self.my_b1 or not self.my_b2 or not self.my_b3)

    def test_case_y(self):
        """Assert not (not b1 and not b2 and not b3)"""
        self.assertTrue(
            not (not self.my_b1 and not self.my_b2 and not self.my_b3))

    def test_case_z(self):
        """Assert not (not b1 or not b2 or not b3))"""
        self.assertFalse(
            not (not self.my_b1 or not self.my_b2 or not self.my_b3))


if __name__ == '__main__':
    unittest.main()
