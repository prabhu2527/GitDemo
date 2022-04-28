from selenium import webdriver

# browser exposes an executable file
# through selenium test we need to invoke the executable file which will then invoke actual browser
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\prabh\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()  # maximize window
driver.get("https://login.salesforce.com")  # get method hit url in the browser
driver.find_element(By.CSS_SELECTOR,"input#username").send_keys("prabhu")
driver.find_element(By.CSS_SELECTOR,".password").send_keys("rampur")
driver.find_element(By.CSS_SELECTOR,".password").clear()
driver.find_element(By.LINK_TEXT,"Forgot Your Password?").click()
driver.find_element(By.XPATH,"//a[text()='Sandbox Login']").click()

driver.find_element(By.XPATH,"//form[@name='login']/div[1]/label").click()

driver.find_element(By.CSS_SELECTOR,"form[name='login'] label:nth-child(3)").clear()
#driver.close()
