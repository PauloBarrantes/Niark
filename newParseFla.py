import ply.yacc as yacc
from newLex import tokens
from ASTStructure import *

globalFile = File()

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
    print(p[1].name)
    globalFile.functions.append(p[1])
    p[0] = globalFile

def p_Start2(p):
    'Niark : instruction NEWLINE Niark'
    globalFile.instructionList.append(p[1])
    print(p[1].name)
    p[0] = globalFile
    print("Hace Niark.")

def p_Start3(p):
    'Niark : methodDefinition'
    globalFile.functions.append(p[1])
    print(p[1].name)
    p[0] = globalFile
    print("Hace Niark.")

def p_Start4(p):
    'Niark : instruction'
    globalFile.instructionList.append(p[1])
    globalFile.printObject()
    p[0] = globalFile
    print("Hace Niark.")


#Method definition
def p_methodDefinition1(p):
    'methodDefinition : domain methodType NAME LEFTPAR parameters RIGHTPAR LEFTKEY NEWLINE instructions RIGHTKEY'
    funcion = Function(p[1], p[2], p[3], p[5])
    funcion.instructionList = p[9]
    p[0] = funcion
    print(1)
    print(p[0].name)
    print("Tam" , len(funcion.instructionList))
    funcion.printObject()
def p_methodDefinition2(p):
    'methodDefinition : domain methodType NAME LEFTPAR RIGHTPAR LEFTKEY NEWLINE instructions RIGHTKEY'
    funcion = Function(p[1], p[2], p[3], p[5])
    funcion.instructionList = p[9]
    print(2)
    p[0] = funcion


#Instructions definition
def p_instructions1(p):
    'instructions : instruction NEWLINE instructions'
    array = [p[1]]
    array.append(p[3])
    p[0] = array

def p_instructions2(p):
    'instructions : empty'
    p[0] = p[1]



#The forms an instruction can become
def p_Instruction1(p):
    'instruction : simple'
    p[0] = p[1]

def p_Instruction2(p):
    'instruction : complex'
    p[0] = p[1]



#The different types of simple instructions
def p_simple1(p):
    'simple : asignation'
    p[0] = p[1]

def p_simple2(p):
    'simple : declaration'
    p[0] = p[1]

def p_simple3(p):
    'simple : read'
    p[0] = p[1]

def p_simple4(p):
    'simple : print'
    p[0] = p[1]

def p_simple5(p):
    'simple : functionCall'
    p[0] = p[1]

def p_simple6(p):
    'simple : return'
    p[0] = p[1]



#Simple instructions definition



#Definition of the different type of asignation
def p_asignation1(p):
    'asignation : NAME ASIGNATION dataTypeAsignation'
    p[0] = VariableAssignation(p[1], p[3])

def p_asignation2(p):
    'asignation : NAME LEFTBRACKET dataLocalizatorType RIGHTBRACKET ASIGNATION dataTypeAsignation'
    P[0] = ArrayAssignation(p[1], p[2], p[6])

#Definition of the different type of declaration
def p_delaration1(p):
    'declaration : VARDECLARATION'
    p[0] = VariableDeclaration(Variable(p[1]))

def p_delaration2(p):
    'declaration : VARDECLARATION ASIGNATION dataTypeAsignation'
    variable = VariableDeclaration(Variable(p[1]))
    variable.variable.addValue(p[3])
    p[0] = variable
    print(p[0].variable.name)

def p_delaration4(p):
    'declaration : VARDECLARATION LEFTBRACKET dataLocalizatorType RIGHTBRACKET'
    p[0] = Array(p[1], p[3])

def p_delaration6(p):
    'declaration : VARDECLARATION LEFTBRACKET dataLocalizatorType RIGHTBRACKET ASIGNATION dataTypeAsignation'
    array = Array(p[1], p[3])
    array.addValue(p[6])
    p[0] = array




#Data type asignation
def p_dataType1(p):
    'dataTypeAsignation : variable'
    p[0] = p[1]

def p_dataType2(p):
    'dataTypeAsignation : variableType'
    p[0] = p[1]

def p_dataType3(p):
    'dataTypeAsignation : arithmetic'
    p[0] = p[1]



#Definition of the read instruction
def p_read1(p):
    'read : READ LEFTPAR NAME RIGHTPAR'
    p[0] = Instructions(p[3], "READ")

# def p_read2(p):
#     'read : READ LEFTPAR VARDECLARATION RIGHTPAR'
#     p[0] = Instructions(p[3], "READ")


#Definition of the print instruction
def p_print(p):
    'print : PRINT LEFTPAR sendingVariables RIGHTPAR'
    p[0] = Instructions(p[3], "PRINT")


#Definition of the systemcall instruction
def p_functioncall1(p):
    'functionCall : NAME LEFTPAR sendingVariables RIGHTPAR'
    p[0] = FunctionCall(p[1], p[3])

def p_functioncall2(p):
    'functionCall : NAME LEFTPAR empty RIGHTPAR'
    p[0] = FunctionCall(p[1], p[3])


#Definition of the return function
def p_return1(p):
    'return : RETURN sendingVariable'
    p[0] = Instructions(p[2], "RETURN")



#The different types of complex instructions
def p_complex1(p):
    'complex : ifCondition'
    p[0] = p[1]

def p_complex2(p):
    'complex : forCondition'
    p[0] = p[1]

def p_complex3(p):
    'complex : whileCondition'
    p[0] = p[1]



#Definition of the if conditional
def p_ifCondition1(p):
    'ifCondition : IF LEFTPAR conditionals RIGHTPAR LEFTKEY NEWLINE instructions RIGHTKEY'
    unIf = If(p[3])
    unIf.instructionList.append(p[7])

def p_ifCondition2(p):
    'ifCondition : IF LEFTPAR conditionals RIGHTPAR LEFTKEY NEWLINE instructions RIGHTKEY ELSE LEFTKEY NEWLINE instructions RIGHTKEY'
    unIf = If(p[3])
    unIf.instructionList.append(p[7])
    unElse = Else()
    unElse.instructionList.append(p[12])

def p_ifCondition3(p):
    'ifCondition : IF LEFTPAR conditionals RIGHTPAR LEFTKEY NEWLINE instructions RIGHTKEY ELSE ifCondition'
    unIf = If(p[3])
    unIf.instructionList.append(p[7])



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
    p[0] = p[1]

def p_conditionalOp2(p):
    'conditionalOp : OR'
    p[0] = p[1]



#Condition operators definition
def p_conditionOp1(p):
    'conditionOp : EQUALS'
    p[0] = p[1]

def p_conditionOp2(p):
    'conditionOp : DIFFERENT'
    p[0] = p[1]

def p_conditionOp3(p):
    'conditionOp : LESSER'
    p[0] = p[1]

def p_conditionOp4(p):
    'conditionOp : GREATER'
    p[0] = p[1]

def p_conditionOp5(p):
    'conditionOp : LESSEREQUAL'
    p[0] = p[1]

def p_conditionOp6(p):
    'conditionOp : GREATEREQUAL'
    p[0] = p[1]



#Domain definition
def p_domain1(p):
    'domain : PUBLIC'
    p[0] = p[1]

def p_domain2(p):
    'domain : PRIVATE'
    p[0] = p[1]



#Method type definition
def p_methodType1(p):
    'methodType : VOID'
    p[0] = p[1]

def p_methodType2(p):
    'methodType : FUNCTION'
    p[0] = p[1]



#Parameters definition
def p_parameters1(p):
    'parameters : NAME COMMA parameters'

def p_parameters2(p):
    'parameters : NAME'
    p[0] = p[1]



#Varialbes definition
def p_sendingVariables1(p):
    'sendingVariables : sendingVariable COMMA sendingVariables'

def p_sendingVariables2(p):
    'sendingVariables : sendingVariable'
    p[0] = p[1]



#Sending variables definition
def p_sendingVariable1(p):
    'sendingVariable : variableType'
    p[0] = p[1]

def p_sendingVariable2(p):
    'sendingVariable : arithmetic'
    p[0] = p[1]

def p_sendingVariable3(p):
    'sendingVariable : variable'
    p[0] = p[1]

def p_sendingVariable4(p):
    'sendingVariable : functionCall'
    p[0] = p[1]




#Varialbe definition
def p_variable1(p):
    'variable : NAME'
    p[0] = p[1]

def p_variable2(p):
    'variable : vectorVariable'
    p[0] = p[1]




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
    p[0] = p[1]

def p_dataLocalizatorType2(p):
    'dataLocalizatorType : variable'
    p[0] = p[1]

def p_dataLocalizatorType3(p):
    'dataLocalizatorType : arithmetic'
    p[0] = p[1]


#Varialbe types definition
def p_variableType1(p):
    'variableType : numberType'
    p[0] = p[1]

def p_variableType2(p):
    'variableType : stringType'
    p[0] = p[1]

def p_variableType3(p):
    'variableType : booleanType'
    p[0] = p[1]



#Number type definition
def p_numberType1(p):
    'numberType : INT'
    p[0] = p[1]

def p_numberType2(p):
    'numberType : DOUBLE'
    p[0] = p[1]

#String type definition
def p_stringType(p):
    'stringType : STRING'
    p[0] = p[1]

#Boolean type definition
def p_booleanType1(p):
    'booleanType : FALSE'
    p[0] = p[1]

def p_booleanType2(p):
    'booleanType : TRUE'
    p[0] = p[1]



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
    p[0] = p[1]

def p_moreArithmetic2(p):
    'moreArithmetic : arithmetic'
    p[0] = p[1]



#Definition of arithmetic data types
def p_arithmeticDataType1(p):
    'arithmeticDataType : numberType'
    p[0] = p[1]

def p_arithmeticDataType2(p):
    'arithmeticDataType : variable'
    p[0] = p[1]

def p_arithmeticDataType3(p):
    'arithmeticDataType : functionCall'
    p[0] = p[1]



#Definition of arithmetic operators
def p_arithmeticOp1(p):
    'arithmeticOp : SUM'
    p[0] = p[1]

def p_arithmeticOp2(p):
    'arithmeticOp : SUBSTRACTION'
    p[0] = p[1]

def p_arithmeticOp3(p):
    'arithmeticOp : MULTIPLICATION'
    p[0] = p[1]

def p_arithmeticOp4(p):
    'arithmeticOp : DIVISION'
    p[0] = p[1]

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

globalFile.printObject()
