from BitMap import *
from semantic import *

## Variables de Generación de Código
executable = open("CompiledCode.asm", "w+")
dataSegment = []
textSegment = []
mainLabel = []
dictionaryVarReg = {}
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
    q = 0
    '''Inicia el algoritmo recursivo de generación de código '''
    for statement in niark.statements:
        if type(statement) == FunctionCall or type(statement) == Method:
            recursive(statement.statement.name)
        else:
            recursive(statement,str(q))
            ++q

    exitSyscall()
    generateCode(executable)
    executable.close()



def recursive(object,label):
    if type(object) is Method:
        pass
    elif type(object) is VariableDeclaration:
        regName = bitmap.obtener()
        textSegment.append("li " + regName + ", " + str(object.variable.value) + "\n")
        dictionaryVarReg[object.variable.name] = regName

    elif type(object) is VariableAssignation:
        pass

    elif type(object) is ArrayDeclaration:
        dataSegment.append(object.array.name + ": .word 0:50\n")

        regName = bitmap.obtener()
        textSegment.append("la "+ regName + ", " + object.array.name + "\n")

        dictionaryVarReg[object.array.name] = regName

    elif type(object) is ArrayAssignation:
        regName = dictionaryVarReg[object.name] #El registro que contiene la direccion del vector
        regPos = dictionaryVarReg[object.index.name] #Registro que contiene el valor del indice
        regPos4 = bitmap.obtener() #Registro libre que vamos a utilizar para apuntar a la direccion de memoria del indice
        regValue = bitmap.obtener() #Registro que va a guardar el valor que vamos a asignar

        value = 0;
        if object.value is "True":
            value = 1

        textSegment.append("li " + regValue + ", " + str(value) + "\n")
        textSegment.append("mul " + regPos4 + ", " + regPos + ", 4" + "\n") #Como son words lo que guarda el vector hay que multiplicar el indice por 4, el resultao e guarda en regPos4
        textSegment.append("add " + regPos4 + ", " + regPos4 + ", " + regName + "\n") #Guadamos en regPos4 la pos inicial del vector + el inidice
        textSegment.append("sw " + regValue + ", (" + regPos4 + ")\n") #Guardamos valor en la direccion del vector
        bitmap.liberar(regPos4)
        bitmap.liberar(regValue)

    elif type(object) is FunctionCall:
        print("gg")
        if object.name == "sqrt":
            reg = dictionaryVarReg[object.parameters]
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
        conditionCode(object.conditions,label + "Continuation")

        for instruction in object.instructions:
            recursive(instruction,instruction.id)


        textSegment.append(label + "Continuation:")
    elif type(object) is IfAndElse:
        pass

    elif type(object) is For:
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
        textSegment.append("li " + regName + ", " + object.variable.value)
        if(object.operator == "++"):
            textSegment.append("addi " + regName + ", " + "1")
        else:
            textSegment.append("addi " + regName + ", " + "-1")
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

def arithmeticCode(object):
    if object.term1 is 0:
        textSegment.append("li $t9, " + str(object.term2) + "\n")
    elif object.operator is "+":
        regTerm1 = dictionaryVarReg[object.term1]
        regTerm2 = dictionaryVarReg[object.term2]
        textSegment.append("add $t9, " + regTerm1 + ", " + regTerm2 + "\n")
    elif object.operator is "-":
        regTerm1 = dictionaryVarReg[object.term1]
        textSegment.append("addi $t9, " + regTerm1 + ", -" + object.term2 + "\n")
    elif object.operator is "/":
        regTerm1 = dictionaryVarReg[object.term1]
        regTerm2 = dictionaryVarReg[object.term2]
        textSegment.append("div " + regTerm1 + ", " + regTerm2 + "\n")
        textSegment.append("mflo $t9\n")

def conditionCode(object,dir):
    if object.operator is "<=":
        arithmeticCode(object.term2)

        regTerm1 = dictionaryVarReg[object.term1.name]
        regResult = bitmap.obtener()

        textSegment.append("bne " + regTerm1 + ", $t9, " + dir + "\n")
        textSegment.append("slt " + regResult + ", " + regTerm1 + ", $t9\n")
        textSegment.append("beq " + regResult + ", $0, " + dir + "\n")

        bitmap.liberar(regResult)

    elif object.operator is "<":
        if type(object.term2) is FunctionCall:
            textSegment.append("jal " + object.term2.name + "\n")
            regTerm1 = dictionaryVarReg[object.term1.name]
            regResult = bitmap.obtener()

            textSegment.append("slt " + regResult + ", " + regTerm1 + ", $v0\n")
            textSegment.append("beq " + regResult + ", $0, " + dir + "\n")

            bitmap.liberar(regResult)

        elif type(object.term2) is Arithmetic:
            arithmeticCode(object.term2)

            regTerm1 = dictionaryVarReg[object.term1.name]
            regResult = bitmap.obtener()

            textSegment.append("slt " + regResult + ", " + regTerm1 + ", $t9\n")
            textSegment.append("beq " + regResult + ", $0, " + dir + "\n")

            bitmap.liberar(regResult)

    elif object.operator is ">":
        regTerm1 = dictionaryVarReg[object.term1.name]
        regTerm2 = bitmap.obtener()
        regResult = bitmap.obtener()

        textSegment.append("li " + regTerm2 + ", " + object.term2 + "\n")
        textSegment.append("slt " + regResult + ", " + regTerm2 + ", " + regTerm1 + "\n")
        textSegment.append("beq " + regResult + ", $0, " + dir + "\n")

        bitmap.liberar(regResult)

    elif object.operator is "==":
        if type(object.term1) is Array:
            regTerm1 = dictionaryVarReg[object.term1.name]
            regPos = dictionaryVarReg[object.term1.size]
            regPos4 = bitmap.obtener()
            regValue = bitmap.obtener()

            textSegment.append("mul " + regPos4 + ", " + regPos + ", 4" + "\n")
            textSegment.append("add " + regPos4 + ", " + regPos4 + ", " + regTerm1 + "\n")
            textSegment.append("lw " + regValue + ", (" + regPos4 + ")\n")
            textSegment.append("bgtz " + regValue + ", " + dir + "\n")

            bitmap.liberar(regPos4)

        else:
            regTerm1 = dictionaryVarReg[object.term1.name]
            regTerm2 = bitmap.obtener()

            textSegment.append("li " + regTerm2 + "," + str(object.term2) + "\n")
            textSegment.append("bne " + regTerm1 + "," + regTerm2 + "," + dir + "\n")
            bitmap.liberar(regTerm2)

codeGenerator()