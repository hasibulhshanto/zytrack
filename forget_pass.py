from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (Chrome in this example)
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH or provide the full path

try:
    # Open the login page
    driver.get("https://zystg.dinnova.ch/login")

    # Wait until the "Forget Password" button is clickable and click it
    forgetpass_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/a"))
    )
    forgetpass_button.click()

    # Wait until the URL changes to the forgot-password page
    WebDriverWait(driver, 20).until(EC.url_to_be("https://zystg.dinnova.ch/forgot-password"))
    
    # Select the email field and enter the email address
    email_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='email']")))
    email_field.send_keys("hshanto.test+24@gmail.com")

    # Wait until the "Send Instruction" button is clickable and click it
    sendinstruction_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/form/div[2]/button"))
    )
    sendinstruction_button.click()

    # Wait until the URL changes back to the login page
    WebDriverWait(driver, 20).until(EC.url_to_be("https://zystg.dinnova.ch/login"))


    #To check the email and set new password
    #driver.execute_script("window.open('');")

    # Switch to the new tab
    #driver.switch_to.window(driver.window_handles[1])

    # Open another URL in the new tab
    #driver.get("https://mail.google.com/mail/u/0/#inbox") #lands on the email inbox page

    #Enter email address
    # gmail_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='identifierId']")))
    # gmail_field.send_keys("hshanto.test@gmail.com") 
    # time.sleep(2)

    # #Click on Next button
    # next_button = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/div[3]"))
    # )
    # next_button.click()

    # #Enter password
    # password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")))
    # password_field.send_keys("Shanto@198503") 
    # time.sleep(2)

    # #Again click on Next button
    # next_button = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "//*[@id='passwordNext']/div/button/div[3]"))
    # )
    # next_button.click()

    # #Click on Continue button
    # continue_button = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "//*[@id='yDmH0d']/div[1]/div[1]/div[2]/div/div/div[3]/div/div[1]/div/div/button/div[3]"))
    # )
    # continue_button.click()










finally:
    # Close the browser
    driver.quit()
