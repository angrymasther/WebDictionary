# -*- coding: utf-8 -*-

import os
import sys
import request

def filtrar(direccion):
    o = open("contenido", "w")
    o.write("\n")
    o.close()
    o = open(direccion , "r")
    i = 0
	string = ""
	etiqueta = ""
	for x in o.read():
		if i == 2:
			i = 0

		if x == "<":
			i = 1

		if x == ">":
			i = 2

		if i == 0:
			string += x
	print "."+string

	o.close()
	o2 = open("contenido" , "w")
	o2.write(string)
	o2.close()
	print "Palabras filtradas , comenzando creacion de diccionario"

def obtener_pagina(direccion):
    r = requests.get(direccion)
    if r.status_code == 404:
        print "página no encontrada"
        exit()
    else:
        return r.text

def obtener(direccion, archivo):
	try:
		Palabras = []
		OTHERS = (" ","'","\\","*","\n","|","		","	","•","»","«","(",")","[","]","{","}","#","~","€","%","&","/","=","?","€","$","+","^","-","_","<",">",".","–",":",";",".",",","\"","–","¡","?","!","¿")
		lista = os.listdir(".")
		filtrar(obtener_pagina(direccion))
		o = open(archivo , "w")
		contenido = open("contenido" , "r")
		palabra = ""
		for x in contenido.read():
			if x not in OTHERS:
				palabra += x
			elif x in OTHERS:
				if palabra not in Palabras:
					Palabras.append(palabra)
					palabra = ""
				else:
					pass

		for x in Palabras:
			o.write(x)
			o.write("\n")
			print x
		o.close()
		os.system("rm contenido")
		os.system("rm "+nombre)
	except IndexError:
		print "Error con los parametros"
