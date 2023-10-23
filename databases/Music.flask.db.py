import sqlite3
from flask import Flask, render_template request, url_for, flash, redirect

app = Flask(__name__)
@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('create.html')
def get_db_connection():
    conn = sqlite3.connect('Music.db.py.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()

    return render_template('index.html', posts=posts)

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')

        elif not content:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)
@app.route('/save_bookmark', methods=['POST'])
def save_bookmark():
    save_request_data = request.form.to_dict()
    print(save_request_data)
    pretend_database.add_new_bookmark(save_request_data)
    all_bookmarks = pretend_database.get_all_bookmarks()
    return render_template('bookmarks.html', bookmarks=all_bookmarks)
