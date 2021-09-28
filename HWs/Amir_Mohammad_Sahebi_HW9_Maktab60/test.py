from datetime import datetime, timedelta
import one
import unittest

class testing(unittest.TestCase):

    def setUp(self):
        self.credit=one.Creditcard(300)
        self.timecredit=one.Timecreditcard(400)
        self.single=one.Singlecard()
    
    def test_use(self):
        self.now1=self.credit.credit()
        self.credit.use()
        self.later1=self.credit.credit()
        self.assertEqual(self.now1 - self.later1, 100)
        
        self.now2=self.timecredit.credit()
        self.timecredit.use()
        self.later2=self.timecredit.credit()
        self.assertEqual(self.now2 - self.later2, 100)

        self.now3=self.single.credit()
        self.single.use()
        self.later3=self.single.credit()
        self.assertEqual(self.now3 - self.later3, 100)

    def test_efficiency(self):
        self.assertEqual(self.credit.use(),True)
        self.credit.credit=0
        self.assertEqual(self.credit.use(),False)

        self.assertEqual(self.timecredit.use(),True)
        self.timecredit.credit=0
        self.assertEqual(self.timecredit.use(),False)

        self.assertEqual(self.single.use(),False)

    def test_charge(self):
        self.now11=self.credit.credit()
        self.credit.charge(200)
        self.later11=self.credit.credit()
        self.assertEqual(self.later11 - self.now11, 200)
        
        self.now22=self.credit.credit()
        self.credit.charge(200)
        self.later22=self.credit.credit()
        self.assertEqual(self.later22 - self.now22, 200)

        self.now33=self.credit.credit()
        self.credit.charge(200)
        self.later33=self.credit.credit()
        self.assertEqual(self.later33 - self.now33, 200)

    def test_exp(self):
        self.assertEqual(self.timecredit.checkexp(datetime.today()+timedelta(days=31)),False)
        self.timecredit.renew()
        self.assertEqual(self.timecredit.checkexp(datetime.today()+timedelta(days=31)),True)


        

