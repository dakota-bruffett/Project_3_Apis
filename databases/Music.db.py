import sqlite3
from database import db
from flask import Flask, render_template, request
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

    print('Here its time to store your data')
    return 'Hi its loaded in all of your data usage.'
