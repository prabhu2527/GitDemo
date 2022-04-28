import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver.support import expected_conditions as EC, wait

validateText = "Option3"
list1=[]
list2 =[]
driver = webdriver.Chrome(executable_path="C:\\Users\\prabh\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()  # maximize window
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in buttons:
    print(button.find_element(By.XPATH,"parent::div/parent::div/h4").text)
    list1.append(button.find_element(By.XPATH,"parent::div/parent::div/h4").text)
    button.click()
print(list1)
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
##wait only for specific object

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
veggies=driver.find_elements(By.CSS_SELECTOR,"p.product-name")
for veg in veggies:
    list2.append(veg.text)
print(list2)
assert list1 == list2
originalAmount = driver.find_element(By.CSS_SELECTOR,".discountAmt").text
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
discountAmount = driver.find_element(By.CSS_SELECTOR,".discountAmt").text
assert float(discountAmount < originalAmount)
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)
amounts = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum=0
for amount in amounts:
    print(amount.text)
    sum = sum + int(amount.text)

print(sum)

totalamount=int(driver.find_element(By.CLASS_NAME,"totAmt").text)

assert sum == totalamount