import ply.yacc as yacc
from newLex import tokens

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#All the ways the program can start

def p_Start1(p):
    'Niark : methodDefinition NEWLINE Niark'

def p_Start2(p):
    'Niark : instruction NEWLINE Niark'

def p_Start3(p):
    'Niark : methodDefinition'

def p_Start4(p):
    'Niark : instruction'

	

#Method definition
def p_methodDefinition1(p):
    'methodDefinition : domain methodType NAME LEFTPAR parameters RIGHTPAR LEFTKEY NEWLINE instructions RIGHTKEY'

def p_methodDefinition2(p):
    'methodDefinition : domain methodType NAME LEFTPAR RIGHTPAR LEFTKEY NEWLINE instructions RIGHTKEY'


	
#Instructions definition
def p_instructions1(p):
    'instructions : instruction NEWLINE instructions'

def p_instructions2(p):
    'instructions : empty'
	

	
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

def p_simple6(p):
    'simple : return'

	
	
#Simple instructions definition



#Definition of the different type of asignation
def p_asignation1(p):
    'asignation : NAME ASIGNATION dataTypeAsignation'

def p_asignation2(p):
    'asignation : NAME LEFTBRACKET dataLocalizatorType RIGHTBRACKET ASIGNATION dataTypeAsignation'


#Definition of the different type of declaration	
def p_delaration1(p):
    'declaration : VARDECLARATION'

def p_delaration2(p):
    'declaration : VARDECLARATION ASIGNATION dataTypeAsignation'

def p_delaration4(p):
    'declaration : VARDECLARATION LEFTBRACKET dataLocalizatorType RIGHTBRACKET'
	
def p_delaration6(p):
    'declaration : VARDECLARATION LEFTBRACKET dataLocalizatorType RIGHTBRACKET ASIGNATION dataTypeAsignation'



#Data type asignation
def p_dataType1(p):
    'dataTypeAsignation : variable'

def p_dataType2(p):
    'dataTypeAsignation : variableType'

def p_dataType3(p):
    'dataTypeAsignation : arithmetic'



#Definition of the read instruction
def p_read1(p):
    'read : READ LEFTPAR NAME RIGHTPAR'
	
def p_read2(p):
    'read : READ LEFTPAR VARDECLARATION RIGHTPAR'

	
#Definition of the print instruction
def p_print(p):
    'print : PRINT LEFTPAR sendingVariables RIGHTPAR'

	
#Definition of the systemcall instruction
def p_functioncall1(p):
    'functionCall : NAME LEFTPAR sendingVariables RIGHTPAR'
	
def p_functioncall2(p):
    'functionCall : NAME LEFTPAR empty RIGHTPAR'



#Definition of the return function
def p_return1(p):
    'return : RETURN sendingVariable'



#The different types of complex instructions
def p_complex1(p):
    'complex : ifCondition'

def p_complex2(p):
    'complex : forCondition'

def p_complex3(p):
    'complex : whileCondition'



#Definition of the if conditional
def p_ifCondition1(p):
    'ifCondition : IF LEFTPAR conditionals RIGHTPAR LEFTKEY NEWLINE instructions RIGHTKEY'

def p_ifCondition2(p):
    'ifCondition : IF LEFTPAR conditionals RIGHTPAR LEFTKEY NEWLINE instructions RIGHTKEY ELSE LEFTKEY NEWLINE instructions RIGHTKEY'

def p_ifCondition3(p):
    'ifCondition : IF LEFTPAR conditionals RIGHTPAR LEFTKEY NEWLINE instructions RIGHTKEY ELSE ifCondition'



#Definition of the for conditional
def p_forCondition(p):
    'forCondition : FOR LEFTPAR declaration SEMICOLON conditionals SEMICOLON incdec RIGHTPAR LEFTKEY NEWLINE instructions RIGHTKEY'



#Definition of the while conditional
def p_whileCondition(p):
    'whileCondition : WHILE LEFTPAR conditionals RIGHTPAR LEFTKEY NEWLINE instructions RIGHTKEY'



#Conditionals definition
def p_conditionals1(p):
    'conditionals : condition'

def p_conditionals2(p):
    'conditionals : condition conditionalOp conditionals'

def p_conditionals3(p):
    'conditionals : LEFTPAR conditionals RIGHTPAR conditionalOp conditionals'

def p_conditionals4(p):
    'conditionals : LEFTPAR conditionals RIGHTPAR'



#Condition definition
def p_condition1(p):
    'condition : sendingVariable conditionOp sendingVariable'



#Increase decrease definition
def p_incdec1(p):
    'incdec : preIncdec'

def p_incdec2(p):
    'incdec : postIncdec'



#Pre Increase decrease definition
def p_preIncdec1(p):
    'preIncdec : INCREASE variable'

def p_preIncdec2(p):
    'preIncdec : DECREASE variable'



#Post Increase decrease definition
def p_postIncdec1(p):
    'postIncdec : variable INCREASE'

def p_postIncdec2(p):
    'postIncdec : variable DECREASE'




#Conditionals operators definition
def p_conditionalOp1(p):
    'conditionalOp : AND'

def p_conditionalOp2(p):
    'conditionalOp : OR'



#Condition operators definition
def p_conditionOp1(p):
    'conditionOp : EQUALS'

def p_conditionOp2(p):
    'conditionOp : DIFFERENT'

def p_conditionOp3(p):
    'conditionOp : LESSER'

def p_conditionOp4(p):
    'conditionOp : GREATER'

def p_conditionOp5(p):
    'conditionOp : LESSEREQUAL'

def p_conditionOp6(p):
    'conditionOp : GREATEREQUAL'



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
def p_sendingVariables1(p):
    'sendingVariables : sendingVariable COMMA sendingVariables'

def p_sendingVariables2(p):
    'sendingVariables : sendingVariable'



#Sending variables definition
def p_sendingVariable1(p):
    'sendingVariable : variableType'

def p_sendingVariable2(p):
    'sendingVariable : arithmetic'

def p_sendingVariable3(p):
    'sendingVariable : variable'

def p_sendingVariable4(p):
    'sendingVariable : functionCall'




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



#Data localization types in Vectors
def p_dataLocalizatorType1(p):
    'dataLocalizatorType : INT'

def p_dataLocalizatorType2(p):
    'dataLocalizatorType : variable'

def p_dataLocalizatorType3(p):
    'dataLocalizatorType : arithmetic'


#Varialbe types definition
def p_variableType1(p):
    'variableType : numberType'

def p_variableType2(p):
    'variableType : stringType'

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
    'arithmetic : moreArithmetic arithmeticOp arithmeticDataType'

def p_arithmetic2(p):
    'arithmetic : LEFTPAR arithmetic RIGHTPAR'

def p_arithmetic3(p):
    'arithmetic : moreArithmetic arithmeticOp LEFTPAR arithmetic RIGHTPAR'

def p_arithmetic4(p):
    'arithmetic : arithmeticOp arithmeticDataType'

def p_moreArithmetic1(p):
    'moreArithmetic : arithmeticDataType'

def p_moreArithmetic2(p):
    'moreArithmetic : arithmetic'



#Definition of arithmetic data types
def p_arithmeticDataType1(p):
    'arithmeticDataType : numberType'

def p_arithmeticDataType2(p):
    'arithmeticDataType : variable'

def p_arithmeticDataType3(p):
    'arithmeticDataType : functionCall'



#Definition of arithmetic operators
def p_arithmeticOp1(p):
    'arithmeticOp : SUM'

def p_arithmeticOp2(p):
    'arithmeticOp : SUBSTRACTION'

def p_arithmeticOp3(p):
    'arithmeticOp : MULTIPLICATION'

def p_arithmeticOp4(p):
    'arithmeticOp : DIVISION'

def p_error(p):
    if p:
        print(bcolors.FAIL+"Error:" +bcolors.ENDC ,bcolors.HEADER + p.type+ bcolors.ENDC, bcolors.BOLD + "", p.value,"" + bcolors.ENDC, bcolors.WARNING + "Sucedió en la línea:" + bcolors.ENDC, bcolors.UNDERLINE + "" ,p.lineno,"" + bcolors.ENDC)
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