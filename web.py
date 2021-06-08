from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from fake_useragent import UserAgent
from selenium import webdriver
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
import random 
import json

class instabot:
  def __init__(self,username,password,curso):
    self.username = username
    self.password = password
    self.curso = curso

    profile = webdriver.FirefoxProfile('C:/Users/SEU_USER/AppData/Roaming/Mozilla/Firefox/Profiles/y14nta5s.default-release')

    PROXY_HOST = "143.255.52.195"
    PROXY_PORT = "59616"
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", PROXY_HOST)
    profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    #COnfiguration PROXY LIST para tentar burlar o RECAPTCHA 

    self.driver = webdriver.Firefox(firefox_profile=profile,executable_path="CAMINHO///PASTAS GO GECK OVER DRIVER/geckodriver.exe")
  #Corpo basico do scraping
  def login(self):
    driver = self.driver
    driver.get("https://prounialuno.mec.gov.br/")
    sleep(random.randint(10,20))
    
    login_pro = driver.find_element_by_link_text('ENTRAR COM GOV.BR')
    login_pro.click()

    user = driver.find_element_by_id('j_username')
    user.click()
    user.clear()
    user.send_keys(self.username)
    user.send_keys(Keys.RETURN)
    sleep(6)
    sleep(random.randint(5,20))

    senha = driver.find_element_by_id('j_password')
    senha.click()
    senha.clear()
    senha.send_keys(self.password)
    sleep(6)  
    senha.send_keys(Keys.RETURN)
    sleep(30)

    #Procurar o curso
    procurar = driver.find_element_by_id('alterar_curso_1')
    procurar.click()
    sleep(8)

    consultar = driver.find_element_by_id('input_consultar')
    consultar.click()
    consultar.send_keys(self.curso)
    sleep(9)
    consultar.send_keys(Keys.DOWN,Keys.DOWN, Keys.RETURN)
    sleep(10)

    #pegando dados 
    municipio = driver.find_elements_by_xpath('//ul[@class =\"municipio_lista\"]').click()
    sleep(10)

    html_content = municipio.get_attribute('outerHTML') 
    print(html_content)

    
    #driver.quit()


inforLogin = instabot('SENHA','USER','CURSO')
inforLogin.login()

