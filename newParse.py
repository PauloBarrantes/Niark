import ply.yacc as yacc

#All the ways the program can start

def p_Start1(p):
    'Niark : methodDefinition newlines Niark'

def p_Start2(p):
    'Niark : instruction newlines Niark'

def p_Start3(p):
    'Niark : methodDefinition'

def p_Start4(p):
    'Niark : instruction'

	
	
#Method definition
def p_methodDefinition1(p):
    'methodDefinition : domain methodType NAME LEFTPAR parameters RIGHTPAR LEFTKEY newlines instructions RIGHTKEY'

def p_methodDefinition2(p):
    'methodDefinition : domain methodType NAME LEFTPAR VOID RIGHTPAR LEFTKEY newlines instructions RIGHTKEY'

	
	
#Instructions definition
def p_instructions(p):
    'instructions: instruction newlines instructions'
	
	
	
#The forms an instruction can become
def p_Instruction1(p):
    'instruction : simple'

def p_Instruction2(p):
    'instruction : complex'

	
	
	
#The different types of simple instructions
def p_simple1(p):
    'simple : asignation'

def p_simple2(p):
    'simple : declaration'

def p_simple3(p):
    'simple : read'

def p_simple4(p):
    'simple : print'

def p_simple5(p):
    'simple : functionCall'

	
	
#Simple instructions definition



#Definition of the different type of asignation
def p_asignation1(p):
    'asignation : NAME ASIGNATION arithmetic'
	
def p_asignation2(p):
    'asignation : NAME ASIGNATION variable'

def p_asignation3(p):
    'asignation : NAME LEFTBRACKET variable RIGHTBRACKET ASIGNATION arithmetic'
	
def p_asignation4(p):
    'asignation : NAME LEFTBRACKET variable RIGHTBRACKET ASIGNATION variable'
	
def p_asignation5(p):
    'asignation : NAME LEFTBRACKET arithmetic RIGHTBRACKET ASIGNATION arithmetic'

	
#Definition of the different type of declaration	
def p_delaration1(p):
    'declaration : VARDECLARATION'

def p_delaration2(p):
    'declaration : VARDECLARATION ASIGNATION arithmetic'
	
def p_delaration3(p):
    'declaration : VARDECLARATION ASIGNATION variable'

def p_delaration4(p):
    'declaration : VARDECLARATION LEFTBRACKET variable RIGHTBRACKET'
	
def p_delaration5(p):
    'declaration : VARDECLARATION LEFTBRACKET arithmetic RIGHTBRACKET'
	
def p_delaration6(p):
    'declaration : VARDECLARATION LEFTBRACKET variable RIGHTBRACKET ASIGNATION arithmetic'
	
def p_delaration7(p):
    'declaration : VARDECLARATION LEFTBRACKET variable RIGHTBRACKET ASIGNATION variable'
	
def p_delaration8(p):
    'declaration : VARDECLARATION LEFTBRACKET arithmetic RIGHTBRACKET ASIGNATION arithmetic'


#Definition of the read instruction
def p_read1(p):
    'read : READ LEFTPAR NAME RIGHTPAR'
	
def p_read2(p):
    'read : READ LEFTPAR VARDECLARATION RIGHTPAR'

	
#Definition of the print instruction
def p_print(p):
    'print : PRINT LEFTPAR variables RIGHTPAR'

	
#Definition of the systemcall instruction
def p_functioncall1(p):
    'functionCall: NAME LEFTPAR variables RIGHTPAR'
	
def p_functioncall2(p):
    'functionCall: NAME LEFTPAR VOID RIGHTPAR'
	
	
	
#The different types of complex instructions
def p_complex1(p):
    'complex : ifCondition'

def p_complex2(p):
    'complex : forCondition'

def p_complex3(p):
    'complex : whileCondition'


	
#Definition of the if conditional
def p_ifCondition1(p):
    'ifCondition : IF LEFTPAR conditionals RIGHTPAR LEFTKEY ignore instructions ignore RIGHTKEY'

def p_ifCondition2(p):
    'ifCondition : IF LEFTPAR conditionals RIGHTPAR LEFTKEY ignore instructions ignore RIGHTKEY ignore ELSE LEFTKEY ignore instructions ignore RIGHTKEY'
	
def p_ifCondition3(p):
    'ifCondition : IF LEFTPAR conditionals RIGHTPAR LEFTKEY ignore instructions ignore RIGHTKEY ignore ELSE ignore ifCondition'
	
	
#Definition of the for conditional
def p_forCondition(p):
    'forCondition : FOR LEFTPAR declaration SEMICOLON conditionals SEMICOLON incdec RIGHTPAR LEFTKEY ignore instructions ignore RIGHTKEY'	
	
	
	
#Domain definition
def p_domain1(p):
    'domain : PUBLIC'

def p_domain2(p):
    'domain : PRIVATE'

	
	
#Method type definition
def p_methodType1(p):
    'methodType : VOID'

def p_methodType2(p):
    'methodType : FUNCTION'

	
	
#Parameters definition
def p_parameters1(p):
    'parameters : NAME COMMA parameters'

def p_parameters2(p):
    'parameters : NAME'
	

	
#Varialbes definition
def p_variables1(p):
    'variables : variable COMMA variables'
	
def p_variables2(p):
    'variables : variable'
	
	

#Varialbe definition
def p_variable1(p):
    'variable : NAME'
	
def p_variable2(p):
    'variable : vectorVariable'
	
	
	

#Vector	definition
def p_vectorVariable1(p):
    'vectorVariable : NAME LEFTBRACKET arithmetic RIGHTBRACKET'
	
def p_vectorVariable2(p):
    'vectorVariable : NAME LEFTBRACKET INT RIGHTBRACKET'
	
def p_vectorVariable3(p):
    'vectorVariable : NAME LEFTBRACKET variable RIGHTBRACKET'
	
	
	
#Varialbe types definition
def p_variableType1(p):
    'variableType : numberType'
	
def p_variableType2(p):
    'variableType : strngType'
	
def p_variableType3(p):
    'variableType : booleanType'
	

#Number type definition
def p_numberType1(p):
    'numberType : INT'
	
def p_numberType2(p):
    'numberType : DOUBLE'
	
#String type definition
def p_stringType(p):
    'stringType : STRING'
	
#Boolean type definition	
def p_booleanType1(p):
    'booleanType : FALSE'
	
def p_booleanType2(p):
    'booleanType : TRUE'


	
#Arithmetic definition
def p_arithmetic1(p):
    'arithmetic : numberType arithmeticOp moreArithmetic'

def p_arithmetic2(p):
    'arithmetic : LEFTPAR arithmetic RIGHTPAR'
	
def p_arithmetic3(p):
    'arithmetic : LEFTPAR arithmetic RIGHTPAR arithmeticOp moreArithmetic'
	
def p_moreArithmetic1(p):
    'moreArithmetic : numberType'
	
def p_moreArithmetic2(p):
    'moreArithmetic : atithmetic'
	

	
#Definition of arithmetic operators
def p_arithmeticOp1(p):
    'arithmeticOp : SUM'
	
def p_arithmeticOp1(p):
    'arithmeticOp : SUBSTRACTION'
	
def p_arithmeticOp1(p):
    'arithmeticOp : MULTIPLICATION'
	
def p_arithmeticOp1(p):
    'arithmeticOp : DIVISION'



# Build the parser
parser = yacc.yacc()

name = input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()


while True:
    parser.parse(line)
    break