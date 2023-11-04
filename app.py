from flask import Flask, request, jsonify
from splinter import Browser
import time
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options


app = Flask(__name__)


@app.route('/execute', methods=['GET'])
def execute_code():
    try:
        browser = Browser('chrome', incognito=True)

        # Define the URL you want to open in the WebView
        url = 'https://google.com'

        # Open the URL in the WebView
        browser.visit(url)
        time.sleep(10)

        browser.quit()

        return jsonify({"message": "Code executed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)



