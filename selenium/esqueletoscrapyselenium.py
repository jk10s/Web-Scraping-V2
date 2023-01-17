#from webdriver_manager.chome import chromedriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
website = 'https://betplay.com.co/'
path = 'chromedriver_linux64/chromedriver' 

def iniciar_chome():
    options = Options()
    user_agent = "Mozilla/5.0(Wiin"