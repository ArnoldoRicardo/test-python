#!/usr/bin/env python

#area del cuadrado
def cuadrado():
    print "cuanto mide tu el lado"
    LADO = float(raw_input ("> "))
    AREA4 = LADO * LADO
    print "tu area es = " + str(AREA4)

#area del circulo
def circulo():
    import math
    print "cuanto mide el radio"
    RADIO = float(raw_input ("> "))
    AREA1 = RADIO * math.pi
    print " tu area es = " + str(AREA1)

#menu
def menu():
    while True:
        print "que area quieres calcular (circulo/cuadrado/regresar)"
        ENTRADA = str(raw_input ("> "))
        if ENTRADA == "circulo":
            circulo()
        elif ENTRADA == "cuadrado":
            cuadrado()
        elif ENTRADA == "regresar":
            break
        else:
            print "introduce un valor correcto (circulo/cuadrado)"

#inicio
while True:
    print "quieres calcular un area (si/no)"
    CERRAR = str(raw_input ("> "))
    if CERRAR == "no":
        break
    elif CERRAR == "si":
        menu()
    else:
        print "introduce un valor correcto (si/no)"
