#!/usr/bin/env python3
import requests
import json
from datetime import datetime
from datetime import date

headers = {
    'authority': 'www.howmanypeopleareinspacerightnow.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.howmanypeopleareinspacerightnow.com/',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '__utma=196977205.895547898.1619828933.1619828933.1619828933.1; __utmc=196977205; __utmz=196977205.1619828933.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=196977205.4.10.1619828933',
}

response = requests.get('https://www.howmanypeopleareinspacerightnow.com/peopleinspace.json', headers=headers).json()

widget = {
    "icon": "/home/pmakhov/.config/awesome/noobie-plugins/people-in-space/icons/rocket-2-fill.svg",
    "text": response["number"]
}

items = []

response["people"].sort(key=lambda x: x["country"])

current_country = ""
for person in response["people"]:
    if current_country != person["country"]:
        if current_country != "":
            items.append({"title": "-"})
        items.append({
            "header": "true",
            "title": person["country"]
        })

    launchdate = datetime.strptime(person["launchdate"], '%Y-%m-%d').date()
    today = date.today()
    days_in_space = today - launchdate

    items.append({
        "icon": person["biophoto"],
        "icon_size": 48,
        "icon_fallback": "/home/pmakhov/.config/awesome/noobie-plugins/people-in-space/icons/astro_helmet.png",
        "title": "<b>" + person["name"] + "</b>",
        "subtitle": person["title"] + " / " + str(days_in_space.days) + "days",
        "onclick": "xdg-open " + person["biolink"]
    })
    current_country = person["country"]

result = {
    "widget": widget,
    "menu": {"items": items}
}

print(json.dumps(result))
