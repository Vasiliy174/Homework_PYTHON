from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/inputs')
input_1 = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_1.send_keys('1000')
input_1.clear()
input_1.send_keys('999')

sleep(2)
