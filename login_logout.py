import gspread
from google.oauth2.service_account import Credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your downloaded JSON key file (fix invalid escape sequence)
credentials_path = r'H:\Automations\copper-tracker-444016-a3-ff77dc688416.json'

# Define the scope for the Sheets and Drive APIs
scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# Authenticate and create a service account
creds = Credentials.from_service_account_file(credentials_path, scopes=scopes)

# Authenticate with gspread using the credentials
gc = gspread.authorize(creds)

# Open the Google Sheet by URL or title
sheet_url = "https://docs.google.com/spreadsheets/d/1eN_lJuM1P_0NG2YCtbcpscmNELTC8_E-7j2YMRZu2T8/edit?usp=sharing"
sheet = gc.open_by_url(sheet_url).sheet1  # Open the first sheet
data = sheet.get_all_records()  # Get all records from the sheet

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH or provide full path
driver.maximize_window()

# Optional: Implicit wait for elements to load
driver.implicitly_wait(10)

try:
    for row in data:
        email = row["Email"]
        password = row["Password"]

        # Open the login page
        driver.get("https://app.zytrack.ch/login")

        # Wait until the email and password fields are present on the page
        email_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
        password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div[2]/form/div[3]/button"))
        )

        # Enter the credentials with short delays between actions
        email_field.clear()
        email_field.send_keys(email)
        time.sleep(2)  # Wait 2 seconds before entering the password
        password_field.clear()
        password_field.send_keys(password)
        time.sleep(2)  # Wait 2 seconds before clicking login

        # Click the login button
        login_button.click()

        # Wait for the login to process and for the next page to load
        WebDriverWait(driver, 20).until(EC.url_changes("https://app.zytrack.ch/login"))
        time.sleep(3)  # Additional short wait after login

        # Check the current URL to decide whether to click the close message button
        current_url = driver.current_url
        if current_url == "https://app.zytrack.ch/dashboard":
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

        WebDriverWait(driver, 20).until(EC.url_changes("https://app.zytrack.ch/dashboard"))
        time.sleep(3)  # Additional short wait after login

finally:
    # Close the browser
    driver.quit()
