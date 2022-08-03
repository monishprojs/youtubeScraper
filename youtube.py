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
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'video-title'))
    )
except:
    driver.quit()
title = driver.find_element(By.ID, 'video-title')
title.click()
meta = driver.find_elements(By.CLASS_NAME, "yt-formatted-string")
print(meta[0])
