import os
import json

from nameko.rpc import rpc, RpcProxy
import requests 

default_baseurl = "https://service-homolog.digipix.com.br/v0b"
baseurl = os.getenv('BASEURL', default_baseurl)

def getResponse(self, qstring):
    resp = requests.get(qstring)
    
    return json.dumps({
        "state": "string",
        "city": "string",
        "neighborhood": "string",
        "street": "string",
        "ibge": "string",
        "additional_info": "string",
        "bairro": "string"
    })


class ZipCodeService:
    name = "zipcode"

    zipcode_rpc = RpcProxy('zipcodeservice')

    @rpc
    def getZipcode(self, zipcode):
        endpoint = '/shipments/zipcode/'
        try:
            if zipcode == None:
                raise ValueError("Missing ZipCode")
            qstring = (baseurl + endpoint + zipcode)
            return getResponse(self, qstring)
        except ValueError:
            print ValueError
            sys.exit()
