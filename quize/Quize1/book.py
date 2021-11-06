from mongo_service import *
from bson.objectid import ObjectId

db = Database()


def create_book(book_data):

    try:
        book_data1 = {
            'name': book_data['name'],
            'writer': book_data['writer'],
            'tags': book_data['tags'],
            'likes': 0,
            'comments': []
        }
        book_entry = db.book_collection.insert_one(book_data1)
        return book_entry.inserted_id
    except:
        print("Error while creating:", book_data)


def create_user(user_data):

    try:
        user_data1= {
            'first_name': user_data['first_name'],
            'last_name': user_data['last_name'],
            'likes': [],
            'comments': []
        }
        user_entry = db.user_collection.insert_one(user_data1)
        return user_entry.inserted_id
    except:
        print("Error while creating:", user_data)


def create_like_book(book_id, user_id):  # uniqueness

    if book_id not in db.user_collection.find_one({'_id': user_id})['likes']:
        db.user_collection.update_one({'_id': user_id}, {'$push': {'likes': book_id}})
        db.book_collection.update_one({'_id': book_id}, {'$inc': {'likes': 1}})


def delete_like_book(book_id, user_id):

    if book_id in db.user_collection.find_one({'_id': user_id})['likes']:
        db.user_collection.update_one({'_id': user_id}, {'$pull': {'likes': book_id}})
        db.book_collection.update_one({'_id': book_id}, {'$inc': {'likes': -1}})


def create_comment_book(book_id, user_id, comment):

    db.user_collection.update_one({'_id': user_id}, {'$push': {'comments': {'book_id': book_id, 'comment': comment ,'date': datetime.datetime.now()}}})
    db.book_collection.update_one({'_id': book_id}, {'$push': {'comments': {'user_id': user_id, 'comment': comment ,'date': datetime.datetime.now()}}})


def get_all_books(tag=None):  # order by like count - include only comment count
    # if tag is not none filter by tag
    
    if tag is None:
        for book in db.book_collection.find({}, {'_id': 0, 'name': 1, 'likes': 1, 'comments': 1}).sort('likes', -1):
            print(book['name'], 'likes:', book['likes'], 'comments:', len(book['comments']))
    else:
        for book in db.book_collection.find({'tags': {"$in": [tag]}},{'_id': 0, 'name': 1, 'likes': 1, 'comments': 1}).sort('likes', -1):
            print(book['name'], 'likes:', book['likes'], 'comments:', len(book['comments']))


def get_all_book_comments(book_id, count, index):  # order by latest

    book=db.book_collection.find({'_id': book_id}, {'_id': 0, 'comments': 1}).sort('comments.date',-1)
    comments = book[0]['comments']
    for i in range(index-1,index+count-1):
        if i>=len(comments):
            break
        print(comments[i])



def get_all_user_liked_book(user_id):
    for liked_id in db.user_collection.find_one({'_id': user_id})['likes']:
        print(liked_id)


def get_all_user_liked_and_taked_comment_book(user_id):
    for liked_id in db.user_collection.find_one({'_id': user_id})['likes']:
        for comment in db.user_collection.find_one({'_id': user_id})['comments']:
            if comment['book_id'] == liked_id:
                print(db.book_collection.find_one({'_id': liked_id})['name'])
                break


def get_books_tag_count():
    # aggregation
    # {histoical: 33}
    for i in (db.book_collection.aggregate([
        {'$project': {'_id': 0, 'tags': 1}},
        {'$unwind': '$tags'},
        {'$group': {'_id': '$tags', 'count': {'$sum': 1}}}
    ])):
        print(i)