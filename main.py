from selenium import webdriver
from selenium.webdriver.common.by import By
import time,threading

# threads
# This thread clicks on the bog cookie
def big_cookie_thread():
    while True:
        big_cookie = driver.find_element(By.ID, "bigCookie")
        big_cookie.click()
        time.sleep(1)

# Thread function to click on upgrades
def click_upgrades():
    while True:
        upgrade = driver.find_element(By.XPATH,'//*[@id="upgrades unlocked enabled"]')
        if upgrade:
            upgrade[-1].click()
        products = driver.find_element(By.XPATH,'//*[@class="product unlocked enabled"]')
        if products:
            products[-1].click()
        time.sleep(5)

# To keep webdriver running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()

time.sleep(5)
language_button = driver.find_element(By.ID, value="langSelect-EN")
print(language_button)
language_button.click()

time.sleep(5)
close_cookies_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div/a[1]")
close_cookies_btn.click()



cookie_click_t = threading.Thread(target=big_cookie_thread)
cookie_click_t.start()
upgrades_click_t = threading.Thread(target=click_upgrades)
upgrades_click_t.start()



# print(cookies_number)

# driver.close()  # Closes the page
# driver.quit()   # Quits the browser