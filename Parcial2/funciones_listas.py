"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""


#Funciones más comunes en las listas
numeros=[23,45,8,24]
varios=[33,3.1416,"hola",True]
vacio=[]
#print(paises)
print(numeros)
print(varios)
print(vacio)

#Imprimir el contenido de una lista


#Recorrer la lista 
#1er forma 
paises=["Mexico","Canada","EUA","Mexica"]

for i in paises:
    print(i)

# #2do forma 
for i in range (0,len(paises)):
    print(paises[i])


#ordenar elementos de una lista
print(paises)
paises.sort()
print(paises)

#dar la vuelta a una lista
paises.reverse()
print(paises)

#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Colombia")
print(paises)
paises.insert(8,"Polonia")
#Eliminar, borrar, suprimir, un elemento de una lista
paises=["Mexico","Canada","EUA","Mexica"]
print(paises)
#1er forma
paises.pop(3)
print(paises)

#2da forma 
paises.remove("EUA")
print(paises)

#Buscar un elemento dentro de la lista
encontro="EUA" in paises
print(encontro)
#Contar el numeros de veces que aparece un elemento dentro de una lista
numeros=[23,45,8,24,23,100,23]
paises=["Mexico","Canada","EUA","Mexica"]

num_veces=numeros.count(23)
print(f"el valor 23 aparece {num_veces}")

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
paises=["Mexico","Canada","EUA","Mexico"]

for i in range(0,len(paises)):
    if paises [i]=="Mexico":
        posicion=i
        print(f"encontre el valor en la posicion {posicion}")


#Unir el contenido de una lista dentro de otra lista
numero1=[23,45,8,24,23,100,23]
numero2=[100,-100]
print(numero1)
print(numero2)
numero1.extend(numero2)
print(numero1)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente
numero1.sort()
numero1.reverse()
print(numero1)



