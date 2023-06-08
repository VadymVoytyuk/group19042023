import json
from pprint import pprint



data = '{"\u0443\u0440\u043b \u0437 \u0432\u0456\u0440\u043d\u043e\u044e \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u043e\u044e": "https://upload.wikimedia.org/wikipedia/commons/1/19/Europ%C3%A4ischer_Ziesel_in_Hockstellung.jpg", "\u0443\u0440\u043b \u0437 \u043d\u0435\u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e\u044e \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u043e\u044e": "https://ichef.bbci.co.uk/news/800/cpsprodpb/6C7E/production/_98847772_60e395f3-f84e-4215-8626-0b977b85e838.jpg"}'
dict_from_json=json.loads(data)
pprint(dict_from_json)