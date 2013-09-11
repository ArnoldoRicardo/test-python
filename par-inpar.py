#!/usr/bin/python
print "es cribe un numero"
ENTRADA = float(raw_input ("> "))
NUMERO = ENTRADA % 2
if  ENTRADA == 0:
    print "no es nada"
elif  NUMERO == 0:
    print "el numero es par"
else:
    print "el numero es inpar"
