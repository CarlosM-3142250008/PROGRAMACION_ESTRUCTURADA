
def ventaAutos(Ap,acum,cont):  
    while Ap== "SI":
        marca= input("marca: ").lower()
        origen= input("origen: ").lower()
        costo= float(input("Costo: "))
        if origen == "alemania":
            impuesto= 0.20
        elif origen== "japo":
            impuesto= 0.30
        elif origen== "italia":
            impuesto= 0.15
        elif origen== "usa":
            impuesto= 0.08
        else:
            print(f"Ingresa solo alemania, japon, italia y usa")
        
        ipagar= impuesto*costo
        pimpuesto= ipagar+costo
        print(f"El impuesto a pagar es de:  {ipagar}")
        print(f"El precio despues del impuesto es de:  {pimpuesto}")
        
        acum+= pimpuesto
        cont+= 1
        Ap=input("Desea ingresar otro? SI/NO: ").upper()
    return Ap,acum,cont
acum=0
impuesto=0
cont=0
Ap= "SI"
Ap,acum,cont= ventaAutos(Ap,acum,cont)
print(f"total por todos los carros{acum}")
print(f"total de carros {cont}")

