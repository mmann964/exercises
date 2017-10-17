#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

url_str = "http://www.nytimes.com"

r = requests.get(url_str)
html_block = r.text
soup = BeautifulSoup(html_block, "html.parser")
# print soup.prettify()

titles = soup.find_all(class_="story-heading")
for article in titles:
    if article.a:
        print article.a.text.replace('\n', " ").strip()
    else:
        print article.contents[0].strip()

# print titles