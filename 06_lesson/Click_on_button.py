from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
wait = WebDriverWait(driver, 40, 0.5)

driver.get("http://uitestingplayground.com/ajax")

click_button = driver.find_element(
    By.CSS_SELECTOR, ('button[class="btn btn-primary"]')
    ).click()
green_text = wait.until(EC.visibility_of_element_located((
    By.CSS_SELECTOR, ".bg-success"))).text
print(green_text)

driver.quit()
