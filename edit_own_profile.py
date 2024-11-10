from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH or provide the full path
driver.maximize_window()

try:
    # Open the login page
    driver.get("https://zystg.dinnova.ch/login")

    # Wait until the login fields are available, then log in
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email"))).send_keys("hshanto.test@gmail.com")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("Info@123")

    time.sleep(2)  # Small delay to simulate human interaction
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div[2]/form/div[3]/button"))
    )
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

    # Locate the file input element and upload the file
    file_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@type='file']"))
    )
    file_path = "C:/Software/Automation/images/man.jpg"  # Replace with the actual file path
    file_input.send_keys(file_path)

    # Wait for the cropping popup to appear and finalize the cropping
    crop_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[3]/form/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/button"))
    )
    crop_button.click()

    # Wait to ensure the upload and crop are complete
    time.sleep(5)

    # Update inputs and profile information
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]"))
    ).clear().send_keys("Shanto Hasan")

    time.sleep(2)
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/form[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/input[1]"))
    ).clear().send_keys("Hasibul")

    time.sleep(2)

    # Locate and click on the custom dropdown (div element)
    dropdown_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/form[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]"))
    )
    dropdown_element.click()

    # Wait for options to appear (check for visibility of dropdown options)
    try:
        options = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='option']"))
        )
    except Exception as e:
        print("Error waiting for dropdown options:", e)
        driver.quit()
        exit()

    # Check if options are found and select the correct one
    target_option = "German"
    option_found = False
    for option in options:
        if option.text == target_option:
            option.click()  # Click the option
            print(f"Changed selection to: {target_option}")
            option_found = True
            break

    if not option_found:
        print(f"Option '{target_option}' not found in the dropdown.")

finally:
    # Close the browser
    driver.quit()
