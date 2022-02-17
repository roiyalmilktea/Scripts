from selenium import webdriver

driver = webdriver.Chrome()
# 攻撃先IPアドレスを指定
url = "http://localhost:8000/admin"

while(True):

    driver.get(url)
