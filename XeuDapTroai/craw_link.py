from selenium import webdriver
import time
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb+srv://17102591:Hao0215817@cluster0.bufis.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.NLP

driver = webdriver.Chrome()
driver.get("")

tp = driver.find_element_by_css_selector('div[class="panel panel-primary"] > div[class="panel-heading"]')
topic = tp.text
def craw_link():
        try:
            list_book = driver.find_elements_by_css_selector('h5[class="tieude text-center"] > a')
            
            for i in list_book:
                link = i.get_attribute('href')
                title = i.text
                print(link)
                
                data = {"title":title,
                        "link":link,
                        "dateCrawl":datetime.now().strftime("%d/%m/%y"),
                        "state": 'No',
                        "topic": topic}                
                db.LINK.insert_one(data)
                
            move = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[21]/ul/li[5]/a')
            move.click()
            
            time.sleep(3)
            craw_link()
        except:
            print('!!!!!!!!!')    
craw_link()        
