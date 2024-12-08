from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(5)
element = driver.find_element(By.LINK_TEXT, 'Close')
element.click()

sleep(5)
