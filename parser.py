import ply.yacc as yacc
from lex import tokens

#GENERAL
def p_INICIAL(p):
    '''
    inicial : funcion inicial instrucciones NEWLINE
            | vacio
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
    definicion_funcion : dominio return NOMBRE PARIZQ parametro PARDER
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
                  | dec_vector NEWLINE
                  | asignacion NEWLINE
                  | llamado_funcion NEWLINE
                  | retorno NEWLINE
                  | vacio
    '''

def p_IF(p):
    '''
    if : indentacion IF PARIZQ condicion PARDER
    '''

def p_ELSE(p):
    'else : indentacion ELSE NEWLINE'

def p_FOR(p):
    '''
    for : indentacion FOR PARIZQ DECVARIABLE ASIGNACION INT PUNTOYCOMA condicion PUNTOYCOMA incdec PARDER
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
    'while : indentacion WHILE PARIZQ condicion PARDER'

def p_PRINT(p):
    'print : indentacion PRINT PARIZQ tipo_variable PARDER'

def p_READ(p):
    'read : indentacion READ PARIZQ STRING PARDER'

def p_DECVARIABLE(p):
    'dec_variable : indentacion DECVARIABLE ASIGNACION op_aritmetica'

def p_DECVECTOR(p):
    '''
    dec_vector : indentacion DECVARIABLE CORCHETEIZQ NOMBRE CORCHETEDER ASIGNACION op_aritmetica
               | indentacion DECVARIABLE CORCHETEIZQ INT CORCHETEDER ASIGNACION op_aritmetica
    '''

def p_ASIGNACION(p):
    'asignacion : indentacion NOMBRE ASIGNACION op_aritmetica'

def p_ASIGNACIONVECTOR(p):
    '''
    asignacion_vector : indentacion NOMBRE CORCHETEIZQ NOMBRE CORCHETEDER ASIGNACION op_aritmetica
                      | indentacion NOMBRE CORCHETEIZQ INT CORCHETEDER ASIGNACION op_aritmetica
    '''

def p_RETORNAR(p):
    '''
    retorno : RETURN tipo_variable
            | RETURN op_aritmetica
    '''


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
    condicion : tipo_variable operador_condicional tipo_variable condicion_extra
    '''

def p_CONDICION_EXTRA(p):
    '''
    condicion_extra : operador_logico tipo_variable operador_condicional tipo_variable condicion_extra
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

def p_op_aritmetica(p):
    '''
    op_aritmetica : tipo_variable operador_aritmetico tipo_variable op_aritmetica_extra
                  | vacio

    '''

def p_op_aritmetica(p):
    '''
    op_aritmetica_extra : operador_aritmetico tipo_variable op_aritmetica_extra
                        | operador_aritmetico PARIZQ tipo_variable op_aritmetica_extra PARDER
                        | vacio

    '''

def p_operador_aritmetico(p):
    '''
    operador_aritmetico : SUMA
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
