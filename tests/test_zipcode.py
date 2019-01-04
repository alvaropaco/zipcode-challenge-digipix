# -*- coding: utf-8 -*-
import unittest
import requests
import json

from flask_script import Manager, Server
#from jsonschema import validate

from ..api import app

responde_schema = {
    "type": "object",
    "properties": {
         {
            "state": {"type": "string"},
            "city": {"type": "string"},
            "neighborhood": {"type": "string"},
            "street": {"type": "string"},
            "ibge": {"type": "string"},
            "additional_info": {"type": "string"},
            "bairro": {"type": "string"}
        }
    }
}


class ZipCodeTestCase(unittest.TestCase):
    """This class represents the zipcode test case"""

    @pytest.mark.parametrize("runserver")
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app.test_client()
        manager = Manager(app, with_default_commands=False)
        manager.run()

    def test_zipcode_happy_flow(self):
        res = self.app.get('http://127.0.0.1:5000/zipcode?code=13560044')
        
        assert resp.city == "São Carlos"
        assert resp.street == "Ruth Bloen Souto"

    def tearDown(self):
        """teardown all initialized variables."""


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
