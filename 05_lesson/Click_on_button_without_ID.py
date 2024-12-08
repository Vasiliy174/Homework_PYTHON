from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()
count = 0
driver.get("http://uitestingplayground.com/dynamicid")
blue_button = driver.find_element(
    "xpath", '//button[text()="Button with Dynamic ID"]').click()
for _ in range(3):
    blue_button = driver.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
count = count + 1
sleep(5)
