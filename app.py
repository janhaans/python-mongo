from models.post import Post
from database import Database

Database.initialize()

post1 = Post(title="Title Post 1",
            content="Content Post 1",
            author="Author Post1")
post1.save()