from BitMap import *
from semantic import *

## Variables de Generación de Código
executable = open("CompiledCode.asm", "w+")
dataSegment = []
textSegment = []
mainLabel = []
currentLabel = 1
bitmap =  BitMap()

def codeGenerator():
    semantic()
    niark = getNiark()
    dataHeader = ".data \n"
    textHeader = ".text \n"
    mainHeader = "main: \n"
    bitmap.inicializar()
    dataSegment.append(dataHeader)
    textSegment.append(textHeader)
    textSegment.append(mainHeader)
    syscall()
    exitSyscall()
    '''Inicia el algoritmo recursivo de generación de código '''

    '''for statement in niark.statements:
        recursive(statement, listOfLists)
      '''
    generateCode(executable)
    executable.close()



def recursive(object, listaDeListas):
    if type(object) is Method:
        pass
    elif type(object) is VariableDeclaration:
        #Libera despues
        pass
    elif type(object) is VariableAssignation:
        pass
    elif type(object) is FunctionCall:
        pass
    elif type(object) is If:
        regName1 = bitmap.obtener()
        regName2 = bitmap.obtener()

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
        if object.id == 'READ':
            if type(object.value) is int:
                readIntSyscall()
            else:
                readStringSyscall()
        elif object.id == 'PRINT':
            if type(object.value) is int:
                printIntSyscall()
            else:
                printStringSyscall()

    elif type(object) is IncDec:
        regName = bitmap.obtener()
        textSegment.append("li ", regName, ", ", object.variable.value)
        if(object.operator == "++"):
            textSegment.append("addi ", regName, ", ", "1")
        else:
            textSegment.append("addi ", regName, ", ", "-1")
        bitmap.liberar(regName)

    else:
        print("Es un literal", type(object))

def printIntSyscall(arg):
    printIntSyscall = "li $v0, 1 \n"
    textSegment.append(str(printIntSyscall) + "li $a0," + str(arg) + "\n")
    syscall()

def printStringSyscall(arg):
    printStringSyscall = "li $v0, 4 \n"
    textSegment.append(str(printStringSyscall) + "li $a0," + str(arg) + "\n")
    syscall()

def readIntSyscall():
    readIntSyscall = "li $v0, 5 \n"
    textSegment.append(readIntSyscall)
    syscall()

def readStringSyscall():
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

def printLabel():
    file.write(currentLabel,":")
    currentLabel += 1

def generateCode(file):
    for line in dataSegment:
        file.write(line)
    for code in textSegment:
        file.write(code)


codeGenerator()