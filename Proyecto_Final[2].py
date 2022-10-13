 # -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:17:01 2021

@author: andre
"""
"""
ANDRÉS CAMILO CASTRO BRAVO
DIEGO ALEJANDRO CIRO MARÍN
JUAN PABLO CABRERA CUBILLOS
DAVID FABIAN GALVIS BARRERA
"""
ahorro = []
gastos = []
ingresos = []
metas = []
costo_metas = []

from datetime import datetime
global date
def current_date_format(date):
    
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

now = datetime.now()


def MENU():
    print("---------------MENU----------------\n")
    print("Digite (i) si quiere ingresar un ingreso")
    print("Digite (g) si desea dar un gasto")
    print("Digite (j) si desea ver su total de ingresos")
    print("digite (f) si desea ver su total de gastos")
    print("Digite (a) si desea ahorrar dinero")
    print("Digite (e) si desea ver su estado de cuenta")
    print("Digite (m) si desea ver su total ahorrado")
    print("Digite (o) si desea agregar un objetivo financiero")
    print("Digite (l) para ver cuanto le falta para lograr su objetivo")
    print("\n------------------------------------------------------------")
    
def respuesta():
    global condicion, ahorro_total
    condicion = input("Elija que opcion va a realizar:")
    if condicion == "i":
        ingresos.append(int(input("digite su ingreso: $")))
        
    elif condicion =="g":
        gastos.append(float(input("ingrese su gasto: $")))
        
    elif condicion == "j":
        if len(ingresos) == 0:
           print("Para poder vizualizar el total de ingresos primero tiene que agregar algun ingreso")
        else:
            suma_ingresos = sum(ingresos)
            print("El total de sus ingresos son: $",suma_ingresos)
            
    elif condicion == "f":
        if len(gastos) == 0:
            print("Para poder vizualizar el total de gastos primero tiene que ingresar gastos")
        else:
            suma_gastos = sum(gastos)
            print("El total de sus gastos son: $",suma_gastos)
            
    elif condicion == "a":
        suma_gastos = sum(gastos)
        suma_ingresos = sum(ingresos)
        cuenta = suma_ingresos - suma_gastos
        ahorro_total = ahorro.append(int(input("Cuanto desea ahorrar: $")))
        ahorro_total = sum(ahorro)
        cuentita = (cuenta) - (ahorro_total)
        if ahorro_total > cuenta:
            print("\nSi ahorra dinero que no tiene se descontara luego cuando ingrese un ahorro positivo.")
        print("\nSu estado de cuenta ahora es de: $",cuentita)
    
    elif condicion == "e":
        suma_gastos = sum(gastos)
        suma_ingresos = sum(ingresos)
        aho = sum(ahorro)
        cuenta = suma_ingresos - suma_gastos - aho
        print("su estado de cuenta es: $",cuenta)
    
    elif condicion=="m":
        print("\nSu ahorro total es de: $",sum(ahorro))
    elif condicion == "o":
        metas.append(input("Digite el nombre de lo que desea comprar:"))
        costo_metas.append(int(input("Digite el costo de lo que desea comprar: $")))
    elif condicion ==  "l":
        ahorro_total = sum(ahorro)
        suma_costo_metas = sum(costo_metas)
        falta_meta = suma_costo_metas - ahorro_total
        if falta_meta<=0:
            print("Ya haz alcanzado el dinero suficiente para tu objetivo",metas," te sobran", falta_meta)
        else:
            print("Le falta un total de: $", falta_meta," Para comprar ", metas)
     
    else:
        print("comando invalido")
        
def menu():
    print("\nDesea salir del programa oprima (s)")
    print("Si desea seguir oprima cualquier otra")

condicion = 0
while condicion != "s":
    print("\n",current_date_format(now))
    MENU()
    respuesta()
    menu()
    condicion = input("Opcion:")
