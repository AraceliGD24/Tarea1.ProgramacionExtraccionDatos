"""
Araceli Garcia Diaz 951    16/03/2024
1.-Escribir un programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:

Mes :Enero   ,Febrero,   Marzo,    Abril

Ventas:30500,35600,28300,33900

Gastos:22000,23400,18100,20700

"""

#IMPORTAR LIBRERIAS
import pandas as pd


#CREAR LA FUNCION CORRESPONDIENTE DENTRO DEL PARAMETRO ESTA EL NOMBRE DEL DICCIONARIO REALIZADO CON SU TIPO DE DATO
def crear_dataframe(datos:dict):
    #INDICAMOS EN UNA VARIABLE LA CREACION DE UN DATAFRAME DE LOS DATOS
    df=pd.DataFrame(datos)
    return  df




#Bloque de codigo para imprimir la funcion
if __name__ == "__main__":
    datos={"Mes":["Enero","Febrero","Marzo","Abril"],
           "Ventas":[30500,35600,28300,33900],
           "Gastos":[22000,23400,18100,20700]}

    df=crear_dataframe(datos)
    print(df)
