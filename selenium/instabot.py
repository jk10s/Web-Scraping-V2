from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys #para teclas especiaeles
import time
import sys
import os
import pickle #para crear y cuardar ls cookies
from crede import *
import wget # para descargar archivos desde internet offf 


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


def cursor_arriba(n=1):
    print(f'\033[{n}A', end="")
def raya():
    print('-'*os.get_terminal_size().columns)
def login_inta():
    print("logeando la pagina de instagram por cookies")
    if os.path.isfile("guardadodecookies.cookies"):
        cookies = pickle.load(open("guardadodecookies.cookies", "rb"))
        driver.get("https://www.instagram.com/robots.txt")
        for cooki in cookies:
            driver.add_cookie(cooki)
        driver.get("https://www.instagram.com")
    #input("pausa..")
        
    print("login agina de instagram desde cero")
    driver.get('https://www.instagram.com/')
    cursor_arriba()
    try:
        usernamex = wait.until(ec.visibility_of_element_located((By.NAME, "username")))
    except TimeoutException:
        print('ERROR elemento "username" no disponible')
        return "ERROR"
    #usernamex  = driver.find_element(By.NAME, "username")

    print("introdur usario")
    usernamex.send_keys(useri)
    cursor_arriba()
    print("introducionendo usario OK")
    print("introdur contraseña ")
    contrax  = driver.find_element(By.NAME, "password")
    contrax.send_keys(contrai)
    cursor_arriba()
    print("introducionendo contraseña OK")
    print("clic en iniciar sesion")
    #driver.find_element(By.XPATH, "//form[@id='loginForm']/div/div[3]/button/div").click()
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print("inicioando sesion OK")
    print("click en guardar informacion")
    wait.until(ec.element_to_be_clickable((By.XPATH,"//button[text()='Guardar información']"))).click()# para hace click en elemento usann wait
    print("guardar info OK")
    cursor_arriba()
    
    #driver.find_element(By.CCS_SELECTOR, "button[type='submit']").click()
    #xpath=//button/div
    print("comprobando si el login es correcto")
    try:
        elemento= wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, "article[role='presentation']")))
        print("login desde ok")
    except TimeoutException:
        print(" ERROR: el feef de noticas no ha cargado")
        return "ERROR"
    return "OK"
    
    cookies = driver.get_cookies()
    pickle.dump(cookies, open("guardadodecookies.cookies", "wb"))
    print("cookies guardas")

def descargarft(hashtag, minimo):
    print(f"buscando hashtag #{hashtag}")
    driver.get(f'https://www.instagram.com/explore/tags/{hashtag}')
    # print(f"si busco la varible  hashtag #{hashtag}")
    # elemento = driver.find_element(By.CSS_SELECTOR, "html")
    #elemento = driver.find_element(By.CSS_SELECTOR, "html")
    url_fotos= set()

    while len(url_fotos) < minimo:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # elemento.send_keys(Keys.PAGE_DOWN) 
        # time.sleep(0.5)
        # elemento = driver.find_element(By.CSS_SELECTOR, "div._aagu")
        elementos = driver.find_elements(By.CSS_SELECTOR, "div._aagu")
        for elemento in elementos:
            try:
                url = elemento.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
                url_fotos.add(url)
            except:
                pass
        print(f' Total de fotos: {len(url_fotos)}')
        cursor_arriba()
        
    #crear unacarpeta
    if not os.path.exists(hashtag):
        os.mkdir(hashtag)
    #descargar las imahenes del conjunto
    n=0
    for url_foto in url_fotos:
        n+=1
        print(f' Decargando {n} de {len(url_fotos)}')
        nombre_archivo=wget.download(url_foto, hashtag)
        cursor_arriba()
        print(f'\33[K descaargando {nombre_archivo}')
        print()
    return len(url_fotos)

if __name__=='__main__':
    modo_de_uso = f'modo de uso:\n'
    modo_de_uso+= f'{os.path.basename(sys.executable)} {sys.argv[0]} hashtag [minimo]\n\n' 
    modo_de_uso+= f' opciones:\n'
    modo_de_uso+= f'minimo : minimi de descargas a relizar (por defecto 300)\n\n'
    modo_de_uso+= f'Ejemplos:\n'
    modo_de_uso+= f'{os.path.basename(sys.executable)} {sys.argv[0]} cats \n' 
    modo_de_uso+= f'{os.path.basename(sys.executable)} {sys.argv[0]} superman 100 \n'
    #control de parametros 
    if len(sys.argv) == 1 or len(sys.argv)>3:
        print(modo_de_uso)
        sys.exit(1)
    elif len(sys.argv)==3:
        if sys.argv[2].isdigit():
            MINIMO = int(sys.argv[2])
        else:
            print(f"ERROR {sys.argv[2]}no es un numero")
            sys.exit(1)
    else:
        MINIMO = 300
    HASHTAG = sys.argv[1].strip('#')
    
    driver=drivere()
    wait = WebDriverWait(driver, 10)
    res = login_inta()
    if res == "ERROR":
        input("pulsa ENTER oara salir...")
        driver.quit()
        sys.exit(1)
    raya()
    descargarft(HASHTAG,MINIMO)
    print(f'se has descargado {res} fotos')
        
    input("pulsa enter para salir")
    # driver.quit()

    
    driver.quit()