import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    yield browser
    browser.quit()


def test_fill_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in fields.items():
        field = driver.find_element(
            By.CSS_SELECTOR, f"input[name='{field_name}']")
        field.send_keys(value)

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "was-validated")))

    for field_name in fields.keys():
        field = driver.find_element(
            By.CSS_SELECTOR, f"input[name='{field_name}']")
        assert "is-valid" in field.get_attribute(
            "class"), f"Поле '{field_name}' должно быть подсвечено зеленым."

    zip_code_field = driver.find_element(
        By.CSS_SELECTOR, "input[name='Zip code']")
    assert "is-invalid" in zip_code_field.get_attribute(
        "class"), "Поле 'Zip code' должно быть подсвечено красным."
