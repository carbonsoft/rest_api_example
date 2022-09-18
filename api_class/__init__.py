import json
import urllib
import requests


class Api(object):
    def __init__(self, srv_address='http://***:8082'):
        self.srv_address = srv_address

    def call_api(self, model, params):
        api_url = "{0}/rest_api/v2/{1}/".format(self.srv_address, model)
        req = requests.post(url=api_url, data=params)
        obj= req.json()
        if obj.get('error'):
            print(u'Произошла ошибка на стороне биллинга:{0}'.format(obj['error']))
        return obj
