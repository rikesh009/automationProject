import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(6)
element_username = driver.find_element(By.NAME,"username")
element_username.send_keys("Admin")
element_password = driver.find_element(By.NAME,"password")
element_password.send_keys("admin123")
element_button= driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
element_button.click()
driver.close()
# python project