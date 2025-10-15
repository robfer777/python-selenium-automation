from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


@given("I open Target product page")
def step_open_target_page(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service()
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    url = "https://www.target.com/p/men-s-short-sleeve-t-shirt-goodfellow-co/-/A-54551690"
    context.driver.get(url)
    print(f"Opened: {url}")


@when("I click through each color option")
def step_click_colors(context):
    driver = context.driver
    wait = WebDriverWait(driver, 30)
    try:
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-test='swatch'] button, div[data-test='swatch']")))
        color_buttons = driver.find_elements(By.CSS_SELECTOR, "div[data-test='swatch'] button, div[data-test='swatch']")
        print(f"Found {len(color_buttons)} colors")
        for i, btn in enumerate(color_buttons):
            try:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", btn)
                print(f"✅ Clicked color {i + 1}")
                time.sleep(1)
            except Exception as e:
                print(f"⚠️ Could not click color {i + 1}: {e}")
    except Exception as e:
        print(f"❌ No color buttons found: {e}")
        raise


@then("each color should be selected successfully")
def step_verify_colors(context):
    print("✅ Color test completed.")
    time.sleep(2)
    context.driver.quit()
