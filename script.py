import time
import requests
import os
import pandas as pd
import ast
from bs4 import BeautifulSoup
from flask import Flask
from flask_restful import Resource, Api, reqparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def getdata():

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
        print(teamname.text.strip())
        print()
    driver.quit()
class teams(Resource):
    #methods go here
    def get(self):
        return {'test value':' noice '},200
    pass



#our main function
app = Flask(__name__)
api = Api(app)
api.add_resource(teams,'/teams')
if __name__ == '__main__':
    getdata() #get data