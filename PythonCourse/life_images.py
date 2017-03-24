"""
Живые картинки

Вам дана ссылка на HTML документ.
Посчитайте количество живых картинок в нем.

Живой картинкой назовем тег <img ... src="url" ... >, который отображается на
странице, ﻿в котором url ведет на страницу, при запросе которой сервер вернет
сообщение с status code равным 200 и заголовком Content-Type, начинающимся с
image (например image/png)

Пример живой картинки
<img src="https://stepic.org/media/attachments/lesson/25669/nya.png">

Sample Input:
https://stepic.org/media/attachments/lesson/25669/sample.html

Sample Output:
2
"""

import re
import requests

def getlist(url):
    pat = r'<img[^>]*? src="(.+?)"'
    res = requests.get(url)
    if res.status_code == requests.codes.ok:
        return re.findall(pat, res.text)
    return []


def check():
    check_img = 0
    url = input()
    linklist = getlist(url)
    for lnk in linklist:
        res = requests.get(lnk)
        if res.status_code == 200 and res.headers['content-type'].startswith('image/'):
            check_img += 1
    return check_img

if __name__ == "__main__":
    print(check())