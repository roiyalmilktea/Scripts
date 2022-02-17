from selenium import webdriver

driver = webdriver.Chrome()


def login():
    driver.get("http://localhost:8000/hello/")


if __name__ == '__main__':
    login()
