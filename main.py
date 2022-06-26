
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#import chrome webdriver
driver = webdriver.Chrome(r'C:\Users\akram\Documents\Akram\aaa\chromedriver.exe')
#open google.com
driver.get('https://www.google.com/')
#Maximize the chrome windows
driver.maximize_window()

#Search and click the button by Name
def buttonClick(text):
    buttonList = driver.find_elements(by=By.TAG_NAME, value='button')
    for button in buttonList:
        if button.text==text:
            button.click()
#Search and click the link by xpath
def linkClick(text):
    linkList= driver.find_elements(by=By.XPATH, value="//h3[contains(text(),\"S\'identifier sur LinkedIn\")]")
    for link in linkList:
        if link.text==text:
            link.click()
#Search and click the area text by selector
def labelClick(text):
    labelist=driver.find_elements(by=By.CSS_SELECTOR, value=text)
    for selector in labelist:
        selector.click()

buttonClick('Tout accepter')
driver.find_element(by=By.NAME, value='q').send_keys('Linkedin Login')
driver.find_element(by=By.NAME, value='q').send_keys(Keys.RETURN)
linkClick('S\'identifier sur LinkedIn')
labelClick('#username')
driver.find_element(by=By.CSS_SELECTOR, value='#username').send_keys('email')
labelClick('#password')
driver.find_element(by=By.CSS_SELECTOR, value='#password').send_keys('password')
time.sleep(5)
driver.find_element(by=By.CSS_SELECTOR, value='#username').send_keys(Keys.RETURN)


