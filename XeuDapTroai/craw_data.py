from selenium import webdriver
import time
from pymongo import MongoClient
from datetime import datetime

def craw_data():    
    try:
        content = driver.find_element_by_class_name('doc-online')
        dt = content.text
        print(dt)
        data={"idLink":link,
              "data":dt,
              "dateCrawl":datetime.now().strftime("%d/%m/%y"),
              "state":'No'}
        db.DATA.insert_one(data)
        #move the next page:
        page_next = driver.find_element_by_css_selector('span[class="glyphicon glyphicon-arrow-right"]')
        page_next.click()
        time.sleep(1)
        craw_data()
    except:
        print('!!!')
    
############
client = MongoClient("mongodb+srv://17102591:Hao0215817@cluster0.bufis.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.NLP
driver = webdriver.Chrome()
for i in db.LINK.find(no_cursor_timeout=True):
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
        print('Khong cho doc online')
    craw_data()
    
##    driver.close()
##    driver.quit()
    


    
    
    
