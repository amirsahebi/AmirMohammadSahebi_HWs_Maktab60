import unittest
from book import *


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book_data1 = {'name': 'da',
                      'writer': 'ahmad',
                      'tags': ['tag1', 'tag2']
                      }

        self.book_id1=create_book(self.book_data1)
        self.assertEqual(db.book_collection.find_one({'_id':self.book_id1})['name'],self.book_data1['name'])

        self.book_data2 = {'name': 'jenayat',
                      'writer': 'ali',
                      'tags': ['tag1']
                      }
        
        self.book_id2=create_book(self.book_data2)
        self.assertEqual(db.book_collection.find_one({'_id':self.book_id2})['name'],self.book_data2['name'])


        self.book_data3 = {'name': 'gorg',
                      'writer': 'reza',
                      'tags': ['tag2']
                      }

        self.book_id3=create_book(self.book_data3)
        self.assertEqual(db.book_collection.find_one({'_id':self.book_id3})['name'],self.book_data3['name'])


        self.user_data1 = {'first_name': 'mostafa',
                      'last_name': 'rezaie',}

        self.user_id1=create_user(self.user_data1)
        self.assertEqual(db.user_collection.find_one({'_id':self.user_id1})['first_name'],self.user_data1['first_name'])


        self.user_data2 = {'first_name': 'hasan',
                      'last_name': 'bagheri',}

        self.user_id2=create_user(self.user_data2)
        self.assertEqual(db.user_collection.find_one({'_id':self.user_id2})['first_name'],self.user_data2['first_name'])


        self.user_data3 = {'first_name': 'karim',
                      'last_name': 'karimi',}

        self.user_id3=create_user(self.user_data3)
        self.assertEqual(db.user_collection.find_one({'_id':self.user_id3})['first_name'],self.user_data3['first_name'])

    def test_create(self):
        pass

    def test_create_like(self):
        likes=len(db.user_collection.find_one({'_id': self.user_id1},{'_id': 0,'likes':1})['likes'])
        create_like_book(self.book_id1,self.user_id1)
        self.assertEqual(len(db.user_collection.find_one({'_id': self.user_id1},{'_id': 0,'likes':1})['likes']),likes+1)


    def test_delete_like(self):
        create_like_book(self.book_id1,self.user_id1)
        likes=len(db.user_collection.find_one({'_id': self.user_id1},{'_id': 0,'likes':1})['likes'])
        delete_like_book(self.book_id1,self.user_id1)
        self.assertEqual(len(db.user_collection.find_one({'_id': self.user_id1},{'_id': 0,'likes':1})['likes']),likes-1)
        


    def test_create_comment(self):
        comment="Hello world!"
        create_comment_book(self.book_id1,self.user_id1,comment)
        self.assertEqual(db.book_collection.find({'_id': self.book_id1}, {'_id': 0, 'comments': 1})[0]['comments'][0]['comment'],comment)




unittest.main()