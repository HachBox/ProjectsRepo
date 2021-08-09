#from this video https://www.youtube.com/watch?v=Xjv1sY630Uc

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.reddit.com/")
print(driver.title)

search = driver.find_element_by_id("header-search-bar")
search.send_keys("funny")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "rpBJOHq2PR60pnwJlUyP0"))
    )
    #print(main.text)
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("_1Y6dfr4zLlrygH-FLmr8x- ")
        print(header.text)
finally:
    driver.quit()

#main - driver.find_element_by_class_name("rpBJOHq2PR60pnwJlUyP0")

#print(driver.page_source) #prints source code

#time.sleep(5)

#driver.close() #closes tab
#driver.quit() #closes browser