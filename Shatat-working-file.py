from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

import pandas as pd

driver = webdriver.Chrome('/Desktop/Personal/CodingProjects/chromedriver_mac_arm64.zip')

driver.get('https://www.rogerebert.com/reviews/insidious-the-red-door-movie-review-2023')

positive = 0
negative = 0
neutral = 0

phrase1 = driver.find_elements_by_xpath('//td[@class="hh-salaries-sorted"]')

phrase2 = driver.find_elements_by_xpath('//td[@class="hh-salaries-sorted"]')