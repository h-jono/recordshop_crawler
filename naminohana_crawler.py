import requests
from bs4 import BeautifulSoup
import re
import pprint
import json

page_url = 'https://naminohana-records.com/?mode=srh&cid=&keyword=&sort=n&page='
page_count = 6 # ページの数(5まで取得)
item_url = 'https://naminohana-records.com/'
text = [] # json出力用の変数

for i in range(1, page_count):
    response = requests.get(page_url + str(i))
    soup = BeautifulSoup(response.text, "html.parser")
    elems = soup.find_all(href=re.compile("pid="))
    elems = elems[1::2]
    
    for elem in elems:
        text.append(elem.contents[0])
        text.append(item_url + elem.attrs['href'])

with open("naminohana.json", "w", encoding = "utf-8") as f:
    json.dump(text, f)

