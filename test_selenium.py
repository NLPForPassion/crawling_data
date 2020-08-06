from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://sachvui.com/doc-sach/tuoi-tho-du-doi/chuong-1-phan-thu-nhat.html")

# Read paragraph:
content = driver.find_element_by_css_selector('p. noi_dung_online')
print(content)

driver.close()