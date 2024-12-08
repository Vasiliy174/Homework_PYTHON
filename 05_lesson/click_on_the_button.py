from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()
chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    add_button = chrome.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()

    chrome_delete_buttons = chrome.find_elements(
        By.XPATH, "//button[text()='Delete']")

print(f"Список состоит из {len(chrome_delete_buttons)} элементов")

sleep(10)
chrome.quit
