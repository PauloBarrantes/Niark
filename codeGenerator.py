from BitMap import *
from semantic import *

## Variables de Generación de Código
executable = open("CompiledCode.asm", "w+")
error = getSemanticError()
dataSegment = []
textSegment = []
mainLabel = []
bitmap =  BitMap()
print(error)

def codeGenerator():
    if error == False:
        semantic()
        niark = getNiark()
        dataHeader = ".data \n"
        textHeader = ".text \n"
        mainHeader = "main: \n"
        bitmap.inicializar()
        dataSegment.append(dataHeader)
        textSegment.append(textHeader)
        textSegment.append(mainHeader)
        exitSyscall()
        '''Inicia el algoritmo recursivo de generación de código '''

        '''for statement in niark.statements:
          recursive(statement, listOfLists)
          '''
        generateCode(executable)
        executable.close()
    else:
        print("Please fix errors so we can create an executable.")


def recursive(object, listaDeListas):
    if type(object) is Method:
        pass
    elif type(object) is VariableDeclaration:
        pass
    elif type(object) is VariableAssignation:
        pass
    elif type(object) is FunctionCall:
        pass
    elif type(object) is If:
        pass
    elif type(object) is IfAndElse:
        pass
    elif type(object) is For:
        pass
    elif type(object) is ArrayDeclaration:
        pass
    elif type(object) is ArrayAssignation:
        pass
    elif type(object) is Variable:
        pass
    elif type(object) is Array:
        pass
    elif type(object) is Arithmetic:
        pass
    elif type(object) is Condition:
        pass
    elif type(object) is Instruction:
        pass
    elif type(object) is IncDec:
        regName = obtener()
        textSegment.append("li ", regName, ", ", object.variable.value)
        if(object.operator == "++"):
            textSegment.append("addi ", regName, ", ", "1")
        else:
            textSegment.append("addi ", regName, ", ", "-1")
    
    else:
        print("Es un literal", type(object))

def printIntSyscall(arg):
    printIntSyscall = "li $v0, 1 \n"
    textSegment.append(printIntSyscall)
    syscall()

def printStringSyscall(arg):
    printStringSyscall = "li $v0, 4 \n"
    textSegment.append(printStringSyscall)
    syscall()

def readIntSyscall(arg):
    readIntSyscall = "li $v0, 5 \n"
    textSegment.append(readIntSyscall)
    syscall()

def readStringSyscall(arg):
    readStringSyscall = "li $v0, 8 \n"
    textSegment.append(readStringSyscall)
    syscall()

def exitSyscall():
    exitSyscall = "li $v0, 10 \n"
    textSegment.append(exitSyscall)
    syscall()

def syscall():
    syscall = "syscall \n"
    textSegment.append(syscall)

def generateCode(file):
    for line in dataSegment:
        file.write(line)
    for code in textSegment:
        file.write(code)


codeGenerator()