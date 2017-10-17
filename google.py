#!/usr/bin/python

import time
from selenium import webdriver

# Basic Selenium implementation

url = "http://www.google.com"

driver = webdriver.Chrome()
driver.get(url)


search_field = driver.find_element_by_id("lst-ib")
search_field.clear()
search_field.send_keys("ServiceNow")
search_field.submit()

lists = driver.find_elements_by_class_name("rc")
count = len(lists)
print "Results returned: {}".format(count)
i = 0
for item in lists:
    print ""
    print item.text

    i += 1
    if i > 10:
        break

time.sleep(5)


driver.quit()