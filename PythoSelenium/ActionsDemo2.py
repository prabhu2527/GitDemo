from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\\prabh\\Downloads\\chromedriver_win32\\chromedriver.exe")
#driver.get("https://www.familysearch.org/en/")
#ActionChains

#action.move_to_element(driver.find_element(By.ID,"search")).perform()
#action.move_to_element(driver.find_element(By.LINK_TEXT("Genealogies")).click().perform())

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action=ActionChains(driver)
action.context_click(driver.find_element(By.ID,"double-click")).perform()
action.double_click(driver.find_element(By.ID,"double-click")).perform()
alert=driver.switch_to.alert
assert "you double clicked me!!!, you got to be kidding me" == alert.text
alert.accept()
