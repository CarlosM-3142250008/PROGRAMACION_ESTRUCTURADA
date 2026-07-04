import funciones
      
pelis={
    "nombre": "Toy story 5",
    "duracion": "120 min", 
    "idioma": "Espanol", 
    
    }      

def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t...:::: AGREGAR CARACTERISTICAS DE UNA PELICULA ::::...\n")
    caracteristica=input("Introducir el nombre de la caracteristica: ").lower().strip()
    valor=input("Introducir el valor de la caracteristica: ").upper().strip()
    pelis[caracteristica]=valor
    funciones.accionExitosa()

def mostrarPeliculas(pelis):
    print("\n\t\t...:::: MOSTRAR CARACTERISTICAS DE LA PELICULA ::::...\n")
    print("\Caracteristica\t\tValor\n")
    if len(pelis)>0:
        for i in pelis:
            print(f"{i+1}\t\t{pelis[i]}")
        funciones.espereTecla()
        
    else: 
        print("...::::No hay caracteristicas a mostrar de la pelicula::::...")
    
def limpiarPeliculas(pelis):
    opc=""
    if len(pelis)>0:
        while opc!="si" and opc!="no":
            
            opc=input("¿Deseas borrar todas las caracteristicas (Si/No)? ").lower().strip()
            
        else:
            input("...¡No hay peliculas que borrar!...") 
        
        if opc--"si":
            pelis=pelis.clear()
            funciones.accionExitosa()
        
def buscarPeliculas(pelis):
    print("\n\t\t...:::: BUSCAR UNA CARACTERISTICA DE LA PELICULA ::::...\n")
    caracteristica=input("Escribir el nombre de la caracteristica: ").upper().strip()
    
    no_encontro=False    
    for i in range(0,len(pelis)):
        if caracteristica==i:
            print("\Caracteristica\t\Valor\n")
            print(f"{i+1}\t\t{pelis[i]}")
            no_encontro=True
        funciones.espereTecla()
        
    else:
        if not(no_encontro):
            input("...¡No exite la pelicula que estas buscando, verifique!...")

def borrarPeliculas(pelis):
    posiciones=[]
    print("\n\t\t...:::: BORRAR UNA CARACTERISTICA DE LA PELICULA ::::...\n")
    caracteristica=input("Escribir el nombre de la caracteristica: ").upper().strip()
    no_encontro=True
    if no_encontro:
        for i in range(0,len(pelis)):
            if caracteristica==i:
                opc=""
                print("\Caracteristica\t\Valor\n")
                print(f"{i+1}\t\t{pelis[i]}")
                while opc!="si" and opc!="no":
                  opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
                if opc=="si":
                  pelis.pop(caracteristica) 
                  no_encontro=False
                  funciones.accionExitosa()
                  
    else:
        if not(no_encontro):
            input("...¡No exite la pelicula que estas buscando, verifique!...")
        
def modificarPeliculas(pelis):
    print("\n\t\t...:::: MODIFICAR EL VALOR DE LA CARACTERISTICA DE UNA PELICULA ::::...\n")
    caracteristica=input("Escribir el valor de la caracteristica: ").upper().strip()
    no_encontro= True
    if no_encontro:
        for i in range(0,len(pelis)):
            if caracteristica==i:
                print("\Caracteristica\t\Valor\n")
                print(f"{i+1}\t\t{pelis[i]}")
                opc=""
                while opc!="si" and opc!="no":
                    opc=input("¿Deseas modificar el valor de la caracteristica de la pelicula (Si/No)? ").lower().strip()
                    if opc=="si":
                        pelis[caracteristica]=input("Escribe el nuevo valor de la caracteristica: ").upper().strip()
                        funciones.accionExitosa()
    if not(no_encontro):
        input("...¡No exite la pelicula que estas buscando, verifique!...")