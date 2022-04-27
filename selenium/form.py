from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://google.com')

# 検索ボックスを探す
e1 = driver.find_element_by_name('q')
# キーワードを入力
e1.send_keys('cyber security')
# フォームを送信する
e1.submit()

time.sleep(10)
driver.close()
