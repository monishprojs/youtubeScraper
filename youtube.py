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
print(driver.title)
try:
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
except:
    driver.quit()
search = driver.find_element(By.NAME, "search_query")
search.click()
search.send_keys("coding")
search.send_keys(Keys.RETURN)
try:
    metadata = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ytd-video-meta-block"))
    )
except:
    driver, quit()
metadata = driver.find_elements(By.CLASS_NAME, "ytd-video-meta-block")
for i in range(3):
    print(metadata[i].text)
