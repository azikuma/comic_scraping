import requests, os, time
from bs4 import BeautifulSoup
from urllib import parse

os.makedirs('images', exist_ok=True)
url = 'url'

htmls = []

soup = BeautifulSoup(requests.get(url).content, 'html.parser')
comics = soup.select_one('section#comics')

for link in comics.select('a'):
    if link.get('target') == '_blank':
        continue
    else:
        htmls.append(link.get('href'))

htmls.reverse()

base_url = 'base_url'
for html in range(len(htmls)):
    html_url = htmls[html]
    soup = BeautifulSoup(requests.get(html_url).content, 'html.parser')
    src = soup.select_one('p > img').get('src')
    img = base_url + src
    num_name = (str)(html + 1) + '.jpg'

    print(img)

print('Done!')
