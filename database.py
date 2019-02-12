import pymongo

class Database(object):
    URI = "mongodb://localhost:27017"
    DATABASE = None
    
    @classmethod
    def initialize(cls):
        client = pymongo.MongoClient(cls.URI)
        cls.DATABASE = client['test']

    @classmethod
    def insert(cls, collection, item):
        cls.DATABASE[collection].insert_one(item)

    @classmethod
    def find(cls, collection, query):
        return cls.DATABASE[collection].find(query)

    @classmethod
    def find_one(cls, collection, query):
        return cls.DATABASE[collection].find_one(query)

