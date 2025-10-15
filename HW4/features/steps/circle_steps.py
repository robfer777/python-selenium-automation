from behave import given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I open Target Circle page")
def step_open_circle_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com/circle")

@then("I should see at least 10 benefit cells")
def step_verify_benefits(context):
    wait = WebDriverWait(context.driver, 15)
    cells = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "[data-test*='CircleBenefit']")
    ))
    assert len(cells) >= 10, f"Expected at least 10 benefit cells, but found {len(cells)}"
    context.driver.quit()
