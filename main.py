from selenium import webdriver
from selenium.webdriver.common.by import By 

# To keep webdriver running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# cookies_number = driver.find_element(By.ID, value="cookies").text
# print(cookies_number)

# driver.close()  # Closes the page
# driver.quit()   # Quits the browser