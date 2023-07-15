from selenium import webdriver

from bs4 import BeautifulSoup

import pandas as pd

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.rogerebert.com/')

time.sleep(2) # Let the user actually see something!

search_box = driver.find_element(By.NAME, 'q')

search_box.send_keys('Jurassic Park')

search_box.submit()

# driver.quit()
