"""
Araceli Garcia Diaz 951    16/03/2024

    2.-El archivo cotización.csv visto en clase contiene las cotizaciones de las empresas del IBEX35
       con las siguientes columnas:
       nombre (nombre de la empresa),
       Final (precio de la acción al cierre de bolsa),
       Máximo (precio máximo de la acción durante la jornada),
       Mínimo (precio mínimo de la acción durante la jornada),
       volumen (Volumen al cierre de bolsa),
       Efectivo (capitalización al cierre en miles de euros).
       Construir una función que construya un DataFrame a partir del archivo con el formato anterior
       y devuelve otro DataFrame con el mínimo, el máximo y la media de cada columna.


"""

#IMPORTAR LIBRERIAS
import pandas as pd


#CREACION DE LA FUNCION PARA CREAR UN DATAFRAME Y DEVOLVER OTRO DATAFRAME CON EL MINIMO , MAXIMO Y MEDIA DE LA COLUMNA
def crear_dataframe_cotizacion(path,sepradaor=",",decimal=".",miles=None):
    #EN UNA VARIABLE CONVERTIMOS EL ARCHIVO A DATAFRAME
    datos = pd.read_csv(path, sep=sepradaor,decimal=decimal, thousands=miles)

    #EN UNA VARIABLE IDENTIFICO LA SELECCION DEL TIPO DE DATO QUE VOY A UTILIZAR SOLAMENTE
    num=datos.select_dtypes(include=["float64","int64"])

    #EN DIFERENTES VARIABLES INDICO LAS FUNCIONES QUE VOY A UTILIZAR PARA IMPRIMIR LOS RESULTADOS
    minimo=num.min()
    maximo=num.max()
    medias=num.mean()
    #DICCIONARIO DE LO QUE QUIERO EN MI DATAFRAME
    datos2={"Minimo":minimo,
            "Maximo":maximo,
            "Mean":medias
            }
    #CONVIERTO EL DICCIONARIO EN DATAFRAME
    df2= pd.DataFrame(datos2)

    print(datos)
    print("///////////////////////////////////")
    print(df2)

    return datos,df2



#Bloque de codigo para imprimir la funcion
if __name__ == "__main__":

    crear_dataframe_cotizacion("DataSet/cotizacion.csv", ";", ",", ".")





