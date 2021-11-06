import time
import json
import datetime

from pymongo import MongoClient
from pymongo import ASCENDING

from settings import MONGO_HOST

class Database:

    def initialize(self):
        try:
            mongo_client = MongoClient(MONGO_HOST, 27017)

            self.database = mongo_client.book_db

            self.book_collection = self.database.book_collection

            self.user_collection= self.database.user_collection

            self.comment_collection= self.database.comment_collection

            # todo define collections here
            
        except:
            print("Mongo Initialization Failed. Passing")
            pass

    def __init__(self):
        self.initialize()

