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
listOfList = []

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

def semantic():
    parse()
    niark = getNiarkCode()
    globalScope = []
    listOfList.insert(0,globalScope)

    for statement in niark.statements:
        if type(statement) is VariableDeclaration:
            if lookup(statement.variable.name,listOfList):
                print("Variable ya declarada antes")
            else:
                print("Es una declaración  de variable")
                name = statement.variable.name
                value = statement.variable.value
                type1 = type(value)
                decVar1 = decVar(name, value, type1)
                globalScope.insert(0,decVar1)
        else:
            if type(statement) is Method:
                name = statement.name
                functionDomain = statement.functionDomain
                returnType = statement.returnType
                parameter = statement.parameter
                decMethod1 = decMethod(name, functionDomain, returnType, parameter)
                globalScope.insert(0,decMethod1)
                print (statement.name)
                newLista = listOfList.insert(0,globalScope)
                recursive(statement, newLista)

            else:
                if type(statement) is VariableAssignation:
                    if lookup(statement.name,listOfList):
                        pass
                else:
                    if type(statement) is FunctionCall:
                        if lookup(statement.name,listOfList):
                            pass

def recursive(object, listaDeListas ):

    if type(object) is Method:
        for instrucction in object.instructions:
            if type(instrucction) is If or type(instrucction) is For:
                recursive(instrucction,list)
            else:
                recursive(instrucction,list)
    if type(object) is Variable:
        pass
    if type(object) is For:
        pass

    if type(object) is If:
        pass

    if type(object) is IfAndElse:
        pass

    if type(object) is VariableAssignation:
        pass

    if type(object) is VariableDeclaration:
        pass

    if type(object) is ArrayAssignation:
        pass

    if type(object) is ArrayDeclaration:
        pass

    if type(object) is FunctionCall:
        pass

    if type(object) is ArrayDeclaration:
        pass

def lookup(name,tableOfSymbols):
    encontrado = False
    for value in tableOfSymbols:
        for value2 in value:
            if value2.name == name:
                encontrado = True

    return encontrado


semantic()

for list in listOfList:
    for object in list:
        print (object.name)
