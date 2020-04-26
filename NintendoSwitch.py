import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup

coolblue_render = requests.get('https://www.coolblue.nl/product/838252/nintendo-switch-2019-upgrade-rood-blauw.html')
intertoys_render = requests.get('https://www.intertoys.nl/shop/nl/intertoys/nintendo-switch-met-blauwe-en-rode-joy-con-controllers?')
gamemania_render = requests.get('https://www.gamemania.nl/Consoles/nintendo-switch/136442_nintendo-switch-neon-blue--red')
otto_render = requests.get('https://www.otto.nl/p/941579551/nintendo-switch-2019-nieuw-model/#?itemId=941579552&c=kinderen-highlights-speelgoed-voor-elke-prijs-speelgoed-van-10-tot-25-')

coolblue = BeautifulSoup(coolblue_render.content, 'html.parser')
intertoys = BeautifulSoup(intertoys_render.content, 'html.parser')
gamemania = BeautifulSoup(gamemania_render.content, 'html.parser')
otto = BeautifulSoup(otto_render.content, 'html.parser')

coolblue_price = coolblue.find('strong', class_='sales-price__current').get_text()[:3]
intertoys_price = intertoys.find_all('input', id='ProductInfoPrice_270505')[0]['value']
real_intertoys_price = str(intertoys_price)[6:][:3]
gamemania_price = gamemania.find('span', class_='currency').get_text()[2:]
otto_price = otto.find('div', class_='innerPrice').get_text()[31:][:3]

list = {
    "Coolblue": int(coolblue_price),
    "Intertoys": int(real_intertoys_price),
    "Gamemania": int(gamemania_price),
    "Otto": int(otto_price)
}
value = min(list, key=list.get)
print(f"You can buy the lowest priced Nintendo Switch at {value} for €{list.get(value)}.00")
