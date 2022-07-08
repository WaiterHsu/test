print('hello world, haha')

import time
import requests
import json
import math

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://shopee.tw/flash_sale')
# driver.set_window_size(1280,1400)
# #driver.refresh()

# driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div/div/div/div[3]/div/div/div[1]/ul/li[1]').click()
# time.sleep(2)

# driver.close()

lib = Selenium()

lib.open_available_browser('https://www.playsport.cc/predictgame.php?allianceid=1')
lib.close_browser()
