# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:53:20 2018

@author: Akhila Sri Manasa
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://stackoverflow.com/questions/tagged/python?sort=votes&pageSize=15")
a = [];
#a = driver.find_element_by_xpath("//*div[@class='questions']/div/div[2]")
a = driver.find_elements_by_class_name('question-hyperlink')
a[1].href.click()
   
 