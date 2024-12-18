import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    yield driver


def test_shop(setup):
    driver = setup

    driver.find_element(By.ID, "user-name").send_keys("standart_user")
    driver.find_element(By.ID, "password").send_keys("secret_sause")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Василий")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("455016")

    driver.find_element(By.ID, "Continue").click()

    result = driver.find_element(By.__class__, "summary_total_label").text
    assert int(result) == "58,29"

    driver.quit()
