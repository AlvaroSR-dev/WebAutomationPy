from lib2to3.pgen2 import driver
from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://www.abc.es/registro-newsletter/personalize.aspx')

time.sleep(2)

UserEmail = "autouser@gmail.com"
email = web.find_element_by_xpath('//*[@id="ctl00_Contenido_Personalize1_email"]')
email.send_keys(UserEmail)

time.sleep(1)

UserPass = "password"
password = web.find_element_by_xpath('//*[@id="ctl00_Contenido_Personalize1_password"]')
password.send_keys(UserPass)

time.sleep(1)

UserName = "Usuario"
name = web.find_element_by_xpath('//*[@id="ctl00_Contenido_Personalize1_Nombre"]')
name.send_keys(UserName)

time.sleep(1)

UserDate = "01/01/1995"
surname = web.find_element_by_xpath('//*[@id="ctl00_Contenido_Personalize1_Fecha"]')
surname.send_keys(UserDate)

time.sleep(1)

UserProvincia = "Madrid"
surname = web.find_element_by_xpath('//*[@id="ctl00_Contenido_Personalize1_Provincia"]')
surname.send_keys(UserProvincia)

time.sleep(1)

Submit = web.find_element_by_xpath('//*[@id="ctl00_Contenido_Personalize1_Enviar"]')
Submit.click()