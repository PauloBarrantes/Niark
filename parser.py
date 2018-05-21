import ply.yacc as yacc
from lex import tokens

#GENERAL
def p_Niark(p):
    '''
    Niark : definicion_funcion instrucciones Niark NEWLINE
          | vacio
    '''

def p_INDENTACION(p):
    '''
    indentacion : TABULACION indentacion
                | vacio
    '''

#FUNCION
def p_DEFINICION_FUNCION(p):
    'definicion_funcion : dominio tipo_return NOMBRE PARIZQ parametro PARDER'
    print("Agarra def func")

def p_DOMINIO_FUNC(p):
    '''
    dominio : PRIVATE
            | PUBLIC
    '''

def p_RETURN_FUNC(p):
    '''
    tipo_return : VOID
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

def p_INSTRUCCION(p):
    '''
    instruccion : condicion_if NEWLINE
                | condicion_else NEWLINE
                | ciclo_for NEWLINE
                | ciclo_while NEWLINE
                | imprimir NEWLINE
                | leer NEWLINE
                | incdec NEWLINE
                | dec_variable NEWLINE
                | dec_vector NEWLINE
                | asigna NEWLINE
                | asignacion_vector NEWLINE
                | llamado_funcion NEWLINE
                | retorno NEWLINE
    '''

def p_INSTRUCCIONES(p):
    '''
    instrucciones : indentacion instruccion concat_instruccion
                  | vacio
    '''

def p_CONCAT_INSTRUCCION(p):
    '''
    concat_instruccion : instruccion concat_instruccion
                       | vacio
    '''

def p_CONDICION_IF(p):
    '''
    condicion_if : IF PARIZQ condicion PARDER
    '''

def p_CONDICION_ELSE(p):
    '''
    condicion_else : ELSE
                   | ELSE condicion_if
    '''

def p_CICLO_FOR(p):
    '''
    ciclo_for : FOR PARIZQ DECVARIABLE ASIGNACION INT PUNTOYCOMA condicion PUNTOYCOMA incdec PARDER
    '''

def p_INCDEC(p):
    '''
    incdec : pre_incdec
           | post_incdec
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


def p_CICLO_WHILE(p):
    'ciclo_while : WHILE PARIZQ condicion PARDER'

def p_IMPRIMIR(p):
    'imprimir : PRINT PARIZQ tipo_variable PARDER'
    print("Agarra print")

def p_LEER(p):
    'leer : READ PARIZQ NOMBRE PARDER'
    print("Agarra read")


def p_DEC_VARIABLE(p):
    '''
    dec_variable : DECVARIABLE ASIGNACION op_aritmetica
                 | DECVARIABLE ASIGNACION tipo_variable
    '''
    print("Agarra declaracion")

def p_DEC_VECTOR(p):
    '''
    dec_vector : DECVARIABLE CORCHETEIZQ NOMBRE CORCHETEDER ASIGNACION op_aritmetica
               | DECVARIABLE CORCHETEIZQ INT CORCHETEDER ASIGNACION op_aritmetica
               | DECVARIABLE CORCHETEIZQ NOMBRE CORCHETEDER ASIGNACION tipo_variable
               | DECVARIABLE CORCHETEIZQ INT CORCHETEDER ASIGNACION tipo_variable
    '''

def p_ASIGNA(p):
    '''
    asigna : NOMBRE ASIGNACION op_aritmetica
           | NOMBRE ASIGNACION tipo_variable
    '''
    print("Agarra asignacion")

def p_ASIGNACIONVECTOR(p):
    '''
    asignacion_vector : NOMBRE CORCHETEIZQ NOMBRE CORCHETEDER ASIGNACION op_aritmetica
                      | NOMBRE CORCHETEIZQ INT CORCHETEDER ASIGNACION op_aritmetica
                      | NOMBRE CORCHETEIZQ NOMBRE CORCHETEDER ASIGNACION tipo_variable
                      | NOMBRE CORCHETEIZQ INT CORCHETEDER ASIGNACION tipo_variable
    '''

def p_RETORNAR(p):
    '''
    retorno : RETURN tipo_variable
            | RETURN op_aritmetica
    '''


#OPERACIONES Y OPERANDOS
def p_OPERADOR_CONDICIONAL(p):
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

def p_TIPO_VARIABLE(p):
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
    'op_aritmetica : tipo_variable operador_aritmetico tipo_variable op_aritmetica_extra'

def p_OP_ARITMETICA_EXTRA(p):
    '''
    op_aritmetica_extra : operador_aritmetico tipo_variable op_aritmetica_extra
                        | operador_aritmetico PARIZQ tipo_variable op_aritmetica_extra PARDER
                        | vacio
    '''

def p_OPERADOR_ARITMETICO(p):
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
    print("ERROR")
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
