import os
import app
import unittest
import tempfile
import json

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def tearDown(self):
    	pass

    def test_empty_db(self):
        r = self.app.get('/')
        r = r.get_data()
        r = json.loads(r)        
        assert 'result' in r
        assert r['result'] == 'success'

if __name__ == '__main__':
    unittest.main()