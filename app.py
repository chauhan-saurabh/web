from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/execute', methods=['GET'])
def execute_code():
    try:
        # Set the DISPLAY environment variable to ':0' to specify the display.
        os.environ['DISPLAY'] = ':0'
        
        # Use ChromeOptions to configure the headless mode and browser settings.
        options = Options()
        options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')

        # Initialize the Chrome WebDriver with the specified options.
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1200, 600)

        # Set an implicit wait to wait for elements to become visible.
        driver.implicitly_wait(10)  # Adjust the timeout as needed.

        # Visit the website.
        driver.get('https://vip.theralytics.net/')

        # Find and interact with web elements using WebDriverWait.
        # username_input = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.NAME, "userName"))
        # )
        # username_input.send_keys('vipadmin')

        # password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
        # password_input.send_keys('TheraAdmin2020@2')

        # login_button = driver.find_element(By.CSS_SELECTOR, 'button')
        # login_button.click()

        # nav_bar = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "nav-menu"))
        # )
        # nav_bar.click()

        # client = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.LINK_TEXT, "Manage Client"))
        # )
        # client.click()

        # client_list = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.LINK_TEXT, "Client List"))
        # )
        # client_list.click()

        # client_search = driver.find_element(By.NAME, 'Name')
        # client_search.send_keys('sean')

        # time.sleep(3)

        # yellow_eye = driver.find_element(By.CSS_SELECTOR, ".tbactionbtn.yellowfont")
        # yellow_eye.click()

        # time.sleep(3)

        # try:
        #     edit_button = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR, ".smbtn.editclient"))
        #     )
        #     edit_button.click()
        # except:
        #     pass

        # try:
        #     middle_name_field = driver.find_element(By.NAME, "middleName")
        #     middle_name_field.send_keys('Davidson')
        # except:
        #     pass

        # try:
        #     submit_button = driver.find_element(By.LINK_TEXT, "Save & Continue")
        #     submit_button.click()
        # except:
        #     pass

        # time.sleep(10)

        driver.quit()

        return jsonify({"message": "Code executed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8084)
