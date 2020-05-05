import config
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
from datetime import datetime

slug = "adventure"


driver.get("https://www.wattpad.com/stories/{}".format(slug))

# elems = driver.find_elements_by_css_selector(".browse-story-item completed [href]")
# links = [elem.get_attribute('href') for elem in elems]

# print(elems)

a_elements = []
content_blocks = driver.find_elements_by_class_name("content")

for block in content_blocks:
    elements = block.find_elements_by_tag_name("a")
    for el in elements:
        a_elements.append(el.get_attribute("innerHTML"))
   
print (a_elements)
driver.close()
