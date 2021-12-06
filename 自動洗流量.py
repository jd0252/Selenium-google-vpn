# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:57:39 2020

@author: jd025
"""
import _thread
import time
from selenium import webdriver
import time
import random


#設定點擊次數
times=5
#設定目標網址
url="https://medium.com/@mirthful_maize_locust_764/python-selenium-google-vpn%E5%A5%97%E4%BB%B6%E5%91%88%E7%8F%BE%E8%87%AA%E5%8B%95%E8%AE%8A%E6%8F%9Bip%E4%BD%8D%E7%BD%AE%E6%B4%97%E6%B5%81%E9%87%8F%E7%A8%8B%E5%BC%8F-6f8872759b8d"

def click(Thread,times,url):
    options = webdriver.ChromeOptions()
    # 禁用瀏覽器彈窗避免預設路徑載入失敗
    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
                }
            }
    
    #找到Google擴充套件的檔案位置(注意路徑需使用雙斜線 "\\")
    options.add_extension('C:\\Users\\jd025\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\gjknjjomckknofjidppipffbpoekiipm\\7.0.10_0.crx')
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
    time.sleep(60)
    for i in range(1,times+1):
        
        #設定隨機間隔時間避免短時間大量造訪被拒
        rest= random.randint(1,10)
        #嘗試以VPN進入網站刷點擊率
        try:
            #透過find_element_by_xpath找到點擊的位置並且點擊
            
            driver.find_element_by_xpath('//*[@id="screenMain"]/div[3]/button[1]').click()
            time.sleep(10)
            #進入目標網頁
            driver.get(url)
            #等待載入
            time.sleep(10)
            print(Thread ,":" , str(i) , "/" , times)
            #回到外部套件關閉VPN
            driver.get("chrome-extension://gjknjjomckknofjidppipffbpoekiipm/panel/index.html")
            driver.find_element_by_xpath('//*[@id="screenMain"]/div[3]/button[1]').click()
            time.sleep(rest)
        except:    
            print("Error! You need to check the website or code and restart the program!")
            break
    print(Thread,"Mission Complete!!")
    driver.close()
    
_thread.start_new_thread( click, ("Thread-1",2 ,url) )
_thread.start_new_thread( click, ("Thread-2",2 ,url ) )
_thread.start_new_thread( click, ("Thread-3",2 ,url ) )
_thread.start_new_thread( click, ("Thread-4",2 ,url ) )
_thread.start_new_thread( click, ("Thread-5",2 ,url ) )
_thread.start_new_thread( click, ("Thread-6",2 ,url ) )
_thread.start_new_thread( click, ("Thread-7",2 ,url ) )
_thread.start_new_thread( click, ("Thread-8",2 ,url ) )    
