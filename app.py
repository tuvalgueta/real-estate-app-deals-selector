from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route('/extract-planning-info', methods=['GET'])
def extract_planning_info():
    # Set up the Selenium WebDriver (make sure you have the necessary driver)
    driver = webdriver.Chrome()  # or use the appropriate driver for your browser

    try:
        # Replace with the URL you want to scrape
        driver.get('http://example.com/planning-info')

        # Extract planning information (modify XPath or CSS Selector as needed)
        planning_info_elements = driver.find_elements(By.XPATH, '//div[@class="planning-info"]')
        planning_info = [element.text for element in planning_info_elements]

        return jsonify(planning_info), 200
    
    except Exception as e:
        return str(e), 500
    
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)