from selenium import webdriver
from urllib.parse import unquote
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from datetime import date
import time

client= MongoClient("mongodb+srv://huylu:npf.huy8@cluster0.ua0vg.mongodb.net/<dbname>?retryWrites=true&w=majority")
db_link= client.Link
db_content= client.Content
driver = webdriver.Chrome()

# --------------------------------------------------

def addContent(id_link,data):
    dataContent = {
        "id_link":id_link,
        "data": data,
        "date": date.today().strftime("%m/%d/%Y"),
        "state": False
    }
    db_content.data.insert_one(dataContent)

# --------------------------------------------------

def clickk():
    try:
        step = driver.find_element_by_link_text("Đọc Online")
        c = step.get_attribute('href')
        driver.get(c)
    except:
        print("Hoan thanh")


# --------------------------------------------------

def get_content(id_link):
    try:
        content = driver.find_element_by_xpath('//div[@class="doc-online"]')
        data= content.text
        addContent(id_link,data)
        time.sleep(1)
        step= driver.find_element_by_xpath('//span[@class="glyphicon glyphicon-arrow-right"]')
        step.click()
        get_content(id_link)
    except:
        db_link.data.update_one({"_id": id_link}, { "$set": { "state": True } })
# --------------------------------------------------

def Test():
    list_id=[]
    for x in db_link.data.find({}):
        list_id.append(x['_id'])
    # print(len(list_id))

    for i in range(0, len(list_id)):
        cursor= db_link.data.find({'_id': list_id[i]})
        for doc in cursor:
            if(doc['state']==False):
                driver.get(doc['link'])
                clickk()
                get_content(doc['_id'])
    driver.close()

Test()

# --------------------------------------------------
