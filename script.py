import time
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#our function for counting from 0-20
def counting():
    for i in range(0,21):
        if i==20:
            print("counting at: "+str(i))
            print("Done counting...")
        else:
            print("counting at: "+str(i))
            time.sleep(5) #sleep for 5 seconds

def getdata():
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=options)
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
#our main function
if __name__ == '__main__':
    getdata() #call our counting method