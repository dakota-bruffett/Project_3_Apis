import unittest

from apis import music_Api

class Api_Unit_Test(unittest.TestCase):
    def Music_api(self):
        fact = muisc_Api.get_a_Fact
        self.assertIsNotNone(fact)

