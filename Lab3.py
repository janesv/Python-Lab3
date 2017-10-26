import urllib.request
import re
import html2text
import pandas as pd

site = urllib.request.urlopen('https://www.accuweather.com/ru/world-weather')
html = site.read().decode('utf8')

city = re.findall(r'<a href="https://www.accuweather.com/ru/.*/\d+">[A-Za-z ]+</a>', html)
temperature = re.findall(r'<span>(\d+).*</span>', html)

h = html2text.HTML2Text()
h.ignore_links = True

i = 0
cityArray = []
temperatureArray = []
for item in city:
    cityArray.append(h.handle(item))
    temperatureArray.append(h.handle(temperature[i]))
    i += 1

ca = []
ta = []
for i in cityArray:
    ca.append(i.rstrip())
for i in temperatureArray:
    ta.append(i.rstrip())

print(ca, "\n", ta)

result = pd.DataFrame(data={'City:': ca, 'Temperature:': ta})
result.to_csv('weather.csv', index=False)

