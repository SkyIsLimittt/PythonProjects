import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.weersverwachting.nl/wereldweer/europa/nederland/amsterdam/5575')
soup = BeautifulSoup(page.content, 'html.parser') 

a = soup.find_all('div', class_='max')[0]
a1 = a.get_text()[:-2]

b = soup.find_all('div', class_='max')[1]
b1 = b.get_text()[:-2]

c = soup.find_all('div', class_='max')[2]
c1 = c.get_text()[:-2]

d = soup.find_all('div', class_='max')[3]
d1 = d.get_text()[:-2]

e = soup.find_all('div', class_='max')[4]
e1 = e.get_text()[:-2]

f = soup.find_all('div', class_='max')[5]
f1 = f.get_text()[:-2]

g = soup.find_all('div', class_='max')[6]
g1 = g.get_text()[:-2]

h = soup.find_all('div', class_='max')[7]
h1 = h.get_text()[:-2]

i = soup.find_all('div', class_='max')[8]
i1 = i.get_text()[:-2]

j = soup.find_all('div', class_='max')[9]
j1 = j.get_text()[:-2]

k = soup.find_all('div', class_='max')[10]
k1 = k.get_text()[:-2]

l = soup.find_all('div', class_='max')[11]
l1 = l.get_text()[:-2]
           
m = soup.find_all('div', class_='max')[12]
m1 = m.get_text()[:-2]

n = soup.find_all('div', class_='max')[13]
n1 = n.get_text()[:-2]

a2 =int(a1)
b2 =int(b1)
c2 =int(c1)
d2 =int(d1)
e2 =int(e1)
f2 =int(f1)
g2 =int(g1)
h2 =int(h1)
i2 =int(i1)
j2 =int(j1)
k2 =int(k1)
l2 =int(l1)
m2 =int(m1)
n2 =int(n1)

f, ax = plt.subplots(1)
xdata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
ydata = [a2, b2, c2, d2, e2, f2, g2, h2, i2, j2, k2, l2, m2, n2]
ax.plot(xdata, ydata)
plt.xlabel('Days')
plt.ylabel('Temprature (°C)')
plt.xlim(1)
plt.show(f)
