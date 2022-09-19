import mongoengine
from mongoengine import connect
from starlette.applications import Starlette
from starlette_admin.contrib.mongoengine import Admin, ModelView

connect("example")


class Post(mongoengine.Document):
    title = mongoengine.StringField(min_length=3, required=True)


class PostView(ModelView, document=Post):
    pass


app = Starlette()

admin = Admin()
admin.add_view(PostView)
admin.mount_to(app)
