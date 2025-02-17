from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = Chrome(chrome_options=chrome_options)
driver.get("https://www.google.com")
