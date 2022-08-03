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
time.sleep(5)
search.send_keys("coding")
