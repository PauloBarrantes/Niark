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

    niark = getNiark()
    dataHeader = ".data \n"
    textHeader = ".text \n"
    mainHeader = "main: \n"
    bitmap.inicializar()
    dataSegment.append(dataHeader)
    textSegment.append(textHeader)
    textSegment.append(mainHeader)
    '''Inicia el algoritmo recursivo de generación de código '''
    for statement in niark.statements:
        print("ggfor")
        recursive(statement)
    exitSyscall()
    generateCode(executable)
    executable.close()



def recursive(object):
    if type(object) is Method:
        pass
    elif type(object) is VariableDeclaration:
        if object.variable.value is not None:
            if type(object.variable.value) is int:
                dataSegment.append(object.variable.name + ": ")
            currentLabel += 1

    elif type(object) is VariableAssignation:
        pass
    elif type(object) is FunctionCall:
        print("gg")
        if object.name == "sqrt":
            reg = diccionarioVarRegs[object.parameters]
            functionCall= "addi  $a0, $zero, 15 \n jal isqrt # v0 = result"
            codeSqrt = "isqrt: \
            # v0 - return / root \
            # t0 - bit \
            # t1 - num \
            # t2,t3 - temps\
            move  $v0, $zero        # initalize return\
            move  $t1, $a0          # move a0 to t1\
            \
            addi  $t0, $zero, 1 \
            sll   $t0, $t0, 30      # shift to second-to-top bit\
            \
            isqrt_bit: \
            slt   $t2, $t1, $t0     # num < bit\
            beq   $t2, $zero, isqrt_loop\
            \
            srl   $t0, $t0, 2       # bit >> 2\
            j     isqrt_bit \
            \
            isqrt_loop: \
            beq   $t0, $zero, isqrt_return\
            \
            add   $t3, $v0, $t0     # t3 = return + bit\
            slt   $t2, $t1, $t3 \
            beq   $t2, $zero, isqrt_else\
            \
            srl   $v0, $v0, 1       # return >> 1\
            j     isqrt_loop_end\
            \
            isqrt_else:\
            sub   $t1, $t1, $t3     # num -= return + bit\
            srl   $v0, $v0, 1       # return >> 1\
            add   $v0, $v0, $t0     # return + bit\
            \
            isqrt_loop_end:\
            srl   $t0, $t0, 2       # bit >> 2\
            j     isqrt_loop\
            \
            isqrt_return:\
            jr  $ra"
            textSegment.append(codeSqrt)
            mainHeader.append(functionCall)
        elif True:
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