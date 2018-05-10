import ply.yacc as yacc
from lex import tokens

#GENERAL
def p_INICIAL(p):
    '''
    inicial : funcion instrucciones
    '''

def p_INDENTACION(p):
    '''
    indentacion : vacio
                | TABULACION indentacion

    '''

#FUNCION
def p_FUNCION(p):
    '''
    funcion : definicion_funcion instrucciones
            | vacio
    '''

def p_DEFINICION_FUNCION(p):
    '''
    definicion_funcion : dominio return NOMBRE PARIZQ parameter PARDER
    '''

def p_DOMINIO_FUNC(p):
    '''
    dominio : PRIVATE
            | PUBLIC
    '''

def p_RETURN_FUNC(p):
    '''
    return : VOID
           | FUNCTION
    '''

def p_PARAMETRO(p):
    '''
    parametro : vacio
              | NOMBRE parametro_extra

    '''

def p_PARAMETRO_EXTRA(p):
    '''
    parametro_extra : COMA NOMBRE parametro_extra
                    | vacio
    '''

#INSTRUCCIONES
def p_LLAMADO_FUNCION(p):
    '''
    llamado_funcion : indentacion NOMBRE PARIZQ parametro_llamado PARDER
    '''

def p_PARAMETRO_LLAMADO(p):
    '''
    parametro_llamado : vacio
                      | tipo_variable parametro_llamado_extra

    '''

def p_PARAMETRO_LLAMADO_EXTRA(p):
    '''
    parametro_llamado_extra : COMA NOMBRE parametro_llamado_extra
                            | vacio
    '''

def p_INSTRUCCIONES(p):
    '''
    instrucciones : if NEWLINE
                  | for NEWLINE
                  | while NEWLINE
                  | print NEWLINE
                  | read NEWLINE
                  | incdec NEWLINE
                  | dec_variable NEWLINE
                  | asignacion NEWLINE
                  | llamado_funcion NEWLINE
                  | RETURN tipo_variable NEWLINE
                  | vacio
    '''

def p_IF(p):
    '''
    if : indentacion IF PARIZQ condition PARDER
    '''

def p_ELSE(p):
    'expression : indentacion ELSE expression'

def p_FOR(p):
    '''
    expression : indentacion FOR PARIZQ DECVARIABLE ASIGNACION INT PUNTOYCOMA condition PUNTOYCOMA incdec PARDER
    '''

def p_INCDEC(p):
    '''
    incdec : indentacion pre_incdec
           | indentacion post_incdec
    '''

def p_PRE_INCDEC(p):
    '''
    pre_incdec : INCREMENTAR NOMBRE
               | DECREMENTAR NOMBRE

    '''

def p_POST_INCDEC(p):
    '''
    post_incdec : NOMBRE INCREMENTAR
                | NOMBRE DECREMENTAR
    '''


def p_WHILE(p):
    'while : indentacion WHILE PARIZQ condition PARDER'

def p_PRINT(p):
    'expression : indentacion PRINT PARIZQ tipo_variable PARDER'

def p_READ(p):
    'expression : indentacion READ PARIZQ STRING PARDER'

def p_DECVARIABLE(p):
    'dec_variable : indentacion DECVARIABLE ASIGNACION tipo_variable Op_Aritmetica'

def p_ASIGNACION(p):
    'asignacion : indentacion NOMBRE ASIGNACION tipo_variable Op_Aritmetica'


#OPERACIONES Y OPERANDOS
def p_operador_condicional(p):
    '''
    operador_condicional : DIFERENTE
                       | IGUAL
                       | MAYOR
                       | MAYORIGUAL
                       | MENOR
                       | MENORIGUAL
    '''

def p_CONDICION(p):
    '''
    condicion : tipo_variable operador_condicional tipo_variable extra_condition
    '''

def p_CONDICION_EXTRA(p):
    '''
    condicion_extra : operador_logico tipo_variable operador_condicional tipo_variable extra_condition
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

def p_OPERADOR_LOGICO(p):
    '''
    operador_logico : AND
                    | OR
    '''

def p_vacio(p):
    'vacio : '

def p_error(p):
    while True:
        tok = parser.token()
        print(tok)
        if not tok or  tok.value == 'NEWLINE': break        # Get the next token
    parser.errok()
# Build the parser
parser = yacc.yacc()

name = input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()


while True:
    parser.parse(line)
    break
