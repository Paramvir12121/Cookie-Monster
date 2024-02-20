from selenium import webdriver

# To keep webdriver running
crome_options = webdriver.ChromeOptions()
crome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")





# driver.close()
# driver.quit()