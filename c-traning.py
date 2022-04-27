from selenium import webdriver

from login import login_download

driver = webdriver.Chrome()

url = "https://judge.u-aizu.ac.jp/onlinejudge/signin.jsp"

driver.get(url)

id = driver.find_element_by_name('userID')
pa = driver.find_element_by_name('password')

id.send_key('hit03923')
id.submit()
pa.submit()
