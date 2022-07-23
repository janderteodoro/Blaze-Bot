from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from config import config
urlCrash = config['crashUrl']

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir-Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acess(self, url):
        self.chrome.get(url)
        sleep(3)

    def close(self):
        self.chrome.quit()

    def getLastValues(self):
        while True:
            try:
                lastValues = []
                spanLastValues = self.chrome.find_element(By.CLASS_NAME, 'entries')
                lastValues = spanLastValues.text.split('\n')
                print(lastValues)
                sleep(6)
                break
                
            except:
                print('Error in get the lasts values in crash game')
                break


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acess(urlCrash)
    chrome.getLastValues()