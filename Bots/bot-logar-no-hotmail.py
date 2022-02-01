import time

from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get('https://login.live.com/')
navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys('roberto-nascimento22@hotmail.com')
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys('53d4fjdrpq')
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
