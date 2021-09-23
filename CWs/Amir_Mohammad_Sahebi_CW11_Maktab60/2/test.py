import unittest
from bank import Account


class TestBankMethods(unittest.TestCase):

    def setUp(self):
        self.ali = Account("ali", 10000)
        self.mahdi = Account("mahdi", 20000)

    def test_transfer(self):
        self.assertEquals(self.ali.transfer(self.mahdi, 5000), True)

    def test_withdraw(self):
        self.assertEquals(self.ali.withdraw(700), True)

