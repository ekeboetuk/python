# %%
from urllib import request
from bs4 import BeautifulSoup

url_link = 'https://alansimpson.me/python/scrape_sample.html'
url_content = request.urlopen(url_link)
soup = BeautifulSoup(url_content, 'html5lib')
content = soup.article
link_list = []

for link in content.find_all('a'):
    url = link.get('href')
    link_list.append(url)

print()
for i,list in enumerate(link_list):
    print(f'{i:>4}', ' - ', list)
# %%
