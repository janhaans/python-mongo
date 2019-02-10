from datetime import datetime
from database import Database
import uuid

class Post(object):

    def __init__(self, title, content, author, time_created = None, id = None):
        self.title = title
        self.content = content
        self.author = author
        self.time_created = time_created if time_created is not None else datetime.utcnow().strftime("%d-%m-%Y:%H-%M")
        self.id = id if id is not None else uuid.uuid4()

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'time_created': self.time_created
        }

    def save(self):
        Database.save(collection='posts',
                        item=self.json())

