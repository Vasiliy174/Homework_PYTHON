from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

usernamefield = driver.find_elements(By.CSS_SELECTOR, "username")
passwordfield = driver.find_elements(By.CSS_SELECTOR, "password")

sleep(5)

usernamefield.send_keys("tomsmith")
passwordfield.send_keys("SuperSecretPassword")

loginbutton = driver.find_elements(By.CSS_SELECTOR, "button")
loginbutton.click()
