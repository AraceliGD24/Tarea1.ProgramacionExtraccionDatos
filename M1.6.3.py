"""
Araceli Garcia Diaz 951    16/03/2024

3.-El archivo titanic.csv visto en clase contiene información sobre los pasajeros del Titanic.
   Escribir un programa con los siguientes requisitos:
    a)Generar un DataFrame con los datos del archivo.
    b)Mostrar el número de datos que contiene y los nombres de sus columnas.
    c)Mostrar las 10 primeras filas.
    d)Mostrar las 10 últimas filas.
    e)Mostrar 10 filas de manera aleatoria.

"""

#IMPORTAR LIBRERIAS
import pandas as pd

#CREACION DE UNA FUNCION PARA OBTENER LOS PUNTOS
def crear_dataframa_calculos_titanium(path,sepradaor=",",decimal=".",miles=None):
    #EN UNA VARIABLE CONVERTIMOS EL ARCHIVO EN UN DATAFRAME
    datos = pd.read_csv(path, sep=sepradaor,
                        decimal=decimal, thousands=miles)  # Sep para indicar cual es el separador de datos
    return datos  # va hacer un dataframe

#Bloque de codigo para imprimir la funcion
if __name__ == "__main__":
    df_titanic = crear_dataframa_calculos_titanium("DataSet/titanic.csv")
    print("Numero de datos y nombre columnas")
    print(df_titanic.info())
    print("Los primeros 10 elementos")
    print(df_titanic.head(10))
    print("Los ultimos 10 elemnetos")
    print(df_titanic.tail(10))
    print("10 datos aleatorios")
    print(df_titanic.sample(10))
