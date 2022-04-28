from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\\prabh\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice")
action=ActionChains(driver)
menu=driver.find_element(By.ID,"mousehover")
action.move_to_element(menu).perform()
childMenu=driver.find_element(By.LINK_TEXT,"Reload")
action.move_to_element(childMenu).click().perform()