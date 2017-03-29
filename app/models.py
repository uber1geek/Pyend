import datetime
from flask import Markup
from markdown import markdown
from micawber import parse_html
from peewee import *
from app import db, oembed

class Comment(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    archived = BooleanField(default=False)

    class Meta:
        database = db

    def html(self):
        html = parse_html(
            markdown(self.content),
            oembed,
            maxwidth=300,
            urlize_all=True)
        return Markup(html)

    @classmethod
    def public(cls):
        return (Comment
                .select()
                .where(Comment.archived == False)
                .order_by(Comment.timestamp.desc()))