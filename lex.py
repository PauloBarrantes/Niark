# coding=utf-8
"""
Nombre del equipo: Byte_Me
Prerequisitos: Tener instalado python 2.6 mínimo

Correr el archivo lex.py, colocar el nombre del archivo .nia que contiene el código fuente del lenguaje de programación Niark
"""
name = raw_input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()

print(line)
