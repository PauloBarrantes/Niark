# coding=utf-8
"""
Nombre del equipo: Byte_Me
Prerequisitos: Tener instalado python 2.6 mínimo

Correr el archivo lex.py, colocar el nombre del archivo .nia que contiene el código fuente del lenguaje de programación Niark
"""
import ply.lex as lex
import sys
reserved = {
    'public' : 'PUBLIC',
    'private': 'PRIVATE',
    'function': 'FUNCTION',
    'void': 'VOID',
    'True': 'TRUE',
    'False': 'FALSE',

    'if' : 'IF',
    'for' : 'FOR',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'return' : 'RETURN',
    'print' : 'PRINT',
    'read' : 'READ',
    'import' : 'IMPORT',
    'switch' :'SWITCH',
    'case' : 'CASE',
    'break' : 'BREAK',
}

# Lista de Tokens
tokens = [

    'INT',
    'DOUBLE',
    'NOMBRE',
    'STRING',
    'DECVARIABLE',
    'IGUAL',
    'MENOR',
    'MAYOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'ASIGNACION',
    'SUMA',
    'RESTA',
    'INCREMENTAR',
    'DECREMENTAR',
    'MULT',
    'DIV',
    'PARIZQ',
    'PARDER',
    'COMENTARIO',

] + list(reserved.values())
## Expresiones Regulares
t_INCREMENTAR = r'\+\+'
t_DECREMENTAR = r'\-\-'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_IGUAL = r'\=='
t_MAYORIGUAL = r'\>='
t_MENORIGUAL = r'\<='

t_ASIGNACION = r'\='
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_ignore = r' '

def t_DECVARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = "DECVARIABLE"
    return t

def t_INT(t):
    r'\d\+'
    t.value = int(t.value)
    return t

def t_NOMBRE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NOMBRE')    # Check for reserved words
    return t

def t_DOUBLE(t):
    r'\d+\.\d'
    t.value = float(t.value)
    return t
def t_STRING(t):
    r'("(\\"|[^"])*")|(\'(\\\'|[^\'])*\')'
    t.type = "STRING"
    return t



#def t_COMENTARIO(t):
 #   r'\c'
  #  pass
    # No return value. Token discarded



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
    print '<',tok.value,'>' ,"-", '<',tok.type,'>'
