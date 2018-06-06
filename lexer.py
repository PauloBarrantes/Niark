# coding=utf-8

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
}
# Lista de Tokens
tokens = [
    'COMMA',
    'INT',
    'DOUBLE',
    'NAME',
    'STRING',
    'SEMICOLON',
    'VARDECLARATION',
    'EQUALS',
    'LESSER',
    'GREATER',
    'LESSEREQUAL',
    'GREATEREQUAL',
    'ASIGNATION',
    'SUM',
    'SUBSTRACTION',
    'INCREASE',
    'DECREASE',
    'MULTIPLICATION',
    'DIVISION',
    'LEFTPAR',
    'RIGHTPAR',
    'LEFTBRACKET',
    'RIGHTBRACKET',
    'NEWLINE',
    'AND',
    'OR',
    'DIFFERENT',
    'LEFTKEY',
    'RIGHTKEY'

] + list(reserved.values())
## Regular Expresion

def t_DOUBLE(t):
    r'\d+\.(\d)+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_STRING(t):
    r'("(\\"|[^"])*")|(\'(\\\'|[^\'])*\')'
    t.type = "STRING"
    return t

def t_VARDECLARATION(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = "VARDECLARATION"
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    t.value = "NEWLINE"
    t.type = "NEWLINE"
    return t

t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_EQUALS = r'\=='
t_LESSER = r'\<'
t_GREATER = r'\>'
t_LESSEREQUAL = r'\<='
t_GREATEREQUAL = r'\>='
t_ASIGNATION = r'\='
t_SUM  = r'\+'
t_SUBSTRACTION  = r'\-'
t_INCREASE = r'\+\+'
t_DECREASE = r'\-\-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'\/'
t_LEFTPAR = r'\('
t_RIGHTPAR = r'\)'
t_LEFTBRACKET = r'\['
t_RIGHTBRACKET = r'\]'
t_AND = r'\&&'
t_OR = r'\|\|'
t_DIFFERENT = r'\!='
t_LEFTKEY = r'\{'
t_RIGHTKEY = r'\}'
t_ignore = r' '

def t_error(t):
    print("Lexical error in line " ,t.lexer.lineno)
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