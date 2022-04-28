from selenium import webdriver

# browser exposes an executable file
# through selenium test we need to invoke the executable file which will then invoke actual browser
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\prabh\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()  # maximize window
driver.get("https://rahulshettyacademy.com/angularpractice/")  # get method hit url in the browser
driver.find_element(By.NAME,'name').send_keys("prabhu")
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("rampur")
driver.find_element(By.ID,'exampleInputPassword1').send_keys("1234")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
#select class provide the method to handle the options in dropdown
dropdown=Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element(By.XPATH,"//input[@type='submit']").click()
print(driver.find_element(By.CLASS_NAME,'alert-success').text)
message = driver.find_element(By.CLASS_NAME,'alert-success').text
assert "success" in message
driver.close()

#driver.close()
