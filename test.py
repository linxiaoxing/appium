# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

caps = {}
caps["deviceName"] = "emulator-5554"
caps["platformName"] = "android"
caps["appPackage"] = "com.example.appiumsam"
caps["appActivity"] = ".MainActivity"
caps["noReset"] = True
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
wait = WebDriverWait(driver,10)
wait.until(lambda driver: driver.find_element_by_id('com.example.appiumsam:id/edittext'))
el1 = driver.find_element_by_id("com.example.appiumsam:id/edittext")
el1.send_keys("00000")
wait = WebDriverWait(driver,10)
wait.until(lambda driver: driver.find_element_by_id('com.example.appiumsam:id/show'))
el2 = driver.find_element_by_id("com.example.appiumsam:id/show")
el2.click()

driver.quit()