import mysql.connector
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
RESET = "\033[0m"
VERDE = "\033[1;32m"
NEGRITA = "\033[1m"
def conectar():
    return mysql.connector.connect(
        host="localhost",      
        user="root",          
        password="",           
        database="stockmaster_db"  
    )

conexion = conectar()

def borrarPantalla():
    print("\033c")

def opcionInvalida():
    input(f"\n\t\t{ROJO}...¡Opción inválida, por favor verifique!...{RESET}{AMARILLO}\n\t\t    ...¡Oprima ENTER para continuar!...{RESET}")

def espereTecla():
    input(f"\n\t\t{NEGRITA}    ...¡Oprima  ENTER para continuar!...{RESET}")

def accionExitosa():
    input(f"\n\t\t{VERDE}...¡Acción Realizada con Éxito!...{RESET}")

def accionNoExitosa():
    input(f"\n\t\t{AMARILLO}...¡No fue posible realizar esta acción, inténtalo más tarde!...{RESET}")