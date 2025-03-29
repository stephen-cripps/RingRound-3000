import time
from selenium import webdriver     
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By

class ui_automator:
    def __init__(self, browser=None):
        if browser:
            self.browser = browser
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            service = Service(executable_path="./chromedriver-win64/chromedriver.exe")
            self.browser = webdriver.Chrome(service=service, options=options)

    def open_and_login(self, username, password):
        self.browser.get("https://acorntheunion.nationbuilder.com/admin")
        print("Opened nationbuilder")

        username_element = WebDriverWait(self.browser, 10).until(
            lambda d: d.find_element(By.ID, "username")
        )
        username_element.send_keys(username)

        password_element = WebDriverWait(self.browser, 10).until(
            lambda d: d.find_element(By.ID, "password")
        )
        password_element.send_keys(password)

        login_button = WebDriverWait(self.browser, 10).until(
            lambda d: d.find_element(By.XPATH, "//button[text()='Continue']")
        )
        login_button.click()

    def update_person(self, person, ring_round_date):
        print(f"Updating {person.name}")

        search_box = WebDriverWait(self.browser, 10).until(
            lambda d: d.find_element(By.ID, "search_box_form")
        )

        # get the input box child of the form
        search_box_input = search_box.find_element(By.TAG_NAME, "input")
        search_box_input.send_keys(person.name)

        search_box_suggestions = WebDriverWait(search_box, 10).until(
            lambda d: search_box.find_elements(By.CLASS_NAME, "suggestion-name")
        )

        # If more than 1 suggestion, log and return. ToDo: Potentially Best to update the CSV? 
        if len(search_box_suggestions) > 1:
            print(f"More than 1 suggestion for {person.name} - please update manually")
            return

        search_box_suggestions[0].click()

        log_contact_button = WebDriverWait(self.browser, 10).until(
            lambda d: d.find_element(By.PARTIAL_LINK_TEXT, "Log contact")
        )

        log_contact_button.click()

        notes_box = WebDriverWait(self.browser, 10).until(
            lambda d: d.find_element(By.XPATH, "//textarea[contains(@id, '_signup_call_content')]")
        )

        self.browser.execute_script("arguments[0].value = arguments[1];", notes_box, person.format_notes(ring_round_date))

        dropdown = WebDriverWait(self.browser, 10).until(
            lambda d: d.find_element(By.XPATH, "//select[@name='signup_call[contact_method_id]']")
        )

        select = Select(dropdown)
        select.select_by_visible_text("Phone call")

        if person.meaningful_interaction.lower() == "yes":
            status_label = "Meaningful interaction"
        elif person.answered.lower() == "yes":
            status_label = "Answered"
        else:
            status_label = "No answer"

        contact_status_radio = WebDriverWait(self.browser, 10).until(
            lambda d: d.find_element(By.XPATH, f"//label[text()='{status_label}']/preceding-sibling::input[@type='radio']")
        )
        self.browser.execute_script("arguments[0].click();", contact_status_radio)

        save_button = WebDriverWait(self.browser, 10).until(
            lambda d: d.find_element(By.XPATH, "//input[contains(@value, 'was contacted')]")
        )

        self.browser.execute_script("arguments[0].click();", save_button)

        print(f"Updated {person.name}")


    def close_browser(self):
        self.browser.quit()