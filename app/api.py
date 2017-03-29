from flask import render_template
from flask_peewee.rest import Authentication
from flask_peewee.rest import RestAPI
from flask_peewee.rest import RestResource

from app import app
from models import Comment


auth = Authentication(protected_methods=['PUT', 'DELETE'])
api = RestAPI(app, default_auth=auth)

class CommentResource(RestResource):
    fields = ('id', 'content', 'timestamp')
    paginate_by = 30

    def get_query(self):
        return Comment.public()

    def prepare_data(self, obj, data):
        data['rendered'] = render_template('comment.html', comment=obj)
        return data


api.register(Comment, CommentResource)
