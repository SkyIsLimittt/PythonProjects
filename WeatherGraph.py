import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.weersverwachting.nl/wereldweer/europa/nederland/amsterdam/5575')
soup = BeautifulSoup(page.content, 'html.parser')

list_of_divs = soup.find_all('div', class_='max')
print(list_of_divs)
ydata = []

for index in range(len(list_of_divs)):
    ydata.append(int(list_of_divs[index].get_text()[:-2]))


f, ax = plt.subplots(1)
xdata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
ax.plot(xdata, ydata)
plt.xlabel('Days')
plt.ylabel('Temprature (°C)')
plt.xlim(1)
plt.show(f)

