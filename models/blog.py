from database import Database
import uuid

class Blog(object):

    def __init__(self, author, title, description, id=None):
        self.author = author,
        self.title = title,
        self.description = description,
        self.id = uuid.uuid4().hex if id is None else id

    def json(self):
        return {
            'id': self.id,
            'author': self.author,
            'title': self.title,
            'description': self.description
        }

    def save_blog(self):
        Database.DATABASE.insert(collection='blogs',
                                 item=self.json())
    
    @classmethod
    def get_blog(cls, blog_id):
        blog = Database(collection='blogs',
                        query={'id':blog_id})
        return cls(author=blog['author'],
                    title=blog['title]'],
                    description=blog['description'],
                    id=blog['id'])

    @staticmethod
    def get_posts(blog_id):
        return [Post(id=post['id'],
                    blog_id=post['blog_id'],
                    title=post['title'],
                    author=post['author'],
                    content=post['content'],
                    time_created=post['time_created']
                    ) for post in Database.find(collection='posts', query={'blog_id': blog_id})]

    
    def new_post(self):
        title = input('Title of new post: ')
        content = input('Content of new post: ')
        return Post(title=title,
                    content=content,
                    author=self.author,
                    blog_id=self.blog_id)
