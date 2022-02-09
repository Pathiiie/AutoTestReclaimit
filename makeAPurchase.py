# Goes into demo shop, chooses an item, puts in customer
# information and completes the order

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

PATH = "G:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://reclaimit.jetshop.se/")

#meny = driver.find_element(By.ID, "menu-activator")
#meny.click()

item1 = driver.find_element(By.ID, "startpage_list_ctl03_linkView")
item1.click()
time.sleep(1)
addToCart = driver.find_element(By.ID, "ctl00_main_ctl00_ctl00_AddToCart")
addToCart.click()
time.sleep(1)
goToCheckout = driver.find_element(By.ID, "dc-checkout-btn")
goToCheckout.click()
time.sleep(1)

förnamn = driver.find_element(By.ID, "ctl00_main_responsivecheckout_CustomerInfo_tbFirstName")
förnamn.send_keys("Patrik")
time.sleep(1)
efternamn = driver.find_element(By.ID, "ctl00_main_responsivecheckout_CustomerInfo_tbLastName")
efternamn.send_keys("Jansson")
time.sleep(1)
adress = driver.find_element(By.ID, "ctl00_main_responsivecheckout_CustomerInfo_tbStreet")
adress.send_keys("fakeland 123")
time.sleep(1)
postnummer = driver.find_element(By.ID, "ctl00_main_responsivecheckout_CustomerInfo_tbPostalCode")
postnummer.send_keys("12345")
time.sleep(1)
ort = driver.find_element(By.ID, "ctl00_main_responsivecheckout_CustomerInfo_tbCity")
ort.send_keys("Stockholm")
time.sleep(1)
email = driver.find_element(By.ID, "ctl00_main_responsivecheckout_CustomerInfo_tbEmail")
email.send_keys("japa19fn@gmail.com")
time.sleep(1)
confirmEmail = driver.find_element(By.ID, "ctl00_main_responsivecheckout_CustomerInfo_tbEmailValidate")
confirmEmail.send_keys("japa19fn@gmail.com")
time.sleep(1)
mobilnummer = driver.find_element(By.ID, "ctl00_main_responsivecheckout_CustomerInfo_tbMobile")
mobilnummer.send_keys("123456789")
time.sleep(1)
paymentMethod = driver.find_element(By.ID, "ctl00_main_responsivecheckout_PaymentSelector_repButtons_ctl01_spanPaymentText")
paymentMethod.click()
time.sleep(1)
