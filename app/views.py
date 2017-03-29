from flask import abort, jsonify, render_template, request

from app import app
from models import Comment

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        if request.form.get('content'):
            # Create a new comment in the db.
            comment = Comment.create(content=request.form['content'])

            # Render a single comment and return the HTML.
            rendered = render_template('comment.html', comment=comment)
            comments = Comment.public().limit(25)
            return render_template('homepage.html', comments=comments)
            # return jsonify({'comment': rendered, 'success': True})

        # If content is empty.
        return jsonify({'success': False})

    comments = Comment.public().limit(25)
    return render_template('homepage.html', comments=comments)


@app.route('/archive/<int:pk>/', methods=['POST'])
def archive_comment(pk):
    try:
        comment = Comment.get(Comment.id == pk)
    except Comment.DoesNotExist:
        abort(404)
    comment.archived = True
    comment.archived_at = datetime.datetime.now()
    comment.save()
    return jsonify({'success': True})