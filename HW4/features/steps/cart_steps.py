from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given("I open Target homepage")
def step_open_homepage(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(service=Service(), options=chrome_options)
    context.driver.get("https://www.target.com/")

@when('I search for "{product}"')
def step_search_product(context, product):
    wait = WebDriverWait(context.driver, 10)
    search_box = wait.until(EC.element_to_be_clickable((By.ID, "search")))
    search_box.send_keys(product)
    search_box.submit()

@when("I add the first product to the cart")
def step_add_product_to_cart(context):
    wait = WebDriverWait(context.driver, 15)
    first_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='addToCartButton']")))
    first_item.click()
    time.sleep(3)

@then("I should see the product in the cart")
def step_verify_product_in_cart(context):
    context.driver.get("https://www.target.com/cart")
    time.sleep(3)
    items = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='cart-item']")
    assert len(items) > 0, "❌ No items found in cart!"
    print(f"✅ Cart has {len(items)} item(s).")
    context.driver.quit()
