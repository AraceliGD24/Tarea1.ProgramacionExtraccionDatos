"""
Araceli Garcia Diaz         8/03/2024
Paso 1. Atender las indicaciones del profesor.

Paso 2.  Investigar sobre el proceso de automatización usando la libreria Selenium.

Paso 3. Realizar una función en python que reciba el nombre de un producto en Amazon y la cantidad de paginas.

Paso 4. La función debe automatizar la busqueda del producto y tomar una impresión de pantalla de la cantidad de paginas indicada en el parametro de la funciónPaso 1. Atender las indicaciones del profesor.

Paso 2.  Investigar sobre el proceso de automatización usando la libreria Selenium.

Paso 3. Realizar una función en python que reciba el nombre de un producto en Amazon y la cantidad de paginas.

Paso 4. La función debe automatizar la busqueda del producto y tomar una impresión de pantalla de la cantidad de paginas indicada en el parametro de la función
"""
#importar librerias
import time
from selenium import webdriver
from selenium.webdriver.common.by import By  #para hacer el control del bots By es para hacer una busqueda
from selenium.webdriver.chrome.service import Service  #Es para conectarme
from selenium.webdriver.chrome.options import Options #es para seleccionar

from webdriver_manager.chrome import ChromeDriverManager

#crear la funcion del bots para que busque la informacion
def busquedaAmazon(producto,cant,index):
    #realizar la descargar necesaria para utilizar la version adaptable a chrome
    s=Service(ChromeDriverManager().install()) #ir a una pagina de chrome y va instalr su version mas actual de chrome
    options = Options() #como se es
    options.add_argument("--Window-size=1020,1200")  #dos obejos con diferentes funciones
    navegador= webdriver.Chrome(service=s,options=options)
    navegador.get("https://www.amazon.com.mx//")
    time.sleep(15)
    #bpton para indicar en donde va escribir el producto que desea buscar
    txtbusqueda = navegador.find_element(By.NAME,"field-keywords")
    #boton para indicar que busque la informacio
    btnboton = navegador.find_element(By.ID,"nav-search-submit-button")
    #mandando a buscar el objeto
    txtbusqueda.send_keys(producto)
    #determino el tiempo que va esperar para hacer el proceso
    time.sleep(5)
    #indico el objeto al cual tendra que picar en la pagina para buscar
    btnboton.click()
    #creacion de un ciclo for para que siga un proceso hasta n veces
    for index in range(cant):
        #hacer una captura lo de index + 1 es para saber la pagina de la cual se realizo la captura
        navegador.save_screenshot(f"imagenes/pagina{index + 1}.png")  # para hacer una captura
        #indicando el boton siguiente
        Sigboton=navegador.find_element(By.CLASS_NAME,"s-pagination-next")
        # indico el objeto al cual tendra que picar e ir a la siguiente pagina
        Sigboton.click()
        #tiene el tiempo de 3 segundos para poder realizar esa tarea
        time.sleep(3)
        #Guardadndo la imagen en una carpetea referente al tema
        navegador.save_screenshot (f"imagenes/pagina{index+1}.png") #para hacer una captura

    time.sleep(20)


if __name__ == "__main__":
    busquedaAmazon("Mochilas",5,0)
