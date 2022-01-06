import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'normal'




driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.


url = 'https://www.kmart.com.au/product/18mp-digital-camera---black/3714304'



driver.get(url);

#driver.find_element_by_xpath("/html/body/div[19]/div[2]/div/div/div[1]/a").click()
#driver.find_element_by_xpath("/html/body/div[11]/section[1]/div[7]/div/div[1]/div[1]").click()



#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/main/div/div/div[2]/div[1]/form[2]/button").click()

time.sleep(20)


driver.quit()
