class Post:

    POSTS = [
        {'id':1,'title':'frist post','content':'this my frist post'},
        {'id':2,'title':'second post','content':'this my second post'},
        {'id':3,'title':'third post','content':'this my third post'},
    ]
   
    @classmethod
    def all(cls):
        return cls.POSTS

    @classmethod
    def find(cls,id):
        try:
            return cls.POSTS[int(id)-1]
        except:
            return None
