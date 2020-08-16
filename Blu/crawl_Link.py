from selenium import webdriver
from pymongo import MongoClient
from datetime import date

client= MongoClient("mongodb+srv://huylu:npf.huy8@cluster0.ua0vg.mongodb.net/<dbname>?retryWrites=true&w=majority")
db_link= client.Link


driver = webdriver.Chrome()
driver.get("https://sachvui.com/the-loai/van-hoc-viet-nam.html")
'''
format document, insert document in db
'''
def addLink(link,title):
    a= date.today().strftime("%m/%d/%Y")
    dataLink={
        "link": link,
        "title":title,
        "date": a,
        "state": False,
        "topic": "Phiêu lưu, mạo hiểm"
    }
    db_link.data3.insert_one(dataLink)
'''
get links in sachvui web
'''
def get_link():
    try:
        contain = driver.find_elements_by_css_selector("h5")
        for p in contain:
            link=driver.find_element_by_link_text(p.text).get_attribute('href')
            addLink(link,p.text)
        step= driver.find_element_by_link_text("→")
        step.click()
        get_link()
    except:
        print("finish")
get_link()


driver.close()