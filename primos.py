#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def isPrime(num):
	if num < 2:
		return False

	i = 2
	for i in range(2,int(math.sqrt(num)+1)):
		if (num % i == 0):
			return False

	return True

def main():
	print "este programa imprime numeros primos"
	inicio = int(raw_input("escribe el numero de inicio: "))
	fin = int(raw_input('escribe el numero final: '))

	for i in range(inicio,fin):
		if isPrime(i):
			print i

if __name__ == '__main__':
	main()