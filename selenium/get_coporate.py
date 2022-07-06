from selenium import webdriver

number = int(input('Which choose number?'))

driver = webdriver.Chrome()
if number == 0:
    # 検索エンジン
    url = 'https://www.google.com'
    driver.get(url)

elif number == 1:
    # FFRI
    url = 'https://www.google.com'
    driver.get(url)
    el = driver.find_element_by_name('q')
    el.send_keys('FFRI')
    el.submit()

elif number == 2:
    # beriserve
    url = 'https://www.google.com'
    driver.get(url)
    el = driver.find_element_by_name('q')
    el.send_keys('beriserve')
    el.submit()

elif number == 3:
    # infosec
    url = 'https://www.google.com'
    driver.get(url)
    el = driver.find_element_by_name('q')
    el.send_keys('infosec')
    el.submit()

elif number == 4:
    # securvail
    url = 'https://www.google.com'
    driver.get(url)
    el = driver.find_element_by_name('q')
    el.send_keys('securvail')
    el.submit()

elif number == 5:
    # solitonsystems
    url = 'https://www.google.com'
    driver.get(url)
    el = driver.find_element_by_name('q')
    el.send_keys('solitonsystems')
    el.submit()
