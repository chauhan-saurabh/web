from flask import Flask, request, jsonify
from splinter import Browser
from selenium import webdriver
import time
import random


app = Flask(__name__)

# Set up the Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
# options.add_argument('--user-agent={}'.format(random.choice(list(self.user_agents))))

driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(90)

# # Load the URL and get the page source
driver.implicitly_wait(6)
driver.get('https://vip.theralytics.net/')


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/execute', methods=['GET'])
def execute_code():
    try:
        browser = Browser('chrome')
        browser.visit('https://vip.theralytics.net/')
        time.sleep(5)

        browser.fill("userName", 'vipadmin')

        password_field = browser.find_by_xpath('//input[@type="password"]')
        password_field.fill("TheraAdmin2020@2")

        login_button = browser.find_by_css("button")
        if login_button:
            login_button.click()
        else:
            return jsonify({"error": "Login button not found!"})

        navBar = browser.find_by_css(".nav-menu")
        if navBar:
            navBar.click()
        else:
            return jsonify({"error": "navBar with class name not found!"})

        client = browser.find_by_text("Manage Client")
        if client:
            client.first.click()
        else:
            return jsonify({"error": "Div element with text 'Client' not found!"})

        client_list = browser.find_by_text("Client List")
        if client_list:
            client_list.first.click()
        else:
            return jsonify({"error": "Div element with text 'Client List' not found!"})

        client_search = browser.find_by_name('Name')
        if client_search:
            client_search.fill('sean')
        else:
            return jsonify({"error": "client_search not found!"})

        time.sleep(3)

        yellow_eye = browser.find_by_css(".tbactionbtn.yellowfont")
        if yellow_eye:
            yellow_eye.click()
        else:
            return jsonify({"error": "yellow_eye with class name not found!"})

        time.sleep(3)

        try:
            edit_button = browser.find_by_css(".smbtn.editclient")
            edit_button.click()
        except StaleElementReferenceException:
            edit_button = browser.find_by_css(".smbtn.editclient")
            edit_button.click()

        time.sleep(1)

        try:
            middleNameField = browser.find_by_name("middleName")
            middleNameField.fill('Davidson')
        except StaleElementReferenceException:
            middleNameField = browser.find_by_name("middleName")
            middleNameField.fill('Davidson')
            time.sleep(1)

        try:
            submitButton = browser.find_by_text("Save & Continue")
            submitButton.click()
        except StaleElementReferenceException:
            submitButton = browser.find_by_text("Save & Continue")
            submitButton.click()

        time.sleep(10)

        browser.quit()

        return jsonify({"message": "Code executed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



