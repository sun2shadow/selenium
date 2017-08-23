#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver import ActionChains
browser = webdriver.Firefox()
url = "http://www.runoob.com/try/try.php?filename=jqueryui-example-draggable"
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_id('draggable')
ActionChains(browser).drag_and_drop_by_offset(source,200,300).perform()
