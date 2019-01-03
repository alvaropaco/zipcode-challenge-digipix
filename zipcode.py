import os
import json

from nameko.rpc import rpc, RpcProxy
import requests

default_baseurl = "https://service-homolog.digipix.com.br/v0b"
baseurl = os.getenv('BASEURL', default_baseurl)
headers = {"Authorization": "Bearer {}".format(os.getenv('JWT'))}
print(headers)


def getResponse(qstring):
    resp = requests.request('GET', qstring, headers=headers)

    return resp.json()


class ZipCodeService:
    name = "zipcode"

    zipcode_rpc = RpcProxy('zipcodeservice')

    @rpc
    def getZipcode(self, zipcode):
        endpoint = '/shipments/zipcode/'
        try:
            if zipcode is None:
                raise ValueError("Missing ZipCode")
            qstring = (baseurl + endpoint + zipcode)

            return getResponse(qstring)
        except ValueError:
            print ValueError
            sys.exit()
