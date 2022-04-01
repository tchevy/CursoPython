from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = "C:/Users/Dev/AppData\Local/Programs/Python/Python310/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
s=Service(driver_path)
option = webdriver.ChromeOptions()
option.binary_location = brave_path

url = "https://terra.com.br"
new_url = "https://www.google.com.br"
cont = 1
while cont ==1:
  browser = webdriver.Chrome(service=s, options=option)
  browser.get (url)
  cont = cont + 1


if cont ==2:
    print(cont)
    browser.get(new_url)

# if cont ==2:
#     print(cont)
#     browser = webdriver.Chrome(service=s, options=option)
#     browser.get(new_url)
#     cont = cont + 1
#     continue
