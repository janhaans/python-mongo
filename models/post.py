from datetime import datetime
from database import Database
import uuid

class Post(object):

    def __init__(self, title, content, author, blog_id, id=None, time_created = datetime.utcnow()):
        self.title = title
        self.content = content
        self.author = author
        self.blog_id = blog_id
        self.id = uuid.uuid4().hex if id is None else id
        self.time_created = time_created

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'time_created': self.time_created
        }

    def save_post(self):
        Database.insert(collection='posts',
                        item=self.json())
    
    @classmethod
    def get_post(cls, id):
        post = Database.find_one(collection='posts', query={'id': id})
        return cls( id=post['id'],
                    blog_id=post['blog_id'],
                    title=post['title'],
                    author=post['author'],
                    content=post['content'],
                    time_created=post['time_created']
                )
    
    @classmethod
    def get_blog_posts(cls, blog_id):
        return [cls(id=post['id'],
                    blog_id=post['blog_id'],
                    title=post['title'],
                    author=post['author'],
                    content=post['content'],
                    time_created=post['time_created']
                    ) for post in Database.find(collection='posts', query={'blog_id': blog_id})]


