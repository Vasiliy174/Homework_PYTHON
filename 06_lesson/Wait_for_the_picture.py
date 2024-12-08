from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 100)

pictures = WebDriverWait(driver, 15).until(

    EC.element_to_be_clickable((By.CSS_SELECTOR, '#image container')))
src = driver.find_element(By.ID, "award")

print(src)

driver.quit()
