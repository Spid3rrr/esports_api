import time
import requests
import os
import ast
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
#from flask_restful import Resource, Api, reqparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def getdata():
    dataresult = ' /// '
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("https://lolesports.com/schedule?leagues=lec")
    html = driver.page_source
    soup = BeautifulSoup(html,features="html.parser")
    results = soup.find_all('div', class_ = 'team team1')
    print('result : \n')
    for result in results:
        teamname = result.find('span',class_='name')
        if teamname is None:
            continue
        dataresult = dataresult +' // '+ teamname.text.strip()
    return dataresult
    driver.quit()

# welcome msg
@app.route('/')
def index():
    sresult = 'Welcome to our server !!' + getdata()
    return sresult



#our main function
app = Flask(__name__)
api = Api(app)
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
