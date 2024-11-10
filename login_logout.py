from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH or provide the full path


# Maximize the browser window
driver.maximize_window()

try:
    # Open the login page
    driver.get("https://zystg.dinnova.ch/login")

    # Wait until the email and password fields are present on the page
    email_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div[2]/form/div[3]/button"))
    )

    # Enter the credentials with short delays between actions
    email_field.send_keys("hshanto.test@gmail.com")
    time.sleep(2)  # Wait 2 seconds before entering the password
    password_field.send_keys("Info@123")
    time.sleep(2)  # Wait 2 seconds before clicking login

    # Click the login button
    login_button.click()

    # Wait for the login to process and for the next page to load
    WebDriverWait(driver, 20).until(EC.url_changes("https://zystg.dinnova.ch/login"))
    time.sleep(3)  # Additional short wait after login

    # Wait until the close message button is clickable and click it
    closemessage_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div[2]"))
    )
    closemessage_button.click()

    # Wait until the user info button is clickable and click it
    userinfo_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[1]/div[2]/div[2]/div[2]"))
    )
    userinfo_button.click()

    # Wait until the sign-out button is clickable and click it
    signout_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[1]/div[2]/div[3]/div/ul/li[4]"))
    )
    signout_button.click()

    WebDriverWait(driver, 20).until(EC.url_changes("https://zystg.dinnova.ch/dashboard"))
    time.sleep(3)  # Additional short wait after login


finally:
    # Close the browser
    driver.quit()
