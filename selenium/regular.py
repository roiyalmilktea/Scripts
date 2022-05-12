import schedule
from selenium import webdriver
from time import sleep
import time


def job():
    driver = webdriver.Chrome()
    url = 'https://google.com/'
    driver.get(url)


schedule.every().days.at("22:31").do(job)

while True:
    schedule.run_pending()
    time.sleep(30)
