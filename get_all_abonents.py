# -*- coding: utf-8 -*-
from api_class import Api
#Зададим метод и парамерты для метода
params = {
          'method1': 'objects.filter',
          'arg1': '{"is_folder":0}'
          }
client=Api()
#Вызовем апи для модели Abonents
res_dict = client.call_api(model='Abonents',params=params)
for row in res_dict['result']:
    print(row['fields']['name'])