import unittest

import app

class Test_Web_app(unittest.TestCase):
    def Test_Web_Home(self):
        with.app.app.Web_Client() as client:
            responce = client.get('/')
            self.assertEqual(200 , responce.status_code)

