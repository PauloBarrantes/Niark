import ply.yacc as yacc
from lex import tokens

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#GENERAL

def p_Niark(p):
    '''
    Niark : definicion_funcion LLAVEIZQ NEWLINE instrucciones LLAVEDER Niark
    '''

def p_Niark1(p):
    '''
    Niark : instrucciones Niark
    '''

def p_Niark2(p):
    '''
    Niark : vacio
    '''

def p_CAMBIOS_DE_LINEA(p):
    '''
    cambios_linea : NEWLINE cambios_linea
    '''

def p_CAMBIOS_DE_LINEA1(p):
    '''
    cambios_linea : vacio
    '''

def p_INDENTACION(p):
    '''
    indentacion : TABULACION indentacion
    '''

def p_INDENTACION1(p):
    '''
    indentacion : vacio
    '''

#FUNCION
def p_DEFINICION_FUNCION(p):
    'definicion_funcion : dominio tipo_return NOMBRE PARIZQ parametro PARDER'

def p_DOMINIO_FUNC(p):
    '''
    dominio : PRIVATE
            |  PUBLIC
    ''' 

def p_RETURN_FUNC(p):
    '''
    tipo_return : VOID
    '''
    print(p[1])

def p_RETURN_FUNC1(p):
    '''
    tipo_return : FUNCTION
    '''
    print(p[1])

def p_PARAMETRO(p):
    '''
    parametro : vacio
    '''

def p_PARAMETRO1(p):
    '''
    parametro : NOMBRE parametro_extra

    '''

def p_PARAMETRO_EXTRA(p):
    '''
    parametro_extra : COMA NOMBRE parametro_extra
    '''

def p_PARAMETRO_EXTRA1(p):
    '''
    parametro_extra : vacio
    '''

#INSTRUCCIONES
def p_LLAMADO_FUNCION(p):
    '''
    llamado_funcion : NOMBRE PARIZQ parametro_llamado PARDER
    '''

def p_LLAMADO_FUNCION01(p):
    '''
    llamado_funcion : NOMBRE PARIZQ vacio PARDER
    '''

def p_PARAMETRO_LLAMADO(p):
    '''
    parametro_llamado : tipo_variable parametro_llamado_extra
    '''

def p_PARAMETRO_LLAMADO1(p):
    '''
    parametro_llamado : op_aritmetica parametro_llamado_extra

    '''

def p_PARAMETRO_LLAMADO_EXTRA(p):
    '''
    parametro_llamado_extra : COMA parametro_llamado
    '''

def p_PARAMETRO_LLAMADO_EXTRA1(p):
    '''
    parametro_llamado_extra : vacio
    '''

def p_INSTRUCCION(p):
    '''
    instruccion : condicion_if
                | condicion_else
                | ciclo_for
                | ciclo_while
                | imprimir
                | leer
                | incdec
                | dec_variable
                | dec_vector
                | usar_vector
                | asigna
                | asignacion_vector
                | llamado_funcion
                | retorno
                | comentario
    '''

def p_COMENTARIO(p):
    '''
    comentario : COMENTARIO
               | vacio
    '''

def p_INSTRUCCIONES(p):
    '''
    instrucciones : indentacion instruccion NEWLINE instrucciones
                  | vacio
    '''


def p_CONDICION_IF(p):
    '''
    condicion_if : IF PARIZQ condicion PARDER LLAVEIZQ NEWLINE instrucciones LLAVEDER
    '''

def p_CONDICION_ELSE(p):
    '''
    condicion_else : ELSE LLAVEIZQ NEWLINE instrucciones indentacion LLAVEDER
                   | ELSE condicion_if
    '''

def p_CICLO_FOR(p):
    '''
    ciclo_for : FOR PARIZQ dec_variable PUNTOYCOMA condicion PUNTOYCOMA incdec PARDER LLAVEIZQ NEWLINE instrucciones indentacion LLAVEDER
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
    'ciclo_while : WHILE PARIZQ condicion PARDER LLAVEIZQ instrucciones indentacion LLAVEDER'

def p_IMPRIMIR(p):
    'imprimir : PRINT PARIZQ tipo_variable PARDER'

def p_LEER(p):
    'leer : READ PARIZQ NOMBRE PARDER'


def p_DEC_VARIABLE(p):
    '''
    dec_variable : DECVARIABLE ASIGNACION op_aritmetica
                 | DECVARIABLE ASIGNACION tipo_variable
    '''

def p_DEC_VECTOR(p):
    '''
    dec_vector : DECVARIABLE CORCHETEIZQ NOMBRE CORCHETEDER
               | DECVARIABLE CORCHETEIZQ INT CORCHETEDER
               | DECVARIABLE CORCHETEIZQ op_aritmetica CORCHETEDER
    '''

def p_USAR_VECTOR(p):
    '''
    usar_vector : vector ASIGNACION op_aritmetica
               | vector ASIGNACION tipo_variable
    '''

def p_VECTOR(p):
    '''
    vector : NOMBRE CORCHETEIZQ NOMBRE CORCHETEDER
           | NOMBRE CORCHETEIZQ INT CORCHETEDER
           | NOMBRE CORCHETEIZQ op_aritmetica CORCHETEDER
    '''

def p_ASIGNA(p):
    '''
    asigna : NOMBRE ASIGNACION op_aritmetica
           | NOMBRE ASIGNACION tipo_variable
    '''

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
    condicion : comparables operador_condicional comparables condicion_extra
              | PARIZQ comparables operador_condicional comparables condicion_extra PARDER condicion_extra
    '''

def p_CONDICION_EXTRA(p):
    '''
    condicion_extra : operador_logico condicion
                    | vacio
    '''

def p_COMPARABLES(p):
    '''
    comparables : tipo_variable
                | op_aritmetica
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
                   | vector
    '''

def p_OP_ARITMETICA(p):
    '''op_aritmetica : op_aritmetica_extra operador_aritmetico tipo_variable
                     | op_aritmetica_extra operador_aritmetico PARIZQ op_aritmetica_extra operador_aritmetico tipo_variable PARDER
                     | PARIZQ op_aritmetica_extra operador_aritmetico tipo_variable PARDER'''

def p_OP_ARITMETICA_EXTRA(p):
    '''
    op_aritmetica_extra : tipo_variable
                        | op_aritmetica
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

def p_error(p):
    if p:
        print(bcolors.FAIL+"Error:" +bcolors.ENDC ,bcolors.HEADER + p.type+ bcolors.ENDC, bcolors.BOLD + "", p.value,"" + bcolors.ENDC, bcolors.WARNING + "Sucedió en la línea:" + bcolors.ENDC, bcolors.UNDERLINE + "" ,p.lineno,"" + bcolors.ENDC)
         # Just discard the token and tell the parser it's okay.
        parser.errok()

def p_vacio(p):
    'vacio : '


# Build the parser
parser = yacc.yacc()

name = input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()


while True:
    parser.parse(line)
    break
