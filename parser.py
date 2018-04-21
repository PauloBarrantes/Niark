import ply.yacc as yacc
from lex import tokens


def p_PUBLIC(p):
    'expression : PUBLIC expression'
    print("PUBLIC: ",p[1])

def p_PRIVATE(p):
    'expression : PRIVATE expression'
    print("PRIVATE: ", p[1])

def p_FUNCTION(p):
    'expression : FUNCTION expression'
    print("FUNCTION: ", p[1])

def p_VOID(p):
    'expression : VOID expression'
    print("VOID: ", p[1])

def p_TRUE(p):
    'expression : TRUE expression'
    print("TRUE: ", p[1])

def p_FALSE(p):
    'expression : FALSE expression'
    print("FALSE: ", p[1])

def p_IF(p):
    'expression : IF expression'
    print("IF: ", p[1])

def p_FOR(p):
    'expression : FOR expression'
    print("FOR: ", p[1])

def p_ELSE(p):
    'expression : ELSE expression'
    print("ELSE: ", p[1])

def p_WHILE(p):
    'expression : WHILE expression'
    print("WHILE: ", p[1])

def p_RETURN(p):
    'expression : RETURN expression'
    print("RETURN: ", p[1])

def p_PRINT(p):
    'expression : PRINT expression'
    print("PRINT: ", p[1])

def p_READ(p):
    'expression : READ expression'
    print("READ: ", p[1])

def p_IMPORT(p):
    'expression : IMPORT expression'
    print("IMPORT: ", p[1])

def p_SWITCH(p):
    'expression : SWITCH expression'
    print("SWITCH: ", p[1])

def p_CASE(p):
    'expression : CASE expression'
    print("CASE: ", p[1])

def p_BREAK(p):
    'expression : BREAK expression'
    print("BREAK: ", p[1])

def p_TABULACION(p):
    'expression : TABULACION expression'
    print("TABULACION: ", p[1])

def p_COMA(p):
    'expression : COMA expression'
    print("COMA: ", p[1])

def p_INT(p):
    'expression : INT expression'
    print("INT: ", p[1])

def p_DOUBLE(p):
    'expression : DOUBLE expression'
    print("DOUBLE: ", p[1])

def p_NOMBRE(p):
    'expression : NOMBRE expression'
    print("NOMBRE: ", p[1])

def p_STRING(p):
    'expression : STRING expression'
    print("STRING: ", p[1])

def p_PUNTOYCOMA(p):
    'expression : PUNTOYCOMA expression'
    print("PUNTOYCOMA: ", p[1])

def p_DECVARIABLE(p):
    'expression : DECVARIABLE expression'
    print("DECVARIABLE: ", p[1])

def p_IGUAL(p):
    'expression : IGUAL expression'
    print("IGUAL: ", p[1])

def p_MENOR(p):
    'expression : MENOR expression'
    print("MENOR: ", p[1])

def p_MAYOR(p):
    'expression : MAYOR expression'
    print("MAYOR: ", p[1])

def p_MAYORIGUAL(p):
    'expression : MAYORIGUAL expression'
    print("MAYORIGUAL: ", p[1])

def p_MENORIGUAL(p):
    'expression : MENORIGUAL expression'
    print("MENORIGUAL: ", p[1])

def p_ASIGNACION(p):
    'expression : ASIGNACION expression'
    print("ASIGNACION: ", p[1])

def p_SUMA(p):
    'expression : SUMA expression'
    print("SUMA: ", p[1])

def p_RESTA(p):
    'expression : RESTA expression'
    print("RESTA: ", p[1])

def p_INCREMENTAR(p):
    'expression : INCREMENTAR expression'
    print("INCREMENTAR: ", p[1])

def p_DECREMENTAR(p):
    'expression : DECREMENTAR expression'
    print("DECREMENTAR: ", p[1])

def p_MULT(p):
    'expression : MULT expression'
    print("MULT: ", p[1])

def p_DIV(p):
    'expression : DIV expression'
    print("DIV: ", p[1])

def p_PARIZQ(p):
    'expression : PARIZQ expression'
    print("PARIZ: ", p[1])

def p_PARDER(p):
    'expression : PARDER expression'
    print("PARDER: ", p[1])

def p_CORCHETEIZQ(p):
    'expression : CORCHETEIZQ expression'
    print("CORCHETEIZQ: ", p[1])

def p_CORCHETEDER(p):
    'expression : CORCHETEDER expression'
    print("CORCHETEDER: ", p[1])

def p_COMENTARIO(p):
    'expression : COMENTARIO expression'
    print("COMENTARIO: ", p[1])

def p_NEWLINE(p):
    'expression : NEWLINE expression'
    print("NEWLINE: ", p[1])

def p_AND(p):
    'expression : AND expression'
    print("AND: ", p[1])

def p_OR(p):
    'expression : OR expression'
    print("OR: ", p[1])

def p_DIFERENTE(p):
    'expression : DIFERENTE expression'
    print("DIFERENTE: ", p[1])

def p_empty(p):
    'expression : '

# Build the parser
parser = yacc.yacc()

name = input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()


while True:
    parser.parse(line)
    break