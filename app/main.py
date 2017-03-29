from app import app
from models import Comment
import views
from api import api

api.setup()

if __name__ == '__main__':
    Comment.create_table(True)
    app.run()
