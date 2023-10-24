# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yandex_reviews_parser', 'yandex_reviews_parser.tests']

package_data = \
{'': ['*']}

install_requires = \
['undetected-chromedriver>=3.5.0,<4.0.0']

setup_kwargs = {
    'name': 'yandex-reviews-parser',
    'version': '0.1.4',
    'description': 'Python yandex company reviews parser',
    'long_description': '# Парсер отзывов c Yandex Карт\n\nСкрипт парсит отзывы с Yandex Карт<br>\nДля парсинга необходимо указать id компании в начале обработки скрипта\n\nПо результатам выполнения, возвращается объект, в котором:\n```json\n{\n  "company_info": {\n    "name": "Дилерский центр Hyundai",\n    "rating": 5.0,\n    "count_rating": 380,\n    "stars": 5\n  },\n  "company_reviews": [\n    {\n      "name": "Иван Иванов",\n      "icon_href": "https://avatars.mds.yandex.net/get-yapic/51381/cs8Tx0sigtfayYhRQBDJkavzJU-1/islands-68",\n      "date": 1681992580.04,\n      "text": "Выражаю огромную благодарность работникам ",\n      "stars": 5,\n      "answer": "Владимир, Благодарим Вас, что уделили время и оставили приятный отзыв о нашем автосервисе! Мы для Вас приготовили подарок в следующий визит."\n    },\n    {\n      "name": "Иван Иванов",\n      "icon_href": "https://avatars.mds.yandex.net/get-yapic/51381/cs8Tx0sigtfayYhRQBDJkavzJU-1/islands-68",\n      "date": 1681992580.04,\n      "text": "Выражаю огромную благодарность работникам ",\n      "stars": 5,\n      "answer": null\n    }\n  ]\n}\n```\n\n\nНеобходимо установить библиотеку<br>\n```shell\npip install yandex-reviews-parser\n```\n\n```python\nfrom yandex_reviews_parser.utils import YandexParser\nid_ya = 1234 #ID Компании Yandex\nparser = YandexParser(id_ya)\n\nall_data = parser.parse() #Получаем все данные\ncompany = parser.parse(type_parse=\'company\') #Получаем данные по компании\nreviews = parser.parse(type_parse=\'company\') #Получаем список отзывов\n```',
    'author': 'Daniil',
    'author_email': 'danil16m@mail.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/useless-apple/yandex_reviews-parser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
