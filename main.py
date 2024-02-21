from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# To keep webdriver running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

language_button = driver.find_element(By.ID, value="langSelect-EN")
language_button.click()
time.sleep(5)


close_cookies_btn = driver.find_element(By.XPATH,"//a[@data-cc-event='click:dismiss']")
close_cookies_btn.click()
while True:
    big_cookie = driver.find_element(By.ID, "bigCookie")
    big_cookie.click()
    



# print(cookies_number)

# driver.close()  # Closes the page
# driver.quit()   # Quits the browser