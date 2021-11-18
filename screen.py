from selenium import webdriver
url = 'https://python.org'

save_file = 'screenshot_full.png'

#main
def screenshot_full(url, save_file):
    w, h = get_page_size(url)
    screenshot_size(url, save_file, w, h)

#ページの幅と長さを取得する
def get_paze_size(url):
	#ブラウザを起動
	driver=webdriver.Chrome()
	driver.get(url)
	# ページ幅を取得
	w=driver.execute_script('return document.body.scrollWidth;')
	h=driver.execute_script('return document.body.scrollHeight;')
	# サイズを得たら閉じる	
	driver.close()
	print('page_size=',w,h)
	return w,h

#指定サイズでページを保存
def screenshot_size(url,save_file,w,h):
	#指定サイズで改めてChromeを起動
	options=webdriver.ChromeOptions()
	options.add_argument(win_size)
	#Chromeを起動し、ページをキャプチャ
	cap_driver=webdriver.Chrome(options=options)
	cap_driver.get(url)
	cap_driver.save_screenshot(save_file)
	cap_driver.close()
	

if __name__ == '__main__':
    screenshot_full(url, save_file)
