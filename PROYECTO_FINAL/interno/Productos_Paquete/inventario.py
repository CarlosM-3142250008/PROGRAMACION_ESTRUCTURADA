from interno import funciones
from interno.Productos_Paquete import crud
from interno.Categorias_Paquete import crud_categorias

AZUL = "\033[1;34m"
VERDE = "\033[1;32m"
CYAN = "\033[1;36m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
RESET = "\033[0m"

def MenuPrincipal():
    print(f"{AZUL}=============================================================={RESET}")
    print(f"{CYAN}\t\t 📦 SISTEMA DE GESTIÓN E INVENTARIO{RESET}")
    print(f"{AZUL}=============================================================={RESET}\n")
    print(f"\t{VERDE}1.{RESET} 📂 Categorías")
    print(f"\t{VERDE}2.{RESET} 🏷️  Productos")
    print(f"\t{VERDE}3.{RESET} 💲 Ventas y Stock")
    print(f"\t{VERDE}4.{RESET} 📜 Ver Historial")
    print(f"\t{ROJO}5.{RESET} 🚪 Salir\n")
    print(f"{AZUL}--------------------------------------------------------------{RESET}")
    return input(f"{AMARILLO}Seleccione una opcion: {RESET}").strip()

def pedirConfirmacion(mensaje, funcion_exito, mensaje_cancelacion):
    resp = input(f"\n{AMARILLO}{mensaje}{RESET} ({VERDE}s{RESET}/{ROJO}n{RESET}): ").strip().lower()
    if resp == 's':
        funcion_exito()
    elif resp == 'n':
        print(f"\n{ROJO}✖ Operación cancelada:{RESET} {mensaje_cancelacion}")
        funciones.espereTecla()
    else:
        print(f"\n{ROJO}⚠️  Opción no válida.{RESET} Ingrese únicamente [{VERDE}s{RESET}] para Sí o [{ROJO}n{RESET}] para No.")
        pedirConfirmacion(mensaje, funcion_exito, mensaje_cancelacion)

def mostrarExito(mensaje_detalle=""):
    print(f"\n{VERDE}✓ Acción realizada con éxito.{RESET}")
    if mensaje_detalle:
        print(f"{CYAN}➜ {mensaje_detalle}{RESET}")
    funciones.espereTecla()

def mostrarTablaProductos(productos):
    print(f"{CYAN}{'ID':<5}|{'NOMBRE':<20}|{'PRECIO':<10}|{'STOCK':<10}|{'CATEGORIA':<10}{RESET}")
    print(f"{AZUL}" + "-" * 60 + f"{RESET}")
    for i, nombre, precio, stock, cat_nombre in productos:
        print(f"{VERDE}{i:<5}{RESET}|{nombre:<20}|${precio:<9.2f}|{stock:<10}|{cat_nombre:<10}")

def verHistorial():
    funciones.borrarPantalla()
    print(f"{AZUL}=============================================================={RESET}")
    print(f"{CYAN}\t\t 📜 HISTORIAL DE MOVIMIENTOS{RESET}")
    print(f"{AZUL}=============================================================={RESET}\n")
    try:
        cursor = funciones.conexion.cursor()
        cursor.execute("SELECT id, movimiento, fecha FROM historial ORDER BY id DESC")
        registros = cursor.fetchall()
        cursor.close()

        if not registros:
            print(f"\t{AMARILLO}⚠️ No hay movimientos registrados en la base de datos.{RESET}\n")
        else:
            print(f"\t{CYAN}{'ID':<6} | {'FECHA Y HORA':<20} | {'DESCRIPCIÓN'}{RESET}")
            print(f"\t{AZUL}" + "-" * 60 + f"{RESET}")
            for reg in registros:
                fecha_str = reg[2].strftime("%Y-%m-%d %H:%M:%S") if reg[2] else "N/A"
                print(f"\t{VERDE}#{reg[0]:<5}{RESET} | {fecha_str:<20} | {reg[1]}")
    except Exception:
        funciones.accionNoExitosa()
        return

    print(f"\n{AZUL}--------------------------------------------------------------{RESET}")
    funciones.espereTecla()

def consultarInventario():
    try:
        funciones.borrarPantalla()
        print(f"{CYAN}\n\t...::: LISTA DE PRODUCTOS :::...\n{RESET}")
        productos = crud.consultar()
        if productos:
            mostrarTablaProductos(productos)
        else:
            print(f"\t{AMARILLO}⚠️ No hay productos registrados en la base de datos.{RESET}")
    except Exception as e:
        print(f"Error al mostrar inventario: {e}")
    funciones.espereTecla()

def buscarProducto():
    try:
        funciones.borrarPantalla()
        print(f"{CYAN}\n\t...:::: BUSCAR PRODUCTOS ::::...\n{RESET}")
        id_prod = input("Escribir el ID del producto: ").strip()
        if not id_prod.isdigit():
            funciones.opcionInvalida()
            return

        prod = crud.buscar(id_prod)
        if prod:
            mostrarTablaProductos(prod)
        else:
            print(f"\t{AMARILLO}⚠️ No se encontró el producto solicitado.{RESET}")
    except Exception as e:
        print(f"Error al buscar producto: {e}")
    funciones.espereTecla()

def agregarProducto():
    try:
        funciones.borrarPantalla()
        print(f"{CYAN}\n\t...::: AGREGAR PRODUCTO :::...\n{RESET}")
        nombre = input("Nombre: ").strip()
        if not nombre:
            funciones.opcionInvalida()
            return

        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))

        cats = crud_categorias.consultar()
        if not cats:
            print(f"\n\t{AMARILLO}⚠️ Primero debes registrar al menos una categoría.{RESET}")
            funciones.espereTecla()
            return

        print(f"\n{AZUL}--- Categorías Disponibles ---{RESET}")
        ids_validos = []
        for c in cats:
            print(f"{VERDE}ID: {c[0]:<3}{RESET} | Categoría: {c[1]}")
            ids_validos.append(str(c[0]))

        cat_id_input = input("\nID de la Categoría seleccionada: ").strip()
        if not cat_id_input.isdigit() or cat_id_input not in ids_validos:
            funciones.opcionInvalida()
            return

        cat_id = int(cat_id_input)

        print(f"\n{AZUL}--- RESUMEN DE CAMBIOS ---{RESET}")
        print(f"Acción: Registro de nuevo producto")
        print(f"Nombre: {nombre}")
        print(f"Precio: ${precio:.2f}")
        print(f"Stock inicial: {stock}")
        print(f"ID Categoría: {cat_id}")

        def ejecutar_agregar():
            if crud.agregar_producto(nombre, precio, stock, cat_id):
                mostrarExito(f"Se agregó correctamente el producto '{nombre}'.")
            else:
                funciones.accionNoExitosa()

        pedirConfirmacion(
            "¿Estás seguro de agregar este producto?",
            ejecutar_agregar,
            f"El usuario canceló la inserción del producto '{nombre}'."
        )
    except ValueError:
        funciones.opcionInvalida()
    except Exception as e:
        print(f"Error inesperado: {e}")
        funciones.espereTecla()

def editarProducto():
    try:
        funciones.borrarPantalla()
        print(f"{CYAN}\n\t...::: EDITAR PRODUCTO :::...\n{RESET}")
        prods = crud.consultar()
        if not prods:
            print(f"\t{AMARILLO}⚠️ No hay productos disponibles para editar.{RESET}")
            funciones.espereTecla()
            return

        mostrarTablaProductos(prods)
        id_prod = input("\nID del producto a editar: ").strip()
        if not id_prod.isdigit():
            funciones.opcionInvalida()
            return

        prod = crud.buscar(id_prod)
        if not prod:
            funciones.opcionInvalida()
            return

        nombre = input("Nuevo nombre: ").strip()
        precio = float(input("Nuevo precio: "))

        cats = crud_categorias.consultar()
        if not cats:
            print(f"\n\t{AMARILLO}⚠️ No hay categorías registradas.{RESET}")
            funciones.espereTecla()
            return

        print(f"\n{AZUL}--- Categorías Disponibles ---{RESET}")
        ids_validos = []
        for c in cats:
            print(f"{VERDE}ID: {c[0]:<3}{RESET} | Categoría: {c[1]}")
            ids_validos.append(str(c[0]))

        cat_id_input = input("\nSeleccione el nuevo ID de Categoría: ").strip()
        if not cat_id_input.isdigit() or cat_id_input not in ids_validos:
            funciones.opcionInvalida()
            return

        cat_id = int(cat_id_input)

        print(f"\n{AZUL}--- RESUMEN DE CAMBIOS ---{RESET}")
        print(f"Acción: Modificación de producto ID {id_prod}")
        print(f"Nuevo Nombre: {nombre}")
        print(f"Nuevo Precio: ${precio:.2f}")
        print(f"Nuevo ID Categoría: {cat_id}")

        def ejecutar_editar():
            if crud.editar_producto(id_prod, nombre, precio, cat_id):
                mostrarExito(f"Se modificó correctamente el producto '{nombre}' (ID: {id_prod}).")
            else:
                funciones.accionNoExitosa()

        pedirConfirmacion(
            "¿Estás seguro de guardar estos cambios?",
            ejecutar_editar,
            f"Se descartaron los cambios para el producto ID {id_prod}."
        )
    except ValueError:
        funciones.opcionInvalida()
    except Exception as e:
        print(f"Error inesperado: {e}")
        funciones.espereTecla()

def eliminarProducto():
    try:
        funciones.borrarPantalla()
        print(f"{CYAN}\n\t...::: ELIMINAR PRODUCTO :::...\n{RESET}")
        prods = crud.consultar()
        if not prods:
            print(f"\t{AMARILLO}⚠️ No hay productos disponibles para eliminar.{RESET}")
            funciones.espereTecla()
            return

        mostrarTablaProductos(prods)
        id_prod = input("\nID del producto a eliminar: ").strip()
        if not id_prod.isdigit():
            funciones.opcionInvalida()
            return

        prod = crud.buscar(id_prod)
        if prod:
            nombre_p = prod[0][1]
            print(f"\n{AZUL}--- RESUMEN DE CAMBIOS ---{RESET}")
            print(f"Acción: Eliminar producto definitivamente")
            print(f"Producto: {nombre_p} (ID: {id_prod})")

            def ejecutar_eliminar():
                if crud.eliminar_producto(id_prod):
                    mostrarExito(f"Se eliminó correctamente el producto '{nombre_p}' (ID: {id_prod}).")
                else:
                    funciones.accionNoExitosa()

            pedirConfirmacion(
                "¿Estás seguro de eliminar este producto?",
                ejecutar_eliminar,
                f"No se eliminó el producto ID {id_prod}."
            )
        else:
            funciones.opcionInvalida()
    except Exception as e:
        print(f"Error inesperado: {e}")
        funciones.espereTecla()

def registrarVenta():
    try:
        funciones.borrarPantalla()
        print(f"{CYAN}\n\t...::: REGISTRAR VENTA :::...\n{RESET}")
        prods = crud.consultar()
        if not prods:
            print(f"\t{AMARILLO}⚠️ No hay productos disponibles.{RESET}")
            funciones.espereTecla()
            return

        mostrarTablaProductos(prods)
        id_p = input("\nID del producto vendido: ").strip()
        if not id_p.isdigit():
            funciones.opcionInvalida()
            return

        prod = crud.buscar(id_p)
        if prod:
            nombre_p = prod[0][1]
            stock_actual = prod[0][3]
            cant = int(input("Cantidad vendida: "))

            if cant <= 0:
                print(f"{ROJO}La cantidad debe ser mayor a 0.{RESET}")
            elif cant <= stock_actual:
                print(f"\n{AZUL}--- RESUMEN DE CAMBIOS ---{RESET}")
                print(f"Acción: Venta de producto")
                print(f"Producto: {nombre_p}")
                print(f"Stock actual: {stock_actual} -> Nuevo Stock: {stock_actual - cant}")

                def ejecutar_venta():
                    exito, _ = crud.vender_producto(id_p, cant)
                    if exito:
                        mostrarExito(f"Se registraron {cant} unidad(es) vendidas del producto '{nombre_p}'.")
                    else:
                        funciones.accionNoExitosa()

                pedirConfirmacion(
                    "¿Estás seguro de realizar esta venta?",
                    ejecutar_venta,
                    f"Se anuló el registro de venta para el producto '{nombre_p}'."
                )
            else:
                print(f"{AMARILLO}Stock insuficiente para realizar la venta.{RESET}")
        else:
            funciones.opcionInvalida()
    except ValueError:
        funciones.opcionInvalida()
    except Exception as e:
        print(f"Error inesperado: {e}")
    funciones.espereTecla()

def reabastecerMercancia():
    try:
        funciones.borrarPantalla()
        print(f"{CYAN}\n\t...::: REABASTECER MERCANCÍA :::...\n{RESET}")
        prods = crud.consultar()
        if not prods:
            print(f"\t{AMARILLO}⚠️ No hay productos disponibles.{RESET}")
            funciones.espereTecla()
            return

        mostrarTablaProductos(prods)
        id_p = input("\nID del producto a reabastecer: ").strip()
        if not id_p.isdigit():
            funciones.opcionInvalida()
            return

        prod = crud.buscar(id_p)
        if prod:
            nombre_p = prod[0][1]
            stock_actual = prod[0][3]
            cant = int(input("Cantidad a añadir: "))

            if cant > 0:
                print(f"\n{AZUL}--- RESUMEN DE CAMBIOS ---{RESET}")
                print(f"Acción: Reabastecimiento de stock")
                print(f"Producto: {nombre_p}")
                print(f"Stock actual: {stock_actual} -> Nuevo Stock: {stock_actual + cant}")

                def ejecutar_reabastecimiento():
                    if crud.reabastecer_stock(id_p, cant):
                        mostrarExito(f"Se agregaron {cant} unidad(es) al stock del producto '{nombre_p}'.")
                    else:
                        funciones.accionNoExitosa()

                pedirConfirmacion(
                    "¿Estás seguro de realizar este reabastecimiento?",
                    ejecutar_reabastecimiento,
                    f"Se descartó el reabastecimiento para '{nombre_p}'."
                )
            else:
                print(f"{ROJO}La cantidad debe ser mayor a 0.{RESET}")
        else:
            funciones.opcionInvalida()
    except ValueError:
        funciones.opcionInvalida()
    except Exception as e:
        print(f"Error inesperado: {e}")
    funciones.espereTecla()

def verStockBajo():
    funciones.borrarPantalla()
    print(f"{CYAN}\n\t...::: ALERTAS DE STOCK BAJO (<= 5) :::...\n{RESET}")
    productos = crud.consultar_stock_bajo()
    if productos:
        print(f"{CYAN}{'ID':<5}|{'PRODUCTO':<20}|{'STOCK':<10}|{'CATEGORÍA':<10}{RESET}")
        print(f"{AZUL}" + "-" * 50 + f"{RESET}")
        for p in productos:
            print(f"{VERDE}{p[0]:<5}{RESET}|{p[1]:<20}|{ROJO}{p[2]:<10}{RESET}|{p[3]:<10}")
    else:
        print(f"\t{VERDE}Todos los productos cuentan con stock suficiente.{RESET}")
    funciones.espereTecla()

def menuStock():
    ciclar = True
    while ciclar:
        funciones.borrarPantalla()
        print(f"{AZUL}=============================================================={RESET}")
        print(f"{CYAN}\t\t 💲 MOVIMIENTOS DE STOCK{RESET}")
        print(f"{AZUL}=============================================================={RESET}\n")
        print(f"\t{VERDE}1.{RESET} 🛍️  Vender Producto")
        print(f"\t{VERDE}2.{RESET} 📦 Reabastecer Producto")
        print(f"\t{VERDE}3.{RESET} ⚠️  Ver Alertas de Stock Bajo")
        print(f"\t{ROJO}4.{RESET} ↩️  Regresar\n")
        print(f"{AZUL}--------------------------------------------------------------{RESET}")
        opc = input(f"{AMARILLO}Selecciona una opción: {RESET}").strip()

        match opc:
            case "1":
                registrarVenta()
            case "2":
                reabastecerMercancia()
            case "3":
                verStockBajo()
            case "4":
                ciclar = False
            case _:
                funciones.opcionInvalida()

def MenuGestion():
    ciclar = True
    while ciclar:
        funciones.borrarPantalla()
        print(f"{AZUL}=============================================================={RESET}")
        print(f"{CYAN}\t\t 🏷️  STOCK MASTER - CONTROL DE INVENTARIO{RESET}")
        print(f"{AZUL}=============================================================={RESET}\n")
        print(f"\t{VERDE}1.{RESET} 📜 Ver Productos")
        print(f"\t{VERDE}2.{RESET} ➕ Agregar Producto")
        print(f"\t{VERDE}3.{RESET} ✏️  Editar Producto")
        print(f"\t{VERDE}4.{RESET} 🗑️  Eliminar Producto")
        print(f"\t{ROJO}5.{RESET} ↩️  Regresar\n")
        print(f"{AZUL}--------------------------------------------------------------{RESET}")
        opc = input(f"{AMARILLO}Seleccione una opción: {RESET}").strip()

        match opc:
            case "1":
                consultarInventario()
            case "2":
                agregarProducto()
            case "3":
                editarProducto()
            case "4":
                eliminarProducto()
            case "5":
                ciclar = False
            case _:
                funciones.opcionInvalida()

def menuHistorial():
    ciclar = True
    while ciclar:
        funciones.borrarPantalla()
        print(f"{AZUL}=============================================================={RESET}")
        print(f"{CYAN}\t\t 🗑️  OPCIONES DE LIMPIEZA DE HISTORIAL{RESET}")
        print(f"{AZUL}=============================================================={RESET}\n")
        print(f"\t{VERDE}1.{RESET} 📜 Ver Historial Actual")
        print(f"\t{VERDE}2.{RESET} ⚠️  Vaciar Historial Completo (PERMANENTE)")
        print(f"\t{ROJO}3.{RESET} ↩️  Regresar al Menú Principal\n")
        print(f"{AZUL}--------------------------------------------------------------{RESET}")
        opc = input(f"{AMARILLO}Seleccione una opción: {RESET}").strip()

        match opc:
            case "1":
                verHistorial()
            case "2":
                vaciarHistorial()
            case "3":
                ciclar = False
            case _:
                funciones.opcionInvalida()
                
def vaciarHistorial():
    funciones.borrarPantalla()
    print(f"{AZUL}=============================================================={RESET}")
    print(f"{CYAN}\t\t 🗑️  VACIAR Y REINICIAR HISTORIAL{RESET}")
    print(f"{AZUL}=============================================================={RESET}\n")

    try:
        cursor = funciones.conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM historial")
        total = cursor.fetchone()[0]
        cursor.close()

        if total == 0:
            print(f"\t{AMARILLO}⚠️ El historial ya se encuentra totalmente vacío.{RESET}\n")
            funciones.espereTecla()
            return

        print(f"\t{ROJO}⚠️ ADVERTENCIA: Se eliminarán {total} registro(s) y el ID volverá a iniciar en 1.{RESET}")
        print(f"\t{ROJO}Esta acción no se puede deshacer.{RESET}\n")

        def ejecutar_vaciar():
            exito, eliminados = crud.vaciar_historial_db(funciones.conexion)
            if exito:
                mostrarExito(f"Historial vaciado por completo. Se eliminaron {eliminados} registros y la secuencia de ID se reinició.")
            else:
                funciones.accionNoExitosa()

        pedirConfirmacion(
            "¿Estás seguro de ejecutar el TRUNCATE al historial?",
            ejecutar_vaciar,
            "Se canceló la limpieza del historial."
        )
    except Exception as e:
        print(f"Error inesperado al intentar vaciar el historial: {e}")
        funciones.espereTecla()
        
def terminarSistema():
    print(f"\n\t{CYAN}...::: Gracias por usar el sistema de inventario :::...{RESET}\n")
    input(f"\t\t{AMARILLO}Presione ENTER para salir del sistema{RESET}")
    exit()