#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 18:08:35 2021

@author: lescardone
"""

from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException
import time
import shutil as sh
import requests

url = 'https://www.pexels.com/search/sad/'
driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

images = soup.find_all('img',class_='photo-item__img')
len(images)
links = [image.attrs['src'] for image in images]
links
len(links)

for i,link in enumerate(links):
    full_url = link
    
    r = requests.get(full_url, stream=True) #Get request on full_url
    if r.status_code == 200:
        with open("photos/all_happy/happy_{}.jpg".format(i), 'wb') as f: 
            r.raw.decode_content = True
            sh.copyfileobj(r.raw, f)
