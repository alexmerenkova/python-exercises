"""
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях
искусства, их работах, выставках.
В рамках данной задачи вам понадобятся сведения о деятелях искусства.

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения.
В случае если у художников одинаковый год рождения, выведите их имена
в лексикографическом порядке.

Примечание:
﻿В качестве имени художника используется параметр sortable_name в кодировке UTF-8.

Пример входных данных:
4d8b92b34eb68a1b2c0003f4
537def3c139b21353f0006a6
4e2ed576477cc70001006f99

Пример выходных данных:
Abbott Mary
Warhol Andy
Abbas Hamra
"""

import requests

def main():
    art_list = []
    token_url = 'https://api.artsy.net/api/tokens/xapp_token'
    params = {
        'client_id': 'c7d68bb29bebdccd736a',
        'client_secret': 'bfbd821fda5c275834532fcac47d0d86'
    }
    res = requests.post(token_url, params = params)
    token = res.json()['token']

    with open('dataset_artsy.txt') as f:
        for art_id in f.readlines():
            api_url = 'https://api.artsy.net/api/artists/{}'.format(art_id.strip())
            headers = {
                'X-Xapp-Token': token,
            }
            res = requests.get(api_url, headers = headers)
            data = res.json()
            art_list.append((data['sortable_name'], data['birthday']))

        art_list.sort(key=lambda x: (x[1], x[0]))
        for name, year in art_list:
            print(name)


if __name__ == "__main__":
    main()
