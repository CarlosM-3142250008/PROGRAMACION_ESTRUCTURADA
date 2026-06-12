print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[23,33,45,8,24,0,100]
print(numeros)
lista=""
for i in numeros:  
    lista+=f"{i}, "
print("["+lista+"]")


lista=""
for i in range(0,len(numeros)):  
    lista+=f"{numeros[i]}, "
print("["+lista+"]")

lista=""
for i in range(0,len(numeros)):  
    lista+=f"{numeros[i]}, "
print("["+lista+"]")

p=0
lista=""
while p<len(numeros):
     lista+=f"{numeros[p]}, "
     p+=1
print("["+lista+"]")

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
#1ER FORMA
palabras=("UTD","tercer","cuatrimestre","TI")
palabra=input("Dame la palabra a buscar:").strip()

if palabra in palabras:
    print(f"encontro la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")
    
#2DA FORMA
palabras=("UTD","tercer","cuatrimestre","TI")
palabra=input("Dame la palabra a buscar:").strip() 
encontro=False
for i in palabras:
    if i==palabra:

        encontro=True
if encontro:
    print(f"encontro la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")

#3er FORMA
palabras=["UTD","tercer","cuatrimestre", "TI"]
palabra=input("Dame la palabra a buscar:").strip() 



# Ejemplo 3 Añadir elementos a la lista
lista=["",""]
#opcion 1
true=True 
while true:
    lista.append(input("Dame un valor").strip())
    opc=input("Ingresa True/False para continuar").strip().lower()
    if opc=="false":
        true=False
    
print(lista) 
  
# opcion 2
true="true"
while true=="true":
    lista.append(input("Dame un valor").strip())
    true=input("Ingresa True/False para continuar").strip().lower()
 
print(lista) 



#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda=[
        ["Manuel","6181234321"],
        ["Jose","6182365456"],
        ["Hector","6182376541"]
        ]
print(agenda)
for i in agenda:
    print(i)


lista=""
for u in range(0,len(agenda)):
    for o in range(0,len(agenda[u])):
        lista+=f"{agenda [u][o]},"
    lista+="\n"
print(lista)
