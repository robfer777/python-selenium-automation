from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I open Target homepage")
def step_open_homepage(context):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    service = Service()
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.get("https://www.target.com/")

@when("I click Account button")
def step_click_account(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Account']"))
    ).click()

@when("I click Sign In from side navigation")
def step_click_sign_in(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Sign in']"))
    ).click()

@then("I should see the Sign In form")
def step_verify_signin_form(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Sign in or create account')]"))
    )
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Sign in')]"))
    )
    context.driver.quit()
