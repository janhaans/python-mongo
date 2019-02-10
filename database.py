import pymongo

class Database(object):
    URI = "mongodb://localhost:27017"
    DATABASE = None
    
    @classmethod
    def initialize(cls):
        client = pymongo.MongoClient(cls.URI)
        cls.DATABASE = client['test']

    @classmethod
    def save(cls, collection, item):
        cls.DATABASE[collection].insert_one(item)

    
