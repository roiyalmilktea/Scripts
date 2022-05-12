from selenium import webdriver


print('login?')

n = int(input())

if n == 1:
    driver = webdriver.Chrome()
    url = "https://accounts.google.com/signin"

    def login():
        driver.get(url)
    if __name__ == '__main__':
        login()
        
