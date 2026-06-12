# 1er utilizar los modulos 
import modulos
modulos.borrarpantalla()
modulos.funcion1()

nom="Daniel"
ape="Carreon"
name,lastname=modulos.funcion4(nom,ape)
print(f"Nombre{name}\nApellidos:{lastname}")

#2da formar de utilizar modulos
#from  modulos import * (el * sirve para importar todas las funciones de el modulo)

from  modulos import borrarpantalla,funcion1,funcion4
borrarpantalla()
funcion1()

nom="Daniel"
ape="Carreon"
name,lastname=modulos.funcion4(nom,ape)
print(f"Nombre{name}\nApellidos:{lastname}")