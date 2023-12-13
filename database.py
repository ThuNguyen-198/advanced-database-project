from pymongo import MongoClient
from pymongo.server_api import ServerApi

from bson.objectid import ObjectId

# uri = "mongodb+srv://dorothy:bark-bark@example-cluster.xrbmras.mongodb.net/?retryWrites=true&w=majority"
# uri = 'mongodb+srv://thunguyen:UyT78OAawkwlHJ0I@shopping.qm9o5yk.mongodb.net/?retryWrites=true&w=majority'
# node.js:
# uri = 'mongodb+srv://thunguyen:UyT78OAawkwlHJ0I@shopping.qm9o5yk.mongodb.net/?retryWrites=true&w=majority'
uri = "mongodb://localhost:27017"

# Create a new client and connect to the server

client = MongoClient(uri)
# client = MongoClient(uri, server_api=ServerApi('1'))
movies_rental_record_db = client.smovies_rental_record_db

def setup_database():
    # ----------setup Rental Record collection---------------
    movies_rental_record_db.drop_collection(movies_rental_record_db.rental_collection)
    rental_collection = movies_rental_record_db.rental_collection
    for item in [
        {"fName": "Hermione",
         "lName": "Granger",
         "movie_title": "I Am Legend",
         "date_borrow": "December 2, 2023",
         "due_date": "January 20, 2024"
         },
        {"fName": "Ron",
         "lName": "Weasley",
         "movie_title": "Avatar",
         "date_borrow": "September 2, 2023",
         "due_date": "November 20, 2023"
         }
    ]:
        rental_collection.insert_one({"fName":item['fName'], 'lName':item['lName'], 'movie_title':item['movie_title'], 'date_borrow':item['date_borrow'], 'due_date':item['due_date']})

    # ----------setup Movies List collection---------------
    movies_rental_record_db.drop_collection(movies_rental_record_db.movies_collection)
    movies_collection = movies_rental_record_db.movies_collection
    for item in [
        {"title": "Avatar",
         "genre": "action",
         "year": 2009,
         "rated": 9.7,
         "runtime": "180 mins"
         },
        {"title": "I Am Legend",
         "genre": "drama",
         "year": 2007,
         "rated": 9.2,
         "runtime": "120 mins"
         }
    ]:
        movies_collection.insert_one({"title":item['title'], 'genre':item['genre'], 'year':item['year'], 'rated':item['rated'], 'runtime':item['runtime']})
# ---------------CRUD Operation for rental---------------------
def get_items(id=None):
    rental_collection = movies_rental_record_db.rental_collection
    if id == None:
        items = rental_collection.find({})
    else:
        items = rental_collection.find({"_id":ObjectId(id)})
    items = list(items)
    for item in items:
        item["id"] = str(item["_id"])
    return items


def add_item(item):
    rental_collection = movies_rental_record_db.rental_collection
    rental_collection.insert_one(item)

def delete_item(id):
    rental_collection = movies_rental_record_db.rental_collection
    rental_collection.delete_one({"_id":ObjectId(id)})

def update_item(id, fName, lName, movie_title, date_borrow, due_date):
    rental_collection = movies_rental_record_db.rental_collection
    where = {"_id": ObjectId(id)}
    updates = {
        "$set": {
            "fName": fName,
            "lName": lName,
            "movie_title": movie_title,
            "date_borrow": date_borrow,
            "due_date": due_date
        }
    }
    rental_collection.update_one(where, updates)
# ---------------CRUD Operation for movies---------------------
def get_movies(id=None):
    movies_collection = movies_rental_record_db.movies_collection
    if id == None:
        items = movies_collection.find({})
    else:
        items = movies_collection.find({"_id":ObjectId(id)})
    items = list(items)
    for item in items:
        item["id"] = str(item["_id"])
    return items


def add_movie(item):
    movies_collection = movies_rental_record_db.movies_collection
    movies_collection.insert_one(item)

def delete_movie(id):
    movies_collection = movies_rental_record_db.movies_collection
    movies_collection.delete_one({"_id":ObjectId(id)})

def update_movie(id, title, genre, year, rated, runtime):
    movies_collection = movies_rental_record_db.movies_collection
    where = {"_id": ObjectId(id)}
    updates = {
        "$set": {
            "title": title,
            "genre": genre,
            "year": year,
            "rated": rated,
            "runtime": runtime
        }
    }
    movies_collection.update_one(where, updates)
# def test_setup_database():
#     print("testing setup_database()")
#     setup_database()
#     items = get_items()
#     assert len(items) == 2
#     fNames = [item['fName'] for item in items]
#     for fName in ['Thu', 'An']:
#         assert fName in fNames

# def test_get_items():
    # print("testing get_items()")
    # setup_database()
    # items = get_items()
#     assert type(items) is list
#     assert len(items) > 0
#     for item in items:
#         assert 'id' in item
#         assert type(item['id']) is str
#         assert 'description' in item
#         assert type(item['description']) is str
#     example_id = items[0]['id']
#     example_description = items[0]['description']
#     items = get_items(example_id)
#     assert len(items) == 1
#     assert example_id == items[0]['id']
#     assert example_description == items[0]['description']

# def test_add_item():
#     print("testing add_item()")
#     setup_database()
#     items = get_items()
#     original_length = len(items)
#     add_item("licorice")
#     items = get_items()
#     assert len(items) == original_length + 1
#     descriptions = [item['description'] for item in items]
#     assert "licorice" in descriptions


# def test_delete_item():
#     print("testing delete_item()")
#     setup_database()
#     items = get_items()
#     original_length = len(items)
#     deleted_description = items[1]['description']
#     deleted_id = items[1]['id']
#     delete_item(deleted_id)
#     items = get_items()
#     assert len(items) == original_length - 1
#     for item in items:
#         assert item['id'] != deleted_id
#         assert item['description'] != deleted_description

# def test_update_item():
#     print("testing update_item()")
#     setup_database()
#     items = get_items()
#     original_description = items[1]['description']
#     original_id = items[1]['id']
#     update_item(original_id,"new-description")
#     items = get_items()
#     found = False
#     for item in items:
#         if item['id'] == original_id:
#             assert item['description'] == "new-description"
#             found = True
#     assert found


if __name__ == "__main__":
    # test_setup_database()
    setup_database()
    get_items()
    get_movies()
    # test_get_items()
    # test_add_item()
    # test_delete_item()
    # test_update_item()
