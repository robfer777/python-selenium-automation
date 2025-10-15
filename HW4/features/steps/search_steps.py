from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I open Target homepage search")
def step_open_homepage(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(service=Service(), options=chrome_options)
    context.driver.get("https://www.target.com/")



@then("I should see multiple product results")
def step_verify_results(context):
    wait = WebDriverWait(context.driver, 10)
    products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-test='product-title']")))
    assert len(products) > 1, f"Expected multiple results, got {len(products)}"
    print(f"✅ Found {len(products)} products.")
    context.driver.quit()
