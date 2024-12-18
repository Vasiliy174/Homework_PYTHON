from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")
input = driver.find_element(By.CSS_SELECTOR, '.form-control')
input.send_keys('SkyPro')

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()
wait = WebDriverWait(driver, 5)

print((button))

driver.quit()
