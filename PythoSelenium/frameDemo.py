from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\\prabh\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()  # maximize window
#tagnames iframe,frameset,frame
driver.get("https://the-internet.herokuapp.com/iframe")
#frameid, framename,index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR,"#tinymce").clear()
driver.find_element(By.CSS_SELECTOR,"#tinymce").send_keys("Iam able to automate")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME,"h3").text)
