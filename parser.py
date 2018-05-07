import ply.yacc as yacc
from lex import tokens


def p_DOMINIO_FUNC(p):
    '''
    dominio : PRIVATE
            | PUBLIC
    '''
    print(p[1])

def p_RETURN_FUNC(p):
    '''
    return : VOID
           | FUNCTION
    '''
    print(p[1])

def p_FUNCION(p):
    '''
    funcion : dominio return NOMBRE PARIZQ parameter PARDER
    '''
    print("FUNCTION: ", p[3],p[4],p[6])

def p_PARAMETRO(p):
    '''
    parametro : vacio
              | NOMBRE parametro_extra

    '''
    print(p[1])

def p_PARAMETRO_EXTRA(p):
    '''
    parametro_extra : COMA NOMBRE parametro_extra
                    | vacio
    '''

def p_LLAMADO_FUNCION(p):
    '''
    llamado_funcion : NOMBRE PARIZQ parametro_llamado PARDER
    '''

def p_PARAMETRO_LLAMADO(p):
    '''
    parametro_llamado : vacio
                      | tipo_variable parametro_llamado_extra

    '''
    print(p[1])

def p_PARAMETRO_LLAMADO_EXTRA(p):
    '''
    parametro_llamado_extra : COMA NOMBRE parametro_llamado_extra
                            | vacio
    '''

def p_IF(p):
    '''
    if : IF PARIZQ condition PARDER
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
    expression : FOR PARIZQ DECVARIABLE ASIGNACION INT PUNTOYCOMA condition PUNTOYCOMA incdec PARDER
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

def p_CONDICION(p):
    '''
    condicion : tipo_variable condition_operator tipo_variable extra_condition
    '''

def p_CONDICION_EXTRA(p):
    '''
    condicion_extra : logic_operator tipo_variable condition_operator tipo_variable extra_condition
                    | vacio
    '''


def p_tipo_variable(p):
    '''
    tipo_variable : NOMBRE
                   | DOUBLE
                   | INT
                   | STRING
                   | FALSE
                   | TRUE
                   | llamado_funcion
    '''
    print(p[1])

def p_INCDEC(p):
    '''
    incdec : INCREMENTAR NOMBRE
           | DECREMENTAR NOMBRE
           | NOMBRE INCREMENTAR
           | NOMBRE DECREMENTAR
    '''

def p_WHILE(p):
    'while : WHILE PARIZQ condition PARDER'
    print("WHILE: ", p[1])

def p_RETURN(p):
    'expression : RETURN tipo_variable'
    print("RETURN: ", p[1])

def p_PRINT(p):
    'expression : PRINT PARIZQ tipo_variable PARDER'
    print("PRINT: ", p[1])

def p_READ(p):
    'expression : READ PARIZQ STRING PARDER'
    print("READ: ", p[1])

def p_IMPORT(p):
    'expression : IMPORT STRING'
    print("IMPORT: ", p[1])

def p_SWITCH(p):
    'expression : SWITCH expression'

def p_CASE(p):
    'case : CASE expression'

def p_BREAK(p):
    'break : BREAK PUNTOYCOMA'

def p_TABULACION(p):
    'tab : TABULACION expression'
    print("TABULACION: ", p[1])

def p_DECVARIABLE(p):
    'dec_variable : DECVARIABLE ASIGNACION tipo_variable Op_Aritmetica'
    print("DECVARIABLE: ", p[1])

def p_ASIGNACION(p):
    'asignacion : NOMBRE ASIGNACION tipo_variable Op_Aritmetica'

def p_OP_ARITMETICA(p):
    '''
    Op_Aritmetica : Operador_Aritmetico tipo_variable Op_Aritmetica
                  | vacio

    '''

def p_OPERADOR_ARITMETICO(p):
    '''
    Operador_Aritmetico : SUMA
                        | RESTA
                        | MULT
                        | DIV
    '''

def p_ASIGNACION(p):
    'expression : ASIGNACION expression'
    print("ASIGNACION: ", p[1])


def p_OPERADOR_LOGICO(p):
    '''
    operador_logico : AND
                    | OR
    '''

def p_vacio(p):
    'vacio : '

def p_error(p):
    line = p.lineno(0);
    index = p.lexpos(0);
    print("Error en la línea ", line,)
    if p:
         print("Syntax error at token", p.type)
         # Just discard the token and tell the parser it's okay.
         parser.errok()
    else:
         print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

name = input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()


while True:
    parser.parse(line)
    break
