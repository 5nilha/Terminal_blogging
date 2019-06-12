import uuid
from database import Database
import datetime

class Post(object):

    def __init__(self, blog_id,  title, content, author, created_date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        if id is None:
            self.id = uuid.uuid4().hex
            # uuid.uuid4() generates a random uid. hex generates a 32 chars hexadecimal string
        else:
            self.id = id

    def save_to_mongo(self):
        Database.insert('posts', self.json())

    def json(self):
        return {
            'id' : self.id,
            'blog_id' : self.blog_id,
            'author' : self.author,
            'content' : self.content,
            'title' : self.title,
            'created_date' : self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        # return a specific post from a query of post id
        post_data = Database.find_one('posts', {'id' : id})
        return cls(blog_id=post_data["blog_id"], author=post_data["author"], content=post_data["content"], title=post_data["title"], created_date=post_data["created_date"])

    @staticmethod
    def from_blog(id):
        #Return a list of posts from a query of blog id
        return [post for post in Database.find('posts', {'blog_id' : id})]