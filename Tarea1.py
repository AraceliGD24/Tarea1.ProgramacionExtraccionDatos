"""
Araceli Garcia Diaz
951
14/02/2024

Duplicados.
Desarrolle una función que dada una lista de números enteros,
retorna True si al menos un valor aparece dos veces, y Falso si todos los elementos son distintos.
"""

def duplicados(lista):
  num=set(lista)
  if len(lista)==len(num):
      return False
  else:
      return True

lista=[1,1,3,4,5]
print(duplicados(lista))


lista=[1,2,3,4,5,1]
print(duplicados(lista))

"""
Suma de dos números.
Dado una lista de números enteros y un valor entero (target), 
retorna el índice de los dos números que sumados sean igual al target. 
Debe asumir que existe siempre una única solución, y que un mismo elemento no se puede usar dos veces.
Debes retornar una tupla con los índices.

"""

def suma(nums,target):
    l={}
    for index,value in enumerate(nums):
        p=target- value
        if p in l:
            return (l[p],index)
        l[value]=index

nums= [2,5, 7, 11, 15]
target = 9
print(suma(nums,target))
#busquedaSuma(nums, target)
#(0, 1)

nums = [3, 2, 4]
target = 6
print(suma(nums,target))
#busquedaSuma(nums, target)
#(1, 2)

"""

Análisis de Población. 
Tienes datos sobre población de diferentes ciudades representados como tuplas (ciudad, población, área). 
Crea funciones para:

a. Calcular la densidad de población (población dividida por la cantidad total de población por área) para cada ciudad.
b. Identificar la ciudad con la mayor densidad de población.

Ejemplo:
ciudades = [	(“Tijuana”, 5, “NoroEste”), 
(“Ciudad de Mexico”, 8, “Centro”), 
(“Ensenada”, 3, “NoroEste”), 
(“Puebla”, 3, “Centro”), 
(“Cancun”, 4, “Sur”)
] 

	densidades = calcular_densidades(ciudades)
	mayor = mayor_densidad(ciudades)
	
print(densidades)
 # {“Tijuana”: 0.62, “Ciudad de Mexico”: 0.72, “Ensenada”: 0.37, “Puebla”:0.27, “Cancun”: 4}
	
print(mayor)
# “Ciudad de México”

"""

#def densidad(ciudades):
    #t={}
    #d={}
    #for ciudad,poblacion,zona  in ciudades:
    #    t[zona]=t.get(zona,0) + poblacion
   #     densi=poblacion/t[zona]
  #      t[ciudad] = round(densi,2)
 #   return t

#def MayorDensi(ciudades):
    #t={}
    #d={}
    #mc = ""  # cadena de texto
    #md = 0

    #for ciudad, poblacion, zona in ciudades:
       # t[zona] = t.get(zona, 0) + poblacion
      #  print(t)
     #   print("***********************")

    #for ciudad, poblacion, zona in ciudades:
        #densi = poblacion / t[zona]
       # d[ciudad] = round(densi, 2)
      #  print("////////////////////")
     #   print(d)
    #if densi < md:
      #  md=densi
     #   mc=ciudad
    #print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
    #print(md,mc)
    #return mc

def densidad(ciudades):
    t={}
    d={}
    for ciudad,poblacion,zona  in ciudades:
        t[zona]=t.get(zona,0) + poblacion
        densi=poblacion/t[zona]
        d[ciudad] = round(densi,2)
    return d

def MayorDensi(ciudades):
    t={}
    d={}
    mc = ""  # cadena de texto
    md = 0 #inicializar la comparacion del mayor

    for ciudad, poblacion, zona in ciudades:
        t[zona] = t.get(zona, 0) + poblacion
    for ciudad, poblacion, zona in ciudades:
        densi = poblacion / t[zona]
        d[ciudad] = round(densi, 2)

        if densi > md:
            md=densi
            mc=ciudad

    return mc

ciudades = [("Tijuana", 5, "NoroEste"),
            ("Ciudad de Mexico", 8, "Centro"),
            ("Ensenada", 3, "NoroEste"),
            ("Puebla", 3, "Centro"),
            ("Cancun", 4, "Sur")
            ]

Densidad_total=densidad(ciudades)
mayot=MayorDensi(ciudades)

print("Densidades:\n",Densidad_total)
print("Mayor densidad:",mayot)


"""
4.-Estadística Básica. 
Cree una clase llamada Estadística que contiene como atributo una lista de números naturales la cual puede contener repetidos.

Debe contener los siguientes métodos:

Frecuencia de Números. Dada la lista, devuelve un diccionario con el número de veces que aparece cada número en la lista.

Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido). Puedes usar la función anterior como ayuda.

Histograma. Dada la lista, muestra el histograma de la lista. Puedes reusar los métodos anteriores. 

Ejemplo:
		lista = ListaNumeros ([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
		lista.histograma()

	Salida:
1 *****
2 ******
3 ****
4 **


"""

class Estadistica:
    def __init__(self,listaNumeros):
        self.listaNumeros = listaNumeros

    def frecuencia(self):
        repetidos={}
        for x in listaNumeros:
            repetidos[x]=repetidos.get(x,0) + 1
        return repetidos

    def moda(self):
        moda=self.frecuencia()
        m=max(moda,key=moda.get)
        return m

    def histograma(self):
        h = self.frecuencia()

        for i in sorted(h):
            print(f"{i}:{h[i]*'*'}")


listaNumeros=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,10,10]

print("Frecuencia de Numeros:")
print(Estadistica(listaNumeros).frecuencia())

print("Moda:")
print(Estadistica(listaNumeros).moda())

print("Histograma:")
print(Estadistica(listaNumeros).histograma())

"""
5.-Detección de Cambios en Datos. 
Imagina tener dos conjuntos de datos que representan el estado actual y el estado anterior de un sistema.
Crea una función que identifique los elementos que han cambiado entre los dos conjuntos. 
Retorna un diccionario usando como la llave el estado anterior y como valor el estado actual. 
Para este ejercicio pueden asumir que los datos son numéricos y/o cadenas.

"""
def cambio(anterior,actual):
    cambios={}
    for index, valor in  zip(anterior,actual):
        if  not index==valor :
            cambios[index]=valor
    dic= dict(zip(anterior,actual))
    print(dic)



    return cambios




anterior= ["Cardiologia","Pediatria","Cirugia General","Analisis clinicos"]
actual=["Cardiologia","Pediatria","Cirugia General","Traumatologia"]

listaCam=cambio(anterior,actual)
print(listaCam)


"""
Sistema de Reserva. Desarrolla un sistema de reservas utilizando sets. 
Crea conjuntos para representar habitaciones disponibles y habitaciones  reservadas en un hotel.
Permite a los usuarios realizar reservas, liberar habitaciones y mostrar la disponibilidad actual. 
NOTA: No utilizar menú,  solo las funciones , realizar las pruebas necesarias para verificar funcionamiento adecuado.
"""

class Reservas():
    def __init__(self,disponibles):
        self.disponibles=set(disponibles)
        self.reservadas=set()

    def reservar(self):
        numR=int(input("Intoduce numero de habitacion que desea:"))
        if numR in self.disponibles:
            self.disponibles.remove(numR)
            self.reservadas.add(numR)
            print("Habitacion",numR, "reservada con exito!!")
        else:
            print("La habitacion",numR, "no esta disponible")

        
    
    def liberarhabi(self):
        nl=int(input("Intoduce numero de habitacion que desea:"))
        if nl in self.reservadas:
            self.reservadas.remove(nl)
            self.disponibles.add(nl)
            print("Habitacion liberada")
        else:
            print("habitacion no esta reservada")


            

    def mostrar(self):
       print("Habitaciones disponibles:",self.disponibles)
       print("Habitaciones Reservadas:",self.reservadas)
          
disponibles=[1,2,3,4,5]

sistema=Reservas(disponibles)
print("Reservar")
sistema.reservar()
print("*********************")
print("Liberar")
sistema.liberarhabi()
print("*********************")
sistema.mostrar()
print("*********************")

"""
   Encriptación y Desencriptación de Mensajes Secretos. 
   Tú y tu mejor amigo están creando un sistema secreto para enviar mensajes entre ustedes sin que nadie más pueda entenderlos. 
   Deciden utilizar un método de encriptación y desencriptación basado en listas o diccionarios.
   
   Parte 1: Encriptación. Crear una función llamada encriptar_mensaje que tome como entrada un mensaje de texto
            y utilice un diccionario para reemplazar cada letra por un código secreto. 
            El diccionario de encriptación debe asignar a cada letra una cadena de caracteres alfanuméricos aleatorios. 
         
   Ejemplo de diccionario:
          diccionario_encriptacion = {'a': '$%3', 'b': '8@*', 'c': '2&9', ...}
   
   Parte 2: Desencriptación. Crear una función llamada desencriptar_mensaje que tome como entrada un mensaje encriptado y 
            utilice el mismo diccionario para revertir el proceso y obtener el mensaje original.

"""


def encriptar_mensaje(mensaje,diccionario_encriptacion):
    encri=""
    for x in mensaje:
        if x in diccionario_encriptacion:
            encri = encri + diccionario_encriptacion[x]
        else:
            encri = encri + x
    return encri

def desencriptar_mensaje(mensaje,diccionario_encriptacion):
    for i,j in diccionario_encriptacion.items():
        mensaje=mensaje.replace(j,i)
    return mensaje

mensaje="hola tengo un chisme, blanca"

diccionario_encriptacion = {'a': '$%3', 'b': '8@*', 'c': '2&9', 'd': '#7$', 'e': '*0@', 'f': '!1%',
    'g': '&5*', 'h': '4^%', 'i': '@2#', 'j': '%6!', 'k': '9*$', 'l': '3&@',
    'm': '^@1', 'n': '$@*', 'o': '&%8', 'p': '7!$', 'q': '1@%', 'r': '*&2',
    's': '!3^', 't': '5*%', 'u': '%^$', 'v': '6@!', 'w': '*&%', 'x': '@^!',
    'y': '0$%', 'z': '!@4' }


print("Mensaje encriptado:",encriptar_mensaje(mensaje, diccionario_encriptacion))

print("Mensaje desencriptado:",desencriptar_mensaje(mensaje, diccionario_encriptacion))



"""
    Inventario de Productos. 
    Gestiona un inventario de productos en una tienda utilizando diccionarios. 
    Las claves pueden ser los códigos de producto y los valores
    pueden ser diccionarios con información como el nombre, precio y cantidad en stock.
    Debe tener funciones para agregar, editar, eliminar producto, además de funciones para realizar venta e imprimir inventario.
"""

class Inventario():
    def __init__(self,productos):
        self.productos=productos
    def agregar(self):
        clave=input("Igrese clave del producto:")
        if clave not in self.productos:
            nombre = input("Nombre del producto:")
            precio = float(input("Precio:"))
            cantidad = float(input("Cantidad"))
            self.productos[clave]={'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
            print(self.productos[clave])
        else:
            print("clave ya existe")

        return clave

    def editar(self):
        clave=input("Ingrese la clave del producto a editar:")
        if clave in self.productos:
            nombre = input("Nombre del producto:")
            precio = float(input("Precio:"))
            cantidad = float(input("Cantidad"))
            self.productos[clave] = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
            print(self.productos[clave])
        else:
            print("clave no existe en el inventario")

    def eliminar(self):
        clave = input("Ingrese la clave del producto que desea eliminar:")
        if clave in self.productos:
            self.productos.pop(clave)
            print("Producto eliminado")
        else:
            print("clave no existe en el inventario")
    def venta(self):
        venta=input("Ingrese nombre del producto:")
        e=0
        for c in self.productos.values():
            if c['nombre']==venta:
                e=1
                cant=int(input("Ingrese la cantidad que desea comprar:"))
                if cant <= c['cantidad']:
                    print("realizar compra")
                else:
                    print("limite de cantidad")
        if e==0:
            print("No ENCONTRADO")


        return venta

    def Imprimir(self):
        return self.productos








productos= {'001': {'nombre': 'Camiseta', 'precio': 15.99, 'cantidad': 50},
    '002': {'nombre': 'Pantalon', 'precio': 29.99, 'cantidad': 30},
    '003': {'nombre': 'Zapatos', 'precio': 49.99, 'cantidad': 20},
    '004': {'nombre': 'Gorra', 'precio': 9.99, 'cantidad': 40},
    '005': {'nombre': 'Mochila', 'precio': 39.99, 'cantidad': 25}}


print(Inventario(productos).agregar())
print(Inventario(productos).editar())
print(Inventario(productos).eliminar())
print(Inventario(productos).venta())
print(Inventario(productos).Imprimir())






