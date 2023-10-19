import unittest
from database import db


conn = sqlite3.connect('Music_Test.sqlite')

conn.execute('Create a table for the song the user decides to input (Song Release date,artest name,song title)')

for row in conn.execute('select * From Music data'):
    print(row)



class Testdatabase(unittest.TestCase):
    def test_Music_Data(self):
        Music_Stored = db.Music_Stored('dataStored.')
        self.assertEqual('here we are', Music_Stored)