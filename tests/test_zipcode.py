# -*- coding: utf-8 -*-
import unittest
import requests
from bson import json_util
import json
from jsonschema import validate

from ../zipcode import ZipCodeService
from nameko.testing.services import worker_factory

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

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app.test_client()

    def test_zipcode_happy_flow(self):
        # create worker with mock dependencies
        service = worker_factory(ZipCodeService)

        # add side effects to the mock proxy to the "maths" service
        resp = service.zipcode_rpc.getZipcode("13560044")
        
        assert resp.city == "São Carlos"
        assert resp.street == "Ruth Bloen Souto"

    def tearDown(self):
        """teardown all initialized variables."""


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
