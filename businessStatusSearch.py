# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:39:14 2020

@author: YongYong
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--disable-notifications")
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://www.hometax.go.kr/')
delay = 30
linkElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'prcpSrvcNm_0')))
linkElem.click()
linkElem = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[4]/div[2]/div[1]/div/div[1]/a')))
time.sleep(0.15)
linkElem.click()
linkElem = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[4]/div[2]/div[1]/div/div[2]/ul/li[4]/a')))
linkElem.click()
linkElem = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[4]/div[2]/div[1]/div/div[2]/ul/li[4]/ul/li[3]/a')))
linkElem.click()
browser.switch_to.frame(browser.find_element_by_id('txppIframe'))
fo = open("bsnoList.txt")
bsno_lists = fo.read().split()
fo.close()
fw = open('bsnoResult.txt', 'a')
for i in bsno_lists:
    inputElem = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.ID,'bsno')))
    inputElem.send_keys(i)
    time.sleep(5)
    inputElem.send_keys(Keys.ENTER)
    fw.write(i + '\t' + WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#grid2_cell_0_1 > nobr'))).text + '\n')
fw.close()
browser.close()
