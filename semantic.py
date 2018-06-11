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
    def __init__(self, name, size, values):
        self.name = name
        self.size = size
        self.values = values

def semantic():
    parse()
    niark = getNiarkCode()
    globalScope = [];
    listOfLists.insert(0,globalScope)

    for statement in niark.statements:
        recursive(statement, listOfLists)


def recursive(object, listaDeListas):

    if type(object) is Method:
        name = object.name
        functionDomain = object.functionDomain
        returnType = object.returnType
        parameter = object.parameter
        decMethod1 = decMethod(name, functionDomain, returnType, parameter)
        listaDeListas[0].insert(0,decMethod1)
        print (object.name)

        newList = listOfLists[:]  #[:] hace que la asignacion sea por copia

        for instruction in object.instructions:
            recursive(instruction, newList)
    else:
        if type(object) is VariableDeclaration:
            if lookup(object.variable.name,listaDeListas):
                print("Variable ya declarada antes")
            else:
                print("Es una declaración  de variable")
                name = object.variable.name
                value = object.variable.value
                type1 = type(value)
                decVar1 = decVar(name, value, type1)
                listaDeListas[0].insert(0,decVar1)
        else:
            if type(object) is VariableAssignation:
                if lookup(object.name,listaDeListas):
                    print("Es una asignacion, vamos a asignar el valor\n")
                    #Deberiamos buscar la ubicación de la variable y verificar que el value del object coincida con el de la variable
                else:
                    print("Variable ",object.name, " no ha sido declarada")
            else:
                if type(object) is FunctionCall:
                    if lookup(object.name,listaDeListas):
                        print("Es un llamado a funcion")
                        # Hay que buscar la ubicación del método y verificar que los parametros coincidan con los declarados
                    else:
                        print("Metodo ",object.name," no existe")
                else:
                    if type(object) is If:
                        newList = listOfLists[:] #Asignamos copia de la tabla de simbolos
                        for instruction in object.instructions:
                            recursive(instruction, newList)# Recursively check internal instructions
                    else:
                        if type(object) is IfAndElse:
                            newList = listOfLists[:] #Asignamos copia de la tabla de simbolos
                            for instruction in object.instructionsIf:
                                recursive(instruction, newList)
                            for instruction in object.instructionsElse:
                                recursive(instruction, newList)# Recursively check internal instructions
                        else:
                            if type(object) is For:
                                for instruction in object.instructions:
                                    recursive(instruction, newList)# Recursively check internal instructions
                            else:
                                if type(object) is ArrayDeclaration:
                                    if lookup(object.name,listaDeListas):
                                        print("El arreglo ya fue declarado")
                                    else:
                                        pass
                                        # Para la construcción del AST nunca creamos objetos ArrayDeclaration, pero deberíamos y mandarle name, size y values.
                                else:
                                    if type(object) is ArrayAssignation:
                                        if lookup(object.name,listaDeListas):
                                            print("Es una asignacion de arreglo, vamos a asignar el valor\n")
                                            #Deberiamos buscar la ubicación del arreglo y verificar que el value del statement coincida con el de la variable
                                        else:
                                            print("Arreglo ",object.name, " no ha sido declarado")
    #listOfLists.insert(0,listaDeListas)


def lookup(name,tableOfSymbols):
    encontrado = False
    for value in tableOfSymbols:
        for value2 in value:
            if value2.name == name:
                encontrado = True

    return encontrado


semantic()

for list in listOfLists:
    for object in list:
        print (object.name)
