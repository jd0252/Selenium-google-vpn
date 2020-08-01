# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:57:39 2020

@author: jd025
"""
from selenium import webdriver
import random
import time
options = webdriver.ChromeOptions()
# 禁用瀏覽器彈窗避免預設路徑載入失敗
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
    
#找到Google擴充套件的檔案位置(注意路徑需使用雙斜線 "\\")
options.add_extension('C:\\Users\\jd025\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\gjknjjomckknofjidppipffbpoekiipm\\6.2.0_0.crx')
#將擴充套件放入至Webdriver的開啟網頁內容
options.add_experimental_option('prefs', prefs)
#隱藏『Chrome正在受到自動軟體的控制』這項資訊
options.add_argument("disable-infobars")  

#啟動selenium 務必確認driver 檔案跟python 檔案要在同個資料夾中
driver = webdriver.Chrome(options=options)

#啟動擴充套件連上VPN 
#連結套件的html位置 chrome-extension://gjknjjomckknofjidppipffbpoekiipm/panel/index.html
driver.get("chrome-extension://gjknjjomckknofjidppipffbpoekiipm/panel/index.html")
#進入迴圈設定點擊次數、點擊目標、間斷時間

#設定點擊次數
times=5
#設定目標網址
url="http://www.web-time.com.tw/sidlink10.aspx?sid=13100"


for i in range(1,times+1):
    #設定隨機間隔時間避免短時間大量造訪被拒
    rest= random.randint(1,10)
    #嘗試以VPN進入網站刷點擊率
    try:
        #透過find_element_by_xpath找到點擊的位置並且點擊
        driver.find_element_by_xpath('//*[@id="screenMain"]/div[3]/div[1]').click()
        #進入目標網頁
        driver.get(url)
        #等待載入
        time.sleep(2)
        print("Success times:"+str(i)+"/"+str(times))
        #回到外部套件關閉VPN
        driver.get("chrome-extension://gjknjjomckknofjidppipffbpoekiipm/panel/index.html")
        driver.find_element_by_xpath('//*[@id="screenMain"]/div[3]/div[1]').click()
        time.sleep(rest)
    except:    
        print("Error! You need to check the website or code and restart the program!")
        break
print("Mission Complete!!")
driver.close()