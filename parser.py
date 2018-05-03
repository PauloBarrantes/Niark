import ply.yacc as yacc
from lex import tokens


def p_PUBLIC(p):
    'expression : PUBLIC expression'
    print("PUBLIC: ",p[1])

def p_PRIVATE(p):
    'expression : PRIVATE expression'
    print("PRIVATE: ", p[1])

def p_FUNCDOMAIN(p):
    '''
    domain : PRIVATE
           | PUBLIC
    '''
    print(p[1])

def p_FUNCRETURN(p):
    '''
    return : VOID
           | FUNCTION
    '''
    print(p[1])

def p_FUNCTION(p):
    '''
    expression : domain return NOMBRE PARIZQ parameter PARDER
    '''
    print("FUNCTION: ", p[3],p[4],p[6])

def p_PARAMETRO(p):
    '''
    parameter : empty
              | NOMBRE parametro_extra

    '''
    print(p[1])

def p_PARAMETRO_EXTRA(p):
    '''
    parametro_extra : COMA NOMBRE parametro_extra
                    | empty
    '''

def p_TRUE(p):
    'expression : TRUE expression'
    print("TRUE: ", p[1])

def p_FALSE(p):
    'expression : FALSE expression'
    print("FALSE: ", p[1])

def p_IF(p):
    '''
    expression : IF PARIZQ condition PARDER
    '''
    print("IF: ", p[1])

def p_ELSE(p):
    'expression : ELSE expression'
    print("ELSE: ", p[1])

def p_OPERATION(p):
    '''
    expression :  t NOMBRE
    '''

def p_FOR(p):
    '''
    expression : FOR PARIZQ DECVARIABLE ASIGNACION INT PUNTOYCOMA condition PUNTOYCOMA incdec NOMBRE PARDER
    '''
    print("FOR: ", p[1],p[2],p[3],p[4],p[5],p[6],p[8],p[10],p[11])

def p_CONDITION_OPERATOR(p):
    '''
    condition_operator : DIFERENTE
              | IGUAL
              | MAYOR
              | MAYORIGUAL
              | MENOR
              | MENORIGUAL
    '''
    print(p[1])

def p_CONDITON(p):
    '''
    condition : variabletypes condition_operator variabletypes extra_condition
    '''

def p_EXTRA_CONDITON(p):
    '''
    extra_condition : variabletypes condition_operator variabletypes extra_condition
                    | empty
    '''


def p_VARIABLETYPES(p):
    '''
    variabletypes : NOMBRE
                  | DOUBLE
                  | INT
                  | STRING
    '''
    print(p[1])

def p_INCDEC(p):
    '''
    incdec : INCREMENTAR
           | DECREMENTAR
    '''

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
    't : SUMA expression'
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

def p_LOGICOPERATOR(p):
    '''
    logic_operator : AND
                   | OR
    '''

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
    'empty : '

def p_error(p):
    print("ERROR")

# Build the parser
parser = yacc.yacc()

name = input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()


while True:
    parser.parse(line)
    break
