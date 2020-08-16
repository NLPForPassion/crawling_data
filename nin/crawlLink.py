from selenium import webdriver
from pymongo import MongoClient
from datetime import datetime
import time


client= MongoClient("mongodb+srv://npfnin:npfnin@cluster0.t4wx3.mongodb.net/<dbname>?retryWrites=true&w=majority")

db= client.Ba
driver = webdriver.Chrome("D:/TuHoc/moitruong/chromedriver.exe")
driver.get("https://sachvui.com/the-loai/thu-vien-phap-luat.html")

tp = driver.find_element_by_css_selector('div[class="panel panel-primary"] > div[class="panel-heading"]')
topic = tp.text
def crawlLink():
        try:
            list_book = driver.find_elements_by_css_selector('h5[class="tieude text-center"] > a')
            
            for i in list_book:
                link = i.get_attribute('href')
                title = i.text
                print(link)
                
                data = {"title":title,
                        "link":link,
                        "dateCrawl":datetime.now().strftime("%d/%m/%y"),
                        "state": "No",
                        "topic": topic}                
                db.Con1.insert_one(data)
            step= driver.find_element_by_link_text("→")
            step.click()   
            
            
            time.sleep(3)
            crawlLink()
        except:
            print('!!!!!!!!!')    
crawlLink()        
