import time
import sys

from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get('https://login.live.com/')
navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys('roberto-nascimento22@hotmail.com')
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys('')
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
navegador.find_element_by_xpath('//*[@id="KmsiCheckboxField"]').click()

navegador.find_element_by_xpath('//*[@id="idBtn_Back"]').click()
#navegador.find_element_by_xpath('//*[@id="id__105"]').click()
#navegador.find_element_by_xpath('//*[@id="id__51"]').click()
#navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys('/home/roberto.dias/Imagens/backgroudti2.jpg')

#navegador.find_element_by_xpath('//*[@id="id__40"]').click()



