import sqlite3
from flask import Flask, render_template, request, make_responce, current_app as app
from .models import db, User
app = Flask(__name__)

conn = sqlite3.connect('Music_data.sqlite')

conn.execute('Create a table for the song the user decides to input (Song Release date,artest name,song title)')


conn.execute('insert year of Release', ("2015") )
conn.execute('insert artest data', ("The Oh hellos") )
conn.execute('insert the song data', ("Soldier, Poet, King") )
conn.commit()
conn.close()
for row in conn.execute('select * From Music data'):
    print(row)


    def init_app():
        """Construct the core application."""
        app = Flask(__name__, instance_relative_config=False)
        app.config.from_object('config.Config')

        db.init_app(app)

        with app.app_context():
            from . import routes  # Import routes
            db.create_all()  # Create sql tables for our data models


@app.route('/', methods=['GET'])
def records():
    """Create a user via query string parameters."""
    song = request.args.get('Song')
    artist = request.args.get('artist')
    if song and artist:
        existing_user = User.query.filter(
            User.username == song or User.email == artist
        ).first()
        if existing_user:
            return make_response(
                f'{artist} ({song}) already created!'
            )
        new_user = User(
            Song=song,
            Artist=artist,
        )
       # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        redirect(url_for('user_records'))
    return render_template(
        'index.jinja2',
        users=User.query.all(),
        title="Show Users"
    )
@app.route('/save',methods=['POST'])
def save_data(data):
    data = request.get_json()
    print(data)
    value = "{{Music.data}}"
    name = "Music.db"
    value = request.form.get ('Music.db')
    return 'saved'

def music_data(self):
    Music_Stored = db.Music_Stored('dataStored')
    self.assertEqual('here we are', Music_Stored)

