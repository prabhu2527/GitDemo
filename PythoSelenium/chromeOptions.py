#Js DOM can access any elements on web page just like how selenium does
#selenium have a method to execute javascript code in it
from selenium import webdriver
from selenium.webdriver.common.by import By
validateText="Option3"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="C:\\Users\\prabh\\Downloads\\chromedriver_win32\\chromedriver.exe",options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice")
print(driver.title)