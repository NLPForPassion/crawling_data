from selenium import webdriver
from pymongo import MongoClient
from datetime import datetime
import time
client = MongoClient("mongodb+srv://npfnin:npfnin@cluster0.t4wx3.mongodb.net/<dbname>?retryWrites=true&w=majority")
db= client.Ba
driver = webdriver.Chrome("D:/TuHoc/moitruong/chromedriver.exe")

def crawlData():    
    try:
        content = driver.find_element_by_class_name('doc-online')
        data = content.text
        print(data)
        data={"idLink":link,
              "data":data,
              "dateCrawl":datetime.now().strftime("%d/%m/%y"),
              "state":'No'}
        db.Con2.insert_one(data)
        #move the next page:
        page_next = driver.find_element_by_css_selector('span[class="glyphicon glyphicon-arrow-right"]')
        page_next.click()
        time.sleep(1)
        crawlData()
    except:
        print('!!!')
    

for i in db.Con1.find():
    try:
        link = i["link"]
        idlink = i["_id"]
               
        driver.get(link)
        
        #open page doc online
        move = driver.find_element_by_css_selector('a[class="btn btn-warning btn-md"]')
        link_temp = move.get_attribute('href')
            
        time.sleep(1)
            
        driver.get(link_temp)
    except:
        db.Con1.update_one({"_id" : i["_id"]}, {"$set": {"state": "Yes"}})
        print('Khong cho doc online')
    crawlData()

driver.close()
##    driver.quit()
    


    
    
    
