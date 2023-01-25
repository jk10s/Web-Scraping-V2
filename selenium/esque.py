from selenium import webdriver
import time

def drivere():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    expot=[
        "enable-automation",
        "ignore-certificate-error",
        "enable-logging"
    ]
    chrome_options.add_experimental_option("excludeSwitches", expot)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    return driver

if __name__=='__main__':
    driver=drivere()
    url = 'https://www.google.com/'
    driver.get(url)
    time.sleep(200)