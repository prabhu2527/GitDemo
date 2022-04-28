import time

from selenium import webdriver
from selenium.webdriver.common.by import By
validateText="Option3"
driver = webdriver.Chrome(executable_path="C:\\Users\\prabh\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(5)
#wait until 5 sec if object not displayed --
# #global wait, applies to all objects
#1.5 sec to reach next page - exexution will resume in 1.5 sec
#if object does not show up at all, then max time your test waits for 5sec
driver.maximize_window()  # maximize window
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
time.sleep(4)
count=len(driver.find_elements(By.XPATH,"//div[@class='products']/div"))
assert count==3
buttons=driver.find_elements(By.XPATH,"//div[@class='product-action']/button")
for button in buttons:
    button.click()
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
driver.find_element(By.CSS_SELECTOR,"span.promoInfo").text
