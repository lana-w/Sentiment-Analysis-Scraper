from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import pandas as pd

driver = webdriver.Chrome('/Applications/Google Chrome.app')

driver.get('https://www.rogerebert.com/')

positive = 0
negative = 0
neutral = 0

search_box = driver.find_element(By.NAME, 'q')

search_box.send_keys('Jurassic Park')

search_box.submit()