import unittest
import redis

from main1 import System, User


class TestManagerClass(unittest.TestCase):

    def setUp(self):
        self.manager = System("1234abcd")
        self.DB = redis.Redis(encoding="utf-8", decode_responses=True)

    def test_new_event(self):
        self.manager.add_event('1400/10/3', 'tehran', 50, 40, 30)
        self.assertEqual(self.DB.exists('event:1'), 1)




class TestCustomerClass(unittest.TestCase):

    def setUp(self):
        self.DB = redis.Redis(encoding='utf-8', decode_responses=True)

    def test_show_events(self):
        self.manager = System("1234abcd")
        self.manager.add_event('1400/4/5', 'tehran', 50,1000,50)
        self.manager.add_event('1400/4/6', 'esfahan', 40,2000,40)
        self.manager.add_event('1400/4/7', 'kerman', 60,3000,60)
        self.customer2 = User('ali', 745,"teacher")
        self.customer2.event_show()

    def test_buy(self):
        self.customer3 = User('mohammad', 343, 'student')
        self.customer3.buy_ticket(2, 2)
        self.assertEqual(self.DB.hget('event:2','left'), '2998')


        



unittest.main()