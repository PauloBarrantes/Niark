# coding=utf-8
"""
Nombre del equipo: Byte_Me
Prerequisitos: Tener instalado python 2.6 mínimo

Correr el archivo lex.py, colocar el nombre del archivo .nia que contiene el código fuente del lenguaje de programación Niark
"""
import ply.lex as lex
import sys
reserved = {    #Keywords

    'public' : 'PUBLIC',
    'private' : 'PRIVATE',
    'function': 'FUNCTION',
    'void' : 'VOID',
    'if' : 'IF',
    'for': 'FOR',
    'switch' : 'SWITCH'

}
# Lista de Tokens
tokens = [


    'INT',
    'DOUBLE',
    'NOMBRE',
    'IGUAL',
    'MENOR',
    'MAYOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'ASIGNACION',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'ID'


] + list(reserved.values())
## Expresiones Regulares
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_IGUAL = r'\=='
t_ASIGNACION = r'\='
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_MAYORIGUAL = r'\>='
t_MENORIGUAL = r'\<='

t_ignore = r' '


def t_INT(t):
    r'd\+'
    t.value = int(t.value)
    return t

def t_DOUBLE(t):
    r'\d+\.\d'
    t.value = float(t.value)
    return t
def t_NOMBRE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = "NOMBRE"
    return t
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
def t_error(t):
    print("Caracteres Inválidos")
    t.lexer.skip(1)

lexer = lex.lex()
name = raw_input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()

lexer.input(line)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)