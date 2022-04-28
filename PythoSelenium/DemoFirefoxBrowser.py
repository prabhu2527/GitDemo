from selenium import webdriver

# browser exposes an executable file
# through selenium test we need to invoke the executable file which will then invoke actual browser
#driver = webdriver.Chrome(executable_path="C:\\Users\\prabh\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Firefox(executable_path="C:\\Users\\prabh\\Downloads\\geckodriver-v0.30.0-win64\geckodriver.exe")
driver.maximize_window()          #maximize window
driver.get("https://rahulshettyacademy.com")   #get method hit url in the browser
print(driver.title) #title of the page
print(driver.current_url)
driver.get("http://google.com")
driver.minimize_window()           #minimize window
driver.back()             #back button
driver.refresh()          #reload the webpage
driver.close()