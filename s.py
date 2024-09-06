from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def startBot(username, password, url):
    # Initialize the ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Open the website
    driver.get(url)
    
    # Allow some time for the page to load
    time.sleep(3)
    
    # Find the username field and input the username
    username_field = driver.find_element(By.NAME, "username")  # Adjust the locator based on the actual attribute
    username_field.send_keys(username)
    
    # Find the password field and input the password
    password_field = driver.find_element(By.NAME, "password")  # Adjust the locator based on the actual attribute
    password_field.send_keys(password)
    
    # Find the login button and click it
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")  # Adjust the CSS selector based on the actual attribute
    login_button.click()
    
    # Optional: Wait to see the result before closing the browser
    time.sleep(5)
    
    # Close the browser
    driver.quit()

# Driver Code
# Enter your login credentials
username = "your_username"
password = "your_password"

# URL of the login page of the website you want to automate
url = "https://www.artisticimpression.org/login"

# Call the function
startBot(username, password, url)
