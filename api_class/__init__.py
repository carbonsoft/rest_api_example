# -*- coding: utf-8 -*-
import json
import urllib
import urllib2


class Api(object):
    def __init__(self, srv_address='http://195.64.222.86:8087'):
        self.srv_address = srv_address

    def call_api(self, model, params):
        encoded_params = urllib.urlencode(params)
        api_url = "{0}/rest_api/v2/{1}/".format(self.srv_address, model)
        print(api_url)
        print('pamams: {0}'.format(encoded_params))
        req = urllib2.Request(api_url, encoded_params)
        response = urllib2.urlopen(req)
        result = response.read()
        obj= json.loads(result)
        if obj.get('error'):
            print(u'Произошла ошибка на стороне биллинга:{0}'.format(obj['error']))
        return obj