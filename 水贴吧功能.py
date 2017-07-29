# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://passport.baidu.com/v2/?login')
driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys(u'小杨杰00')
driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys(u'yj68034201')
driver.find_element_by_id('TANGRAM__PSP_3__submit').send_keys(Keys.ENTER)
driver.get('https://tieba.baidu.com/p/5127644817')
menu = driver.find_element_by_id('ueditor_replace').click()
time.sleep(5)
js="document.getElementById('ueditor_replace').innerHTML='abc'"
driver.execute_script(js)
driver.find_element_by_class_name('poster_submit').send_keys(Keys.ENTER)
