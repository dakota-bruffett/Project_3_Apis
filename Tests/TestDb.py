import unittest
from database import db

class Testdatabase(unittest.TestCase):
    def test_Music_Data(self):
        Music_Stored = db.Music_Stored('dataStored')
        self.assertEqual('here we are', Music_Stored)