"""
Araceli Garcia Diaz 951     10/03/2024
Modificar la función de la Meta 1.3 para que en lugar de tomar los screenshot extraega
el nombre, rating, precio, fecha de entrega de cada uno de los productos de la busqueda
tomando como límite la cantidad de paginas especificadas.
 La función debe de retornar un dataframe y crear un archivo csv con la información recabada.
"""

#Importar librerias
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By  #para hacer el control del bots By es para hacer una busqueda
from selenium.webdriver.chrome.service import Service  #Es para conectarme
from selenium.webdriver.chrome.options import Options #es para seleccionar
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup

def busquedaAmazon(producto,cant):
    #realizar la descargar necesaria para utilizar la version adaptable a chrome
    s=Service(ChromeDriverManager().install()) #ir a una pagina de chrome y va instalr su version mas actual de chrome

    options = Options() #como se es
    options.add_argument("--Window-size=1020,1200")  #dos obejos con diferentes funciones
    navegador= webdriver.Chrome(service=s,options=options)
    navegador.get("https://www.amazon.com.mx//")
    time.sleep(15)

    #indicar en donde esta ubicado los botones que se van a necesitar
    txtbusqueda = navegador.find_element(By.NAME,"field-keywords")
    btnboton = navegador.find_element(By.ID,"nav-search-submit-button")
    txtbusqueda.send_keys(producto)
    time.sleep(5)
    btnboton.click()


    #crear un diccionario para guardar la informacion
    all_info = {"Nombre": [],
                "Raiting": [],
                "Precio": [],
                "Fecha": []}
    #Crear un ciclo para que termine hasta n cantidad de paginas
    for index in range(cant):
        soup = BeautifulSoup(navegador.page_source, "html5lib")
        cuadro = soup.find("div", attrs={"class": "a-section a-spacing-base"})
        renglones = cuadro.findAll("div")

        for x in renglones:
            nombre=x.find("span",{"class":"a-size-base-plus"})
            raiting =x.find("span",{ "class":"a-icon-alt"})
            precio = x.find("span",{ "class":"a-offscreen"})
            fecha=x.find("span",{ "class": "a-text-bold"})

            if nombre is not None:
                all_info["Nombre"].append(nombre.text)
            else:
                all_info["Nombre"].append("No hay nombre")

            if raiting is not None:
                all_info["Raiting"].append(raiting.text)
            else:
                all_info["Raiting"].append("No hay rating")

            if precio is not None:
                all_info["Precio"].append(precio.text)
            else:
                all_info["Precio"].append("No hay precio")


            if fecha is not None:
                all_info["Fecha"].append(fecha.text)
            else:
                all_info["Fecha"].append("No hay fecha")



        Sigboton=navegador.find_element(By.CLASS_NAME,"s-pagination-next")
        Sigboton.click()
        time.sleep(5)

        df = pd.DataFrame(all_info)
        df.to_csv("DataSet/Amazon.csv")
    time.sleep(20)

if __name__ == "__main__":
    busquedaAmazon("Mochilas",5)