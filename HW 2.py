from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome in incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Open Target website
    driver.get("https://www.target.com/")
    time.sleep(3)

    # Step 2: Click on Account button
    account_button = driver.find_element(By.XPATH, "//span[text()='Account']")
    account_button.click()
    time.sleep(2)

    # Step 3: Click Sign In button from side navigation
    sign_in_button = driver.find_element(By.XPATH, "//span[text()='Sign in']")
    sign_in_button.click()
    time.sleep(3)

    # Step 4: Verify Sign-In page opened
    driver.find_element(By.XPATH, "//h1[contains(text(),'Sign in or create account')]")
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign in')]")

    print("✅ Test Passed: Sign-In page opened successfully!")

except Exception as e:
    print("❌ Test Failed:", e)

finally:
    time.sleep(3)
    driver.quit()
