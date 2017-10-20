#!/usr/bin/python

from selenium import webdriver

url = "http://www.nytimes.com"

driver = webdriver.Chrome()
driver.get(url)
articles = driver.find_elements_by_class_name("story-heading")
print len(articles)

with open("nytimes.txt", 'w') as fname:
    for i in articles:
        try:
            fname.write(i.text)
            fname.write("\n")
        except UnicodeEncodeError:
            fname.write("UnicodeEncodeError \n")

driver.close()