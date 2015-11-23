# -*- coding: utf-8 -*-
from api_class import Api
# Получаем всех абонентов из биллинга и выводим их имена
# Зададим метод и парамерты для метода
params = {
    'get_version': True,
}
client = Api()
# Вызовем апи для модели Abonents
res_dict = client.call_api(model='Version', params=params)
print('result: {0}'.format(res_dict['result']))
