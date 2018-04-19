import ply.yacc as yacc

from lex import tokens


def p_INT(p):
    '''
    expression : INT
    '''
    p[0] = p[1]
    print(p[1])
    print("INT")

def p_DOUBLE(p):
    '''
    expression : DOUBLE
    '''
    p[0] = p[1]
    print(p[1])
    print("DOUBLE")

def p_STRING(p):
    '''
    expression : STRING
    '''
    p[0] = p[1]
    print(p[1], "-STRING")

def p_NOMBRE(p):
    '''
    expression : NOMBRE
    '''
    p[0] = p[1]
    print(p[1])

def p_MULT(p):
    '''
    expression : expression MULT expression
    '''
    p[0] = p[1] * p[3]
    print(p[0])

def p_DIV(p):
    '''
    expression : expression DIV expression
    '''
    p[0] = p[1] / p[3]
    print(p[0])

def p_SUMA(p):
    '''
    expression : expression SUMA expression
    '''
    p[0] = p[1] + p[3]
    print(p[0])

def p_RESTA(p):
    '''
    expression : expression RESTA expression
    '''
    p[0] = p[1] - p[3]
    print(p[0])

def p_NEWLINE(p):
    '''
    expression : NEWLINE
    '''
    print("NEWLINE")

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None
'''

def p_PUBLIC(p):
    'expression : expression PUBLIC expression'

def p_PRIVATE(p):
    'expression : expression PRIVATE expression'

def p_FUNCTION(p):
    'expression : expression FUNCTION expression'

def p_VOID(p):
    'expression : expression VOID expression'

def p_TRUE(p):
    'expression : expression TRUE expression'

def p_FALSE(p):
    'expression : expression FALSE expression'

def p_IF(p):
    'expression : expression IF expression'

def p_FOR(p):
    'expression : expression FOR expression'

def p_ELSE(p):
    'expression : expression ELSE expression'

def p_WHILE(p):
    'expression : expression WHILE expression'

def p_RETURN(p):
    'expression : expression RETURN expression'

def p_PRINT(p):
    'expression : expression PRINT expression'

def p_READ(p):
    'expression : expression READ expression'

def p_IMPORT(p):
    'expression : expression IMPORT expression'

def p_SWITCH(p):
    'expression : expression SWITCH expression'

def p_CASE(p):
    'expression : expression CASE expression'

def p_BREAK(p):
    'expression : expression BREAK expression'

def p_TABULACION(p):
    'expression : expression TABULACION expression'

def p_COMA(p):
    'expression : expression COMA expression'

def p_INT(p):
    'expression : expression INT expression'

def p_DOUBLE(p):
    'expression : expression DOUBLE expression'

def p_NOMBRE(p):
    'expression : expression NOMBRE expression'

def p_STRING(p):
    'expression : expression STRING expression'

def p_PUNTOYCOMA(p):
    'expression : expression PUNTOYCOMA expression'

def p_DECVARIABLE(p):
    'expression : expression DECVARIABLE expression'

def p_IGUAL(p):
    'expression : expression IGUAL expression'

def p_MENOR(p):
    'expression : expression MENOR expression'

def p_MAYOR(p):
    'expression : expression MAYOR expression'

def p_MAYORIGUAL(p):
    'expression : expression MAYORIGUAL expression'

def p_MENORIGUAL(p):
    'expression : expression MENORIGUAL expression'

def p_ASIGNACION(p):
    'expression : expression ASIGNACION expression'

def p_SUMA(p):
    'expression : expression SUMA expression'

def p_RESTA(p):
    'expression : expression RESTA expression'

def p_INCREMENTAR(p):
    'expression : expression INCREMENTAR expression'

def p_DECREMENTAR(p):
    'expression : expression DECREMENTAR expression'

def p_MULT(p):
    'expression : expression MULT expression'

def p_DIV(p):
    'expression : expression DIV expression'

def p_PARIZQ(p):
    'expression : expression PARIZQ expression'

def p_PARDER(p):
    'expression : expression PARDER expression'

def p_CORCHETEIZQ(p):
    'expression : expression CORCHETEIZQ expression'

def p_CORCHETEDER(p):
    'expression : expression CORCHETEDER expression'

def p_COMENTARIO(p):
    'expression : expression COMENTARIO expression'

def p_NEW_LINE(p):
    'expression : expression NEW_LINE expression'

def p_AND(p):
    'expression : expression AND expression'

def p_OR(p):
    'expression : expression OR expression'

def p_DIFERENTE(p):
    'expression : expression DIFERENTE expression'

def p_expression(p):
    'expression : expression'

def p_empty(p):
    'expression : '
'''
# Build the parser
parser = yacc.yacc()

name = input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()


while True:
    parser.parse(line)
    break