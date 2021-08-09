from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.autotempest.com/")

link = driver.find_element_by_link_text("Blog")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "AutoTempest’s New Email Alerts Bring A Nationwide Used Car Search to Your Inbox"))
    )
    element.click()

    driver.back()
    driver.back()
    driver.back()
    driver.forward()
except:
    time.sleep(5)
    driver.quit()

# driver.find_element_by_xpath("//select[@name='make']/option[text()='Ford']").click()
# driver.find_element_by_xpath("//select[@id='model']/option[text()='Aerostar']").click()
# driver.find_element_by_xpath('//*[@id="search-main"]/div/div[4]/button').click()

#time.sleep(15)
#driver.quit()