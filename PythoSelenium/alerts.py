import time

from selenium import webdriver
from selenium.webdriver.common.by import By
validateText="Option3"
driver = webdriver.Chrome(executable_path="C:\\Users\\prabh\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()  # maximize window
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(validateText)
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert
print(alert.text)
alertText = alert.text
assert validateText in alertText
alert.accept()


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(validateText)
driver.find_element(By.ID,"confirmbtn").click()
alert=driver.switch_to.alert
print(alert.text)
alertText = alert.text
assert validateText in alertText
alert.dismiss()
