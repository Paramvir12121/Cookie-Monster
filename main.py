from selenium import webdriver

# To keep webdriver running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://amazon.ca")



# driver.close()  # Closes the page
# driver.quit()   # Quits the browser