from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

url = 'https://uta.pw/sakusibbs/users.php?user_id=1'
driver.get(url)

a_list = driver.find_elements_by_css_selector('ul#mmlist li a')
for a in a_list:
    print('■', a.text)
    print('〇', a.get_attribute('href'))
driver.close()
