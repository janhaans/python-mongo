from models.post import Post
from database import Database

Database.initialize()

post1 = Post(title="Title Post 1",
            content="Content Post 1",
            author="Author Post1",
            id=1,
            blog_id=1)

post1.save_post()

print('First post {}'.format(Post.get_post(1)))

post2 = Post(title="Title Post 2",
            content="Content Post 2",
            author="Author Post2",
            id=2,
            blog_id=1)

post2.save_post()

for post in Post.get_blog_posts(1):
    print('Post in blog 1: author = {0}; title = {1}; date created  = {2}'.format(post.author, 
                                                                                post.title,
                                                                                post.time_created.strftime('%d %b %Y: %H:%M')))

