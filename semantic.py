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

class decArray(): #En el AST la declaracion de arreglo está como declaración de variable, me parece que vamos a necesitar cambiarlo y usar esto.
    def __init__(self, name, size, values):
        self.name = name
        self.size = size
        self.values = values

def semantic():
    parse()
    niark = getNiarkCode()
    globalScope = []
    listOfList.insert(0,globalScope) #Si listOfLists tiene un elemento globalScope, qué va en los demás espacios? Cada scope es una casilla?

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
#                listOfList.insert(0,globalScope)      //Ya hicimos esto al inicio del método, no hay necesidad de volver a hacerlo
                newList = listOfLists[:]  #[:] hace que la asignacion sea por copia
                recursive(statement, newList)

            else:
                if type(statement) is VariableAssignation:
                    if lookup(statement.name,listOfList):
                        print("Es una asignacion, vamos a asignar el valor\n")
                        #Deberiamos buscar la ubicación de la variable y verificar que el value del statement coincida con el de la variable
                    else:
                        print("Variable ",statement.name, " no ha sido declarada")
                else:
                    if type(statement) is FunctionCall:
                        if lookup(statement.name,listOfList):
                            print("Es un llamado a funcion")
                            globalScope.insert(0,statement)
                        else:
                            print("Metodo ",statement.name," no existe")

def recursive(object, listaDeListas ):

    if type(object) is Method:
        for instruction in object.instructions:
            if type(instruction) is If or type(instruction) is For or type(instruction) is IfAndElse:
                recursive(instruction,list)
            else:
                recursive(instruction,list)
    else:
        '''
        Nota: El recursive lo en teoría debe hacer, es ver que es lo que estamos procesando dependiendo de eso,
        hacemos llamados recursivos, pero de qué?
                    - Hacemos un for que recorra toda las instrucciones (que es una lista de objetos) y le pasamos la actual lista de listas del scope.
        '''
        if type(object) is If:
            # No se necesita lookup
            # Paulo - Si se necesita, hay que recorrer todas las condiciones viendo si hay variables y hacer lookup
            newList = listOfLists[:] #Asignamos copia de la tabla de simbolos
            recursive(statement, newList)# Recursively check internal instructions
            # No entiendo bien como va a funcionar el scope y el recursive
            #no se
        else:
            if type(object) is IfAndElse:
                # No se necesita lookup
                #Paulo- sí se necesita recorrer las condiciones y ver si hay variables no declradas.
                newList = listOfLists[:] #Asignamos copia de la tabla de simbolos
                recursive(statement, newList)# Recursively check internal instructions
                # No entiendo bien como va a funcionar el scope y el recursive
                # Paulo - En el if and else se debe hacer un for para las instrucciones del if y otro para las instrucciones del Else con diferentes tabla de símbolos.

            else:
                if type(object) is For:
                    # No se necesita lookup
                    # Si se necesita para ver si se hace una condición con alguna variable, hay que verificar si esta en el tos
                    newList = listOfLists[:] #Asignamos copia de la tabla de simbolos
                    recursive(statement, newList)# Recursively check internal instructions
                    # No entiendo bien como va a funcionar el scope y el recursive
                else:
                    if type(object) is ArrayDeclaration:
                        if lookup(statement.name,listOfList):
                            print("El arreglo ya fue declarado")
                        else:
                            # Para la construcción del AST nunca creamos objetos ArrayDeclaration, pero deberíamos y mandarle name, size y values.
                    else:
                        if type(object) is ArrayAssignation:
                            if lookup(statement.name,listOfList):
                                print("Es una asignacion de arreglo, vamos a asignar el valor\n")
                                #Deberiamos buscar la ubicación del arreglo y verificar que el value del statement coincida con el de la variable
                            else:
                                print("Arreglo ",statement.name, " no ha sido declarado")
                        else:
                            ## Hay que agregar Variables....

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
