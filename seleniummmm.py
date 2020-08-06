from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient

client = MongoClient('mongodb+srv://firstData:firstdata10@cluster-iukdn.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = client.nlp



driver = webdriver.Chrome()
driver.get("https://sachvui.com/doc-sach/tuoi-tho-du-doi/chuong-1-phan-thu-nhat.html")

# Read paragraph:
content = driver.find_element_by_xpath('/html/body/div[1]/div[3]/p')
print(content.text)
data = content.text

# create json variety
datas = {}
# datas = {"data":string}
datas["data"] = data

# push data to mongoDB
db.data_raw.insert_one(datas)

def clickk():
    try:
        nextt = driver.find_element_by_xpath('//span[@class="glyphicon glyphicon-arrow-right"]')
        nextt.click()
        content = driver.find_element_by_xpath('//p[@class=" noi_dung_online"]')
        data = content.text

        # create json variety
        datas = {}
        # datas = {"data":string}
        datas["data"] = data

        # push data to mongoDB
        db.data_raw.insert_one(datas)

        clickk()

    except:
        print('finish!!!')

clickk()
