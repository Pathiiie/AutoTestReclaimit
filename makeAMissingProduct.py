from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

PATH = "G:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://reclaimit.jetshop.se/")

time.sleep(2)
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(4)

reklamation = driver.find_element(By.ID, "category-navigation")
reklamation.click()

driver.switch_to.frame(driver.find_element(By.ID, "reclaimitiframe"))
time.sleep(2)

try:
    order = driver.find_element(By.ID, "ReceiptNumber")
    order.send_keys("10006")
except NoSuchElementException:
    print("exception handled")

time.sleep(2)

try:
    email = driver.find_element(By.ID, "CustomerNumber")
    email.send_keys("demo@reclaimit.com")
except NoSuchElementException:
    print("exception handled")


time.sleep(2)

#//submit[@value='Nästa »']

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Nästa »']"))).click()
time.sleep(2)




