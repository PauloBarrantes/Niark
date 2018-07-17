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
            q += 1

    textSegment.append("li $v0, 10\n")
    textSegment.append("syscall\n")
    generateCode(executable)
    executable.close()



def recursive(object,label):
    if type(object) is VariableDeclaration:
        if type(object.variable.value) is Variable:
            regName = bitmap.obtener()
            dictionaryVarReg[object.variable.name] = regName
            regValue = dictionaryVarReg[object.variable.value.name]
            textSegment.append("lw " + regName + ", " + regValue + "\n")

        else:
            regName = bitmap.obtener()
            textSegment.append("li " + regName + ", " + str(object.variable.value) + "\n")
            dictionaryVarReg[object.variable.name] = regName

    elif type(object) is VariableAssignation:
        pass

    elif type(object) is ArrayDeclaration:
        dataSegment.append(object.array.name + ": .word 0:50\n")

        regName = bitmap.obtener()
        textSegment.append("la " + regName + ", " + object.array.name + "\n")

        dictionaryVarReg[object.array.name] = regName

    elif type(object) is ArrayAssignation:
        regValue = bitmap.obtener()
        regPos4 = bitmap.obtener()
        if object.value is "True":
            textSegment.append("li " + regValue + ", 1\n")
        else:
            textSegment.append("li " + regValue + ", 0\n")

        regName = dictionaryVarReg[object.name]

        if type(object.index) is Arithmetic:
            recursive(object.index,label)
            textSegment.append(
                "mul " + regPos4 + ", $t9, 4" + "\n")
        else:
            regPos = dictionaryVarReg[object.index.name]
            textSegment.append(
                "mul " + regPos4 + ", " + regPos + ", 4" + "\n")

        textSegment.append(
            "add " + regPos4 + ", " + regPos4 + ", " + regName + "\n")
        textSegment.append("sw " + regValue + ", (" + regPos4 + ")\n")
        bitmap.liberar(regPos4)
        bitmap.liberar(regValue)

    elif type(object) is Arithmetic:
        if object.term1 is 0:
            textSegment.append("li $t9, -" + str(object.term2) + "\n")
        elif object.operator is "+":
            if type(object.term1) is FunctionCall:
                recursive(object.term1)
                regTerm1 = bitmap.obtener()
                textSegment.append("lw " + regTerm1 + ", $v0\n")

                recursive(object.term2,label)
                textSegment.append("add $t9, " + regTerm1 + ", $v0\n")

                bitmap.liberar(regTerm1)
            else:
                regTerm1 = dictionaryVarReg[object.term1.name]
                regTerm2 = dictionaryVarReg[object.term2.name]
                textSegment.append("add $t9, " + regTerm1 + ", " + regTerm2 + "\n")

        elif object.operator is "-":
            regTerm1 = dictionaryVarReg[object.term1]
            textSegment.append("addi $t9, " + regTerm1 + ", -" + object.term2 + "\n")
        elif object.operator is "/":
            regTerm1 = dictionaryVarReg[object.term1.name]
            regTerm2 = dictionaryVarReg[object.term2.name]
            textSegment.append("div " + regTerm1 + ", " + regTerm2 + "\n")
            textSegment.append("mflo $t9\n")

    elif type(object) is Condition:
        if object.operator is "<=":
            recursive(object.term2,label)

            regTerm1 = dictionaryVarReg[object.term1.name]
            regResult = bitmap.obtener()

            textSegment.append("bne " + regTerm1 + ", $t9, " + label + "\n")
            textSegment.append("slt " + regResult + ", " + regTerm1 + ", $t9\n")
            textSegment.append("beq " + regResult + ", $0, " + label + "\n")

            bitmap.liberar(regResult)

        elif object.operator is "<":
            if type(object.term2) is FunctionCall:
                recursive(object.term2)
                regTerm1 = dictionaryVarReg[object.term1.name]
                regResult = bitmap.obtener()

                textSegment.append("slt " + regResult + ", " + regTerm1 + ", $v0\n")
                textSegment.append("beq " + regResult + ", $0, " + label + "\n")

                bitmap.liberar(regResult)

            elif type(object.term2) is Arithmetic:
                recursive(object.term2)

                regTerm1 = dictionaryVarReg[object.term1.name]
                regResult = bitmap.obtener()

                textSegment.append("slt " + regResult + ", " + regTerm1 + ", $t9\n")
                textSegment.append("beq " + regResult + ", $0, " + dir + "\n")

                bitmap.liberar(regResult)

            else:
                regTerm1 = dictionaryVarReg[object.term1.name]
                regTerm2 = dictionaryVarReg[object.term2.name]
                regResult = bitmap.obtener()

                textSegment.append("slt " + regResult + ", " + regTerm1 + ", " + regTerm2 + "\n")
                textSegment.append("beq " + regResult + ", $0, " + dir + "\n")

                bitmap.liberar(regResult)

        elif object.operator is ">":
            regTerm1 = dictionaryVarReg[object.term1.name]
            regTerm2 = bitmap.obtener()
            regResult = bitmap.obtener()

            textSegment.append("li " + regTerm2 + ", " + str(object.term2) + "\n")
            textSegment.append("slt " + regResult + ", " + regTerm2 + ", " + regTerm1 + "\n")
            textSegment.append("beq " + regResult + ", $0, " + dir + "\n")

            bitmap.liberar(regResult)

        else:
            if type(object.term1) is Array:
                regTerm1 = dictionaryVarReg[object.term1.name]
                regPos = dictionaryVarReg[object.term1.size.name]
                regPos4 = bitmap.obtener()
                regValue = bitmap.obtener()

                textSegment.append("mul " + regPos4 + ", " + regPos + ", 4" + "\n")
                textSegment.append("add " + regPos4 + ", " + regPos4 + ", " + regTerm1 + "\n")
                textSegment.append("lw " + regValue + ", (" + regPos4 + ")\n")
                textSegment.append("bgtz " + regValue + ", " + label + "\n")

                bitmap.liberar(regPos4)
                bitmap.liberar(regValue)

            else:
                regTerm1 = dictionaryVarReg[object.term1.name]
                regTerm2 = bitmap.obtener()

                textSegment.append("li " + regTerm2 + ", " + str(object.term2) + "\n")
                textSegment.append("bne " + regTerm1 + ", " + regTerm2 + "," + dir + "\n")
                bitmap.liberar(regTerm2)

    elif type(object) is Instruction:
        if object.id == 'READ':
            if type(object.value) is int:
                textSegment.append("li $v0, 5\n")
                textSegment.append("syscall\n")
            else:
                textSegment.append("li $v0, 8\n")
                textSegment.append("syscall\n")
        elif object.id == 'PRINT':
            if type(object.value) is int:
                textSegment.append("li $v0, 1\n" + "li $a0," + str(arg) + "\n")
            else:
                pass #Hay que tener un codigo
        else:
            if type(object.value) is Arithmetic:
                recursive(object.value)
                textSegment.append("li $v0, $t9\n")
            elif type(object.value) is Variable:
                textSegment.append("la $v0, " + str(object.value.name) + "\n")
            else:
                textSegment.append("li $v0, " + str(object.value) + "\n")

    elif type(object) is IncDec:
        regName = dictionaryVarReg[object.variable.name]
        if (object.operator == "++"):
            textSegment.append("addi " + regName + ", " + regName + ", 1\n")
        else:
            textSegment.append("addi " + regName + ", " + regName + ", -1\n")

    elif type(object) is FunctionCall:
        if type(object.parameters) is Arithmetic:
            recursive(object.parameters)
            textSegment.append("sw $t9, ($sp)\n")
        elif type(object.parameters) is int:
            regValue = bitmap.obtener()
            textSegment.append("li " + regValue + ", " + str(object.parameters) + "\n")
            textSegment.append("sw " + regValue + ", ($sp)\n")
            bitmap.liberar(regValue)
        else:
            pass

        textSegment.append("addiu $sp, $sp, -8\n")
        textSegment.append("jal " + label + "\n")

    elif type(object) is If:
        recursive(object.conditions,"Continuation" + label)

        for instruction in object.instructions:
            recursive(instruction,label + instruction.id)


        textSegment.append("Continuation" + label + ":\n")

    elif type(object) is IfAndElse:
        recursive(object.conditions, "Else" + label)

        for instruction in object.instructionsIf:
            recursive(instruction, label + instruction.id)
        textSegment.append("j Continuation" + label + "\n")

        textSegment.append("Else" + label + ":\n")

        for instruction in object.instructionsElse:
            recursive(instruction, label + instruction.id)

        textSegment.append("Continuation" + label + ":\n")

    elif type(object) is For:
        recursive(object.declaration, label + object.declaration.id)
        textSegment.append("Loop" + label + ":\n")

        recursive(object.conditions, "ExitLoop" + label)
        for instruction in object.instructions:
            recursive(instruction, label + instruction.id)

        recursive(object.incdec)
        textSegment.append("j Loop" + label + "\n")
        textSegment.append("ExitLoop" + label + ":\n")

    elif type(object) is Method:
        textSegment.append(label + ":\n")
        textSegment.append("sw $ra, 4($sp)\n")

        dictionaryVarReg[object.parameter.name] = "4($sp)"
        for instruction in object.instructions:
            recursive(instruction, label + instruction.id)

        textSegment.append("sw $ra, 4($sp)\n")
        textSegment.append("addiu $sp, $sp, 8\n")
        textSegment.append("jr $ra\n")


    else:
        print("Es un literal", type(object))





def generateCode(file):
    for line in dataSegment:
        file.write(line)
    for code in textSegment:
        file.write(code)



codeGenerator()