from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()
chrome.get("http://uitestingplayground.com/classattr")
sleep(5)
blue_button = chrome.find_element(By.CSS_SELECTOR,
                                  '.btn.btn-primary').click()
for _ in range(3):
    blue_button = chrome.find_element(By.CSS_SELECTOR,
                                      '.btn.btn-primary').click()

sleep(5)
