import ply.yacc as yacc
from newLex import tokens
from SimpleAST import *


globalFile = GlobalFile()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# All the ways the program can start
def p_start(p):
    '''
    start : decvariable NEWLINE start
    '''
    globalFile.instructionList.append(p[1])
    for val in globalFile.instructionList:
        val.imprimir()

def p_start1(p):
    '''
    start : empty
    '''

def p_decVariable1(p):
    '''
    decvariable : VARDECLARATION ASIGNATION INT
    '''
    p[0] = VariableDeclaration(p[1])

#Data type asignation
def p_dataType1(p):
    'dataTypeAsignation : NAME'
    p[0] = p[1]

def p_dataType2(p):
    'dataTypeAsignation : INT'
    p[0] = p[1]

def p_dataType3(p):
    'dataTypeAsignation : STRING'
    p[0] = p[1]

def p_error(p):
    if p:
        print(bcolors.FAIL + "Error:" + bcolors.ENDC, bcolors.HEADER + p.type + bcolors.ENDC, bcolors.BOLD + "",
              p.value, "" + bcolors.ENDC, bcolors.WARNING + "Sucedió en la línea:" + bcolors.ENDC,
              bcolors.UNDERLINE + "", p.lineno, "" + bcolors.ENDC)
        # Just discard the token and tell the parser it's okay.
        parser.errok()


def p_empty(p):
    'empty : '


# Build the parser
parser = yacc.yacc()

name = input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()

while True:
    parser.parse(line)
    break
