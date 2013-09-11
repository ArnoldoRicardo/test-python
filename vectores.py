#!/usr/bin/python
import math

def fr():
    print "introduce la fuerza x"
    fx= float(raw_input("> "))
    print "introduce la fuerza y"
    fy= float(raw_input("> "))
    fr= str(math.sqrt(fx**2+fy**2))
    print "la fuerza resultante es " + fr
    raw_input ("> ")
    angulo(fx,fy)

def angulo(fx,fy):
    a = fy/fx
    b = math.tan (a)
    teta = str(math.degrees (b))
    print "el angulo es " + teta + " grados"
    raw_input ("> ")
    
while True:
    print "quieres calcular un vector(si/no)"
    pregunta=raw_input ("> ")
    if pregunta == "no":
        break
    elif pregunta == "si":
        fr()
    else:
        print "escriba una obsion correcta"
