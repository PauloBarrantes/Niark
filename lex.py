# coding=utf-8
#comment
"""
Nombre del equipo: Byte_Me
Prerequisitos: Tener instalado python 3.5

Correr el archivo lex.py, colocar el nombre del archivo .nia que contiene el código fuente del lenguaje de programación Niark
"""
import ply.lex as lex
reserved = {
    'public' : 'PUBLIC',
    'private': 'PRIVATE',
    'function': 'FUNCTION',
    'void': 'VOID',
    'True': 'TRUE',
    'False': 'FALSE',
    'if' : 'IF',
    'for' : 'FOR',
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
    'TABULACION',
    'COMA',
    'INT',
    'DOUBLE',
    'NOMBRE',
    'STRING',
    'PUNTOYCOMA',
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
    'CORCHETEIZQ',
    'CORCHETEDER',
    'COMENTARIO',
    'NEWLINE',
    'AND',
    'OR',
    'DIFERENTE'

] + list(reserved.values())
## Expresiones Regulares

lineno  = 1 #Número de línea

def t_DOUBLE(t):
    r'-?\d+\.(\d)+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

t_INCREMENTAR = r'\+\+'
t_DECREMENTAR = r'\-\-'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_IGUAL = r'\=='
t_DIFERENTE = r'\!='
t_MAYORIGUAL = r'\>='
t_MENORIGUAL = r'\<='
t_AND = r'\&&'
t_OR = r'\|\|'
t_COMA = r'\,'
t_PUNTOYCOMA = r'\;'
t_ASIGNACION = r'\='
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r'\]'
t_ignore = r' '

def t_DECVARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = "DECVARIABLE"
    return t

def t_NOMBRE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NOMBRE')    # Check for reserved words
    return t

def t_STRING(t):
    r'("(\\"|[^"])*")|(\'(\\\'|[^\'])*\')'
    t.type = "STRING"
    return t
def t_TABULACION(t):
    r'\t'
    t.value = "Tabulacion"
    t.type = "TABULACION"
    return t
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    t.value = "NEWLINE"
    t.type = "NEWLINE"
    return t

def t_COMENTARIO(t):
    r'//(.[^(//)]|\n)*//'
    pass
    #No return value. Token discarded

def t_error(t):
    print("Error Lexico en la linea " ,t.lexer.lineno)
    t.lexer.skip(1)


lexer = lex.lex()
'''

name = input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()

lexer.input(line)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
'''