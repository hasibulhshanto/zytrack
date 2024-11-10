from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH or provide the full path
driver.maximize_window()

try:
    # Open the target page
    driver.get("https://zystg.dinnova.ch/login")

    # Wait until the login fields are available, then log in
    email_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div[2]/form/div[3]/button"))
    )

    email_field.send_keys("hshanto.test@gmail.com")
    time.sleep(2)
    password_field.send_keys("Info@123")
    time.sleep(2)
    login_button.click()

    # Wait for the profile page to load and navigate to profile page
    WebDriverWait(driver, 20).until(EC.url_changes("https://zystg.dinnova.ch/login"))

    # Go to the My Profile page
    userinfo_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[1]/div[2]/div[2]/div[2]"))
    )
    userinfo_button.click()

    myprofile_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[1]/div[2]/div[3]/div/ul/li[1]"))
    )
    myprofile_button.click()

    WebDriverWait(driver, 20).until(EC.url_contains("/profile"))

    # To upload image
    uploadphoto_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div/div/div/div[3]/form/div[1]/div[2]/div/div[1]/div/div[2]/div/div/label[2]"))
    )
    uploadphoto_button.click()

    # Locate the file input element and upload the file
    file_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@type='file']"))
    )
    file_path = "C:/Software/Automation/images/man.jpg"  # Replace with the actual file path
    file_input.send_keys(file_path)

    # Wait for the cropping popup to appear (adjust the XPath as needed)
    crop_popup = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div/div/div/div[3]/form/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div"))
    )

    # Perform cropping actions - this depends on the HTML structure of the crop popup
    # Example: Click and drag to set the cropping area (requires JS if it's a draggable crop area)
    
    # Example of clicking a Crop button
    crop_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div/div/div/div[3]/form/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/button"))
    )
    crop_button.click()

    # Wait to ensure the upload and crop are complete
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
