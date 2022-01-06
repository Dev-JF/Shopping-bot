import requests
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

with open('info.json') as info_file:
 data = json.load(info_file)
 
with open('UserInfo.json') as user_info:
 user = json.load(user_info)
 
 
driver = webdriver.Chrome('chromedriver')
options = Options()
options.page_load_strategy = 'normal'


#Loops through the sotre list json file, takes the url and returns the status code
for count, store1 in data.items():
    
    checkUrl = store1['url']
    storeName = store1["name"]
    response = requests.get(checkUrl)
    statCode = response.status_code
    
    # if status code 200, the if statements opens the relevant store file 
    if statCode == 200:
     storeName = store1['name']
     # loads the store file to be used by the webdriver
     
     with open(storeName + '.json') as store_Name:
      shop = json.load(store_Name)
      driver.get(checkUrl)
      
      
      for count, closePopUpButton in shop.items():
       key_list = list(closePopUpButton)
       values = closePopUpButton.values()
       key_values = list(values)
       
       
      
       
       if key_list[0] == "button":
        
        driver.find_element_by_xpath(key_values[0]).click()
        
       elif key_list[0] == "input":
  
        
        if key_values[1] == "firstName":
         driver.find_element_by_xpath(key_values[0]).sendKeys(user['first name'])
        elif key_values[1] == "lastName":
         driver.find_element_by_xpath(key_values[0]).sendKeys(user['last name'])
        elif key_values[1] == "emailAddress":
         driver.find_element_by_xpath(key_values[0]).sendKeys(user['email Address'])
        elif key_values[1] == "number":
         driver.find_element_by_xpath(key_values[0]).sendKeys(user['number'])
         
        elif key_values[1] == "address":
         driver.find_element_by_xpath(key_values[0]).sendKeys(user['address'])
         
        
     time.sleep(15)
     #driver.quit()
    
    
    
 



 