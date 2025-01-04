from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Setup webdriver
driver = webdriver.Chrome ()
driver.maximize_window()

# Optional: Implicit wait for elements to load
driver.implicitly_wait(10)

try:
    #To open url
    driver.get("https://zystg.dinnova.ch/login")


    # Wait until the email and password fields are present on the page
    email_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div[2]/form/div[3]/button"))
        )
    # Enter the credentials with short delays between actions
    email_field.clear()
    email_field.send_keys("qa@infodigita.com")
    time.sleep(2)  # Wait 2 seconds before entering the password
    password_field.clear()
    password_field.send_keys("password")
    time.sleep(2)  # Wait 2 seconds before clicking login

    # Click the login button
    login_button.click()

    # Wait for the login to process and for the next page to load
    WebDriverWait(driver, 20).until(EC.url_changes("https://zystg.dinnova.ch/login"))
    time.sleep(3)  # Additional short wait after login

    # Check the current URL to decide whether to click the close message button
    current_url = driver.current_url
    if current_url == "https://zystg.dinnova.ch/admin-dashboard":
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

    WebDriverWait(driver, 20).until(EC.url_changes("https://zystg.dinnova.ch/admin-dashboard"))
    time.sleep(3)  # Additional short wait after login












finally:
    #To close browser
    driver.quit()
