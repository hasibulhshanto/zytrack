from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
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

    first_name_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div/div/div/div[3]/form/div[1]/div[2]/div/div[2]/div/div/input"))
    )
    first_name_input.clear()
    first_name_input.send_keys("Shanto Hasan")

    time.sleep(2)

    # Wait for the last name input to be clickable, then update it
    last_name_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div/div/div/div[3]/form/div[1]/div[2]/div/div[3]/div/div/input")) 
    )
    last_name_input.clear()
    last_name_input.send_keys("Hasibul")

    time.sleep(2)

    # Wait for the Zytrack Language dropdown to be visible and click it
    languagedd_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='flex items-center justify-between h-[46px] gap-2 px-3 bg-white border cursor-pointer toggler border-input rounded-bl-[0px] rounded-br-[0px] !rounded-[5px]']"))
    )
    languagedd_button.click()  # Click to open the dropdown

    # Wait for the currently selected language to be visible
    selected_language = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='text-[13px] overflow-hidden whitespace-nowrap placeholder !text-[#232C2F] flex gap-2']"))
    )

    # Get the text of the currently selected language
    current_language = selected_language.text.strip()

    # Check the selected language and select the opposite one
    if "English" in current_language:
        # If English is selected, select German
        german_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div/div/div/div[3]/form/div[1]/div[2]/div/div[5]/div/div/div[2]/div[1]"))  # XPath for German option
        )
        german_option.click()
    elif "Deutsch" in current_language:
        # If German is selected, select English
        english_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div/div/div/div[3]/form/div[1]/div[2]/div/div[5]/div/div/div[2]/div[2]"))  # XPath for English option
        )
        english_option.click()
    else:
        print("Current language is neither English nor German.")

    # # Wait for the English & German dropdown options to be visible
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='text-[13px] overflow-hidden whitespace-nowrap placeholder !text-[#232C2F] flex gap-2']"))
    # )

    # time.sleep(2)

    # # Find and click the option you want to select German
    # german_option = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "//div[@id='app']//form//div[1]//div[2]//div[5]//div//div//div[2]//div[1]"))
    # )
    # german_option.click()

    # Optional: Wait to verify the action
    time.sleep(2)

    

finally:
    # Close the browser
    driver.quit()
