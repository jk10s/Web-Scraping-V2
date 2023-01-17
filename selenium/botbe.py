from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
website = 'https://betplay.com.co/'
path = 'chromedriver_linux64/chromedriver' 

# define 'driver' variable
driver = webdriver.Chrome(path)
driver.maximize_window()
# open Google Chrome with chromedriver
driver.get(website)

usuario = driver.find_element(By.ID, "dropdownLogin")

#usuario = driver.find_element_by_id("identifierId")
time.sleep(5)
#usuario.send_keys("eventosjcv2014@gmail.com")
usuario.send_keys(Keys.ENTER)
username = driver.find_element(By.ID, "userName")
username.send_keys("1050692513") 
passwordd = driver.find_element(By.ID, "password")
passwordd.send_keys("7894561230Ju") 
iniciase = driver.find_element(By.ID, "btnLoginPrimary").click()


time.sleep(2)




# Navigate to YouTube
driver.get('https://betplay.com.co/slots/launchGame?gameCode=SPB_aviator&flashClient=true&additionalParam=&integrationChannelCode=PARIPLAY')