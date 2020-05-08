# -*- coding: utf-8 -*-
import os
import sys
import re
import urllib2
from bs4 import BeautifulSoup
archivo = sys.argv[1]
resultado = sys.argv[2]
if resultado in os.listdir("."):
    print "El nombre del archivo ya esta en uso"
    exit()

def sacar_palabras_del_texto(texto):
    lista_palabras = []
    palabra = ""
    for caracter in texto:
        if caracter == " ":
            if palabra not in lista_palabras:
                lista_palabras.append(palabra.strip())
            palabra = ""
        palabra += caracter
    print "Lista de palabras creada"
    return lista_palabras

def cleanhtml(raw_html):
    soup = BeautifulSoup(raw_html, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def escribir_diccionario(texto):
    diccionario = open(resultado, "w")
    diccionario.write("")
    diccionario.close()
    diccionario = open(resultado, "a")
    for x in texto:
        try:
            diccionario.write(x)
        except:
            pass
        diccionario.write("\n")
    diccionario.close()
    print "Diccionario escrito en "+resultado

r = urllib2.Request(archivo)
url = urllib2.urlopen(r)
texto = url.read()
print texto
texto = cleanhtml(texto)
print texto
diccionario = sacar_palabras_del_texto(texto)
escribir_diccionario(diccionario)
