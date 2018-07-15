from BitMap import *
from semantic import *

## Variables de Generación de Código
executable = open("CompiledCode.asm", "w+")
dataSegment = []
textSegment = []
mainLabel = []
diccionarioVarRegs = {}
currentLabel = 1
bitmap =  BitMap()

def codeGenerator():
    semantic()
    print(type(2))
    niark = getNiark()
    dataHeader = ".data \n"
    textHeader = ".text \n"
    mainHeader = "main: \n"
    bitmap.inicializar()
    dataSegment.append(dataHeader)
    textSegment.append(textHeader)
    textSegment.append(mainHeader)
    '''Inicia el algoritmo recursivo de generación de código '''

    '''for statement in niark.statements:
        recursive(statement)
      '''
    exitSyscall()
    generateCode(executable)
    executable.close()



def recursive(object):
    if type(object) is Method:
        pass
    elif type(object) is VariableDeclaration:
        if object.variable.value is not None:
            if type(object.variable.value) is int
                dataSegment.append(object.variable.name + ": ")
            currentLabel += 1

    elif type(object) is VariableAssignation:
        pass
    elif type(object) is FunctionCall:
        if object.name == "sqrt":
            reg = diccionarioVarRegs[object.parameters]
            code= "addi  $a0, $zero, 15 jal   isqrt # v0 = result"
        elif:
            pass
    elif type(object) is If:
        regName1 = recursive(object.conditions.term1)
        regName2 = recursive(object.conditions.term2)

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
                printIntSyscall(object.value)
            else:
                printStringSyscall(object.value)

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