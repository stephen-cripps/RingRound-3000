from selenium import webdriver     
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


def open_and_login(username, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = Service(executable_path="./chromedriver-win64/chromedriver.exe")
    
    browser = webdriver.Chrome(service=service, options=options)

    browser.get("https://acorntheunion.nationbuilder.com/admin")

    print("Opened nationbuilder")

    usernameElement = WebDriverWait(browser, 10).until(lambda d: d.find_element(By.ID, "username"))

    usernameElement.send_keys(username)

    passwordElement = WebDriverWait(browser, 10).until(lambda d: d.find_element(By.ID, "password"))

    passwordElement.send_keys(password)

    loginButton = WebDriverWait(browser, 10).until(lambda d: d.find_element(By.XPATH, "//button[text()='Continue']"))

    loginButton.click()

    # Keep the browser open for 60 seconds
    time.sleep(60)




