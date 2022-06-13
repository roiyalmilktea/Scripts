from selenium import webdriver

driver = webdriver.Chrome()

url = "https://google.com"


def login():
    driver.get(url)


if __name__ == '__main__':
    login()
