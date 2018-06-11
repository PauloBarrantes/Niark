from parser import *
from ASTStructure import *

'''
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1+list2

print (list3)
print (list2)
print (list1)

'''
listOfLists = []

class decMethod():
    def __init__(self, name, functionDomain, returnType, parameter):
        self.name = name
        self.functionDomain = functionDomain
        self.returnType = returnType
        self.parameter = parameter

class decVar():
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

class decArray(): #En el AST la declaracion de arreglo está como declaración de variable, me parece que vamos a necesitar cambiarlo y usar esto.
    def __init__(self, name, size):
        self.name = name
        self.size = size

def semantic():
    parse()
    niark = getNiarkCode()
    globalScope = []
    listOfLists.insert(0,globalScope)

    for statement in niark.statements:
        recursive(statement, listOfLists)


def recursive(object, listaDeListas):
    if type(object) is Method:
        if not lookup(object.name,listaDeListas):
            name = object.name
            functionDomain = object.functionDomain
            returnType = object.returnType
            parameter = object.parameter
            decMethod1 = decMethod(name, functionDomain, returnType, parameter)
            listaDeListas[0].insert(0,decMethod1)

            newScope = []
            newTable = listaDeListas[:]  #[:] hace que la asignacion sea por copia
            newTable.insert(0, newScope)
            if parameter is not None:
                parameter1 = decVar(object.parameter, 'idk','idk')
                newTable[0].insert(0,parameter1)
            for instruction in object.instructions:
                recursive(instruction, newTable)
        else:
            printError(object.name+ " fue declarado antes")
    elif type(object) is VariableDeclaration:
        if lookup(object.variable.name,listaDeListas):
            printError(object.variable.name + " fue declarada antes")
        else:
            name = object.variable.name
            value = object.variable.value
            type1 = type(value)
            decVar1 = decVar(name, value, type1)
            listaDeListas[0].insert(0,decVar1)
    elif type(object) is VariableAssignation:
        if not lookup(object.name,listaDeListas):
            printError(object.name + " no ha sido declarada" )

    elif type(object) is FunctionCall:
        if object.name == "sqrt":
            print ("jaquemate")
        elif not lookup(object.name,listaDeListas):
            printError(object.name + " no hay nigún método declarado.")
        else:
            recursive(object.parameters, listaDeListas)
    elif type(object) is If:

        newScope = []
        newTable = listaDeListas[:]  #[:] hace que la asignacion sea por copia
        newTable.insert(0, newScope)

        recursive(object.conditions, newTable)
        for instruction in object.instructions:
            recursive(instruction, newTable)# Recursively check internal instructions2
    elif type(object) is IfAndElse:
        newScope1 = []
        newScope2 = []

        newTable1 = listaDeListas[:]  #[:] hace que la asignacion sea por copia
        newTable2 = listaDeListas[:]  #[:] hace que la asignacion sea por copia

        newTable1.insert(0, newScope1)
        newTable2.insert(0, newScope2)

        recursive(object.conditions, newTable1)

        for instruction in object.instructionsIf:
            recursive(instruction, newTable1)
        for instruction in object.instructionsElse:
            recursive(instruction, newTable2)# Recursively check internal instructions3
    elif type(object) is For:
        newScope = []
        newTable = listaDeListas[:]  #[:] hace que la asignacion sea por copia
        newTable.insert(0, newScope)
        recursive(object.declaration, newTable) # Guardamos la declaración del for
        recursive(object.conditions, newTable)
        recursive(object.incdec, newTable)

        for instruction in object.instructions:
            recursive(instruction, newTable)# Recursively check internal instructions4
    elif type(object) is ArrayDeclaration:
        if lookup(object.array.name,listaDeListas):
            printError(object.array.name +" el array ya fue declarado")
        else:
            name = object.array.name
            size = object.array.size

            decArray1 = decArray(name, size)
            listaDeListas[0].insert(0,decArray1)
    elif type(object) is ArrayAssignation:
        if not lookup(object.name,listaDeListas):
            printError(object.name + " no ha sido declarado")

    elif type(object) is Variable:
        if not lookup(object.name,listaDeListas):
            printError(object.name + " no ha sido declarado")

    elif type(object) is Array:
        if not lookup(object.name, listaDeListas):
            printError(object.name + " no ha sido declarado")

    elif type(object) is Arithmetic or type(object) is Condition:
        recursive(object.term1, listaDeListas)
        recursive(object.term2, listaDeListas)

    elif type(object) is Instruction:
        recursive(object.value,listaDeListas)

    elif type(object) is IncDec:
        recursive(object.variable, listaDeListas)
    else:
        print("Es algo raro :o", type(object))

def lookup(name,tableOfSymbols):
    encontrado = False
    for value in tableOfSymbols:
        for value2 in value:
            if value2.name == name:
                encontrado = True

    return encontrado

def printError(error):
    print(bcolors.FAIL+"Error:" +bcolors.ENDC ,bcolors.WARNING + error + bcolors.ENDC)
semantic()

for list in listOfLists:
    for object in list:
        print (object.name)
