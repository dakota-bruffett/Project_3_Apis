import sqlite3

conn = sqlite3.connect('Music_data.sqlite')

conn.execute("DROP TABLE IF EXISTS ArtistInfo ")

conn.execute("CREATE TABLE ArtistInfo (Name text, Country text, City text, Gender text)")

# Insert the values into the table

conn.commit() # Commit all my changes

conn.close()
# for row in conn.execute('select * From Music data'):
#     print(row)


#     def init_app():
#         """Construct the core application."""
#         app = Flask(__name__, instance_relative_config=False)
#         app.config.from_object('config.Config')

#         db.init_app(app)

#         with app.app_context():
#             from . import routes  # Import routes
#             db.create_all()  # Create sql tables for our data models


# @app.route('/', methods=['GET'])
# def records():
#     """Create a user via query string parameters."""
#     username = request.args.get('user')
#     email = request.args.get('email')
#     if username and email:
#         existing_user = User.query.filter(
#             User.username == username or User.email == email
#         ).first()
#         if existing_user:
#             return make_response(
#                 f'{username} ({email}) already created!'
#             )
#         new_user = User(
#             username=username,
#             email=email,
#         )
#        # Create an instance of the User class
#         db.session.add(new_user)  # Adds new User record to database
#         db.session.commit()  # Commits all changes
#         redirect(url_for('user_records'))
#     return render_template(
#         'index.jinja2',
#         users=User.query.all(),
#         title="Show Users"
#     )
# @app.route('/save',methods=['POST'])
# def save_data(data):
#     data = request.get_json()
#     print(data)
#     value = "{{Music.data}}"
#     name = "Music.db"
#     value = request.form.get ('Music.db')
#     return 'saved'

# def music_data(self):
#     Music_Stored = db.Music_Stored('dataStored')
#     self.assertEqual('here we are', Music_Stored)

