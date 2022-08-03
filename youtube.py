from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Users/harishgundluru/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://youtube.com")
driver.maximize_window()
try:
    hrefContainer = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video-title-link"))
    )
except:
    driver.quit()
hrefContainer = driver.find_element(By.ID, "video-title-link")
href = hrefContainer.get_attribute("href")
driver.get(href)
try:
    viewCount = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "view-count"))
    )
except:
    driver.quit()
viewCount = driver.find_element(By.CLASS_NAME, "view-count")
print(viewCount.text)
