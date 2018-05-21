import ply.yacc as yacc
from lex import tokens


def p_START(p):
    '''
    start : declare_function NEWLINE TABULACION
    '''

def p_FUNCTION(p):
    '''
    declare_function : function_type function_return NOMBRE PARIZQ parameter PARDER
    '''

def p_FUNCTION_TYPE(p):
    '''
    function_type : PUBLIC
                  | PRIVATE
    '''

def p_FUNCTION_RETURN(p):
    '''
    function_return : FUNCTION
                    | VOID
    '''

def p_PARAMETER(p):
    '''
    parameter : NOMBRE extra_parameter
              | empty
    extra_parameter : COMA NOMBRE extra_parameter
                    | COMA NOMBRE
    '''

def p_EMPTY(p):
    '''
    empty :
    '''

def p_error(p):
    print("error")
# Build the parser
parser = yacc.yacc()

name = input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()


while True:
    parser.parse(line)
    break
