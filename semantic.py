from parser import *
from ASTStructure import *
from tableOfSymbols import *

'''
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1+list2

print (list3)
print (list2)
print (list1)

'''
tos =  TableOfSymbols()
listOflist = []

class decMethod():
    def __init__(self, name, functionDomain, returnType):
        self.name = name
        self.functionDomain = functionDomain
        self.returnType = returnType
    def parameters(arg):
        pass
class decVar():
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.value = type

def semantic():
    parse()
    niark = getNiarkCode()
    niark.printObject('')
    globalScope = []
    listOflist.insert(0,globalScope)

    for statement in niark.statements:
        if type(statement) is VariableDeclaration:
            print("Es una declaración  de variable")
            name = statement.variable.name
            value = statement.variable.value
            type1 = type(value)
            decVar1 = decVar(name, value, type1)
            globalScope.insert(0,decVar1)
        else:
            if type(statement) is Method:
                newLista = listOflist.insert(0,globalScope)
                recursive(statement, newLista)
            else:
                print ("gg")
def recursive(object, listaDeListas ):

    if type(object) is Method:
        for instrucction in object.instrucctions:
            if type(instrucction) is If or type(instrucction) is For:
                recursive(instruction,list)
            else:
                recursive(instruction)

def lookup(tableOfSymbols):
    pass

semantic()

for value in listOflist:
    for value2 in value:
        print (value2.name)
