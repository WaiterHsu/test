import time
import requests
import json
import math

import git
repo = git.Repo.init(path='.')

#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from RPA.Browser.Selenium import Selenium

#讀取 現在時間
from datetime import datetime
a = datetime.now()
print(a)


# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://shopee.tw/flash_sale')
# driver.set_window_size(1280,1400)
# #driver.refresh()

# driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div/div/div/div[3]/div/div/div[1]/ul/li[1]').click()
# time.sleep(2)

# driver.close()

#爬蟲
lib = Selenium()

lib.open_available_browser('https://www.playsport.cc/predictgame.php?allianceid=1&gameday=yesterday')
out = lib.get_text('//*[@id="predict_form"]/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/a')
lib.close_browser()
print(out)

#把 資訊 塞進 txt
try:
  with open('未命名.txt','a') as wf:
    wf.write(out)
except:
  print('error in write new thing.')
  
# 讀取新的txt 看是否有改變
try:
  with open('未命名.txt','r') as rf:
    print(rf.readlines())
  print('已改寫，未命名')
except:
  with open('未命名1.txt','r') as wf:
    print(wf.readlines())
  print('已改寫，未命名1')
  
  
#嘗試用git 更改檔案
try:
    repo.index.add(items=['未命名.txt'])
    repo.index.commit('write a line into test.file')
    print('successful')
except:
    print('error in git push')



