class File:
    def __init__(self):
        self.instructions = []
        self.variables = dict()

    def addInstruction(self,instruction):
        print('Adding instruction')
        self.instructions.append(instruction)

    def print(self):
        print('Amount of instruction: ',len(self.instructions))
        for x in range (len(self.instructions)):
            self.instructions[x].print()



class Function:
    functionDomain = False
    returnType = False
    name = ''
    def __init__(self, functionDomain, returnType, name, parameters):
        self.functionDomain = functionDomain
        self.returnType = returnType
        self.name = name
        self.parameters = parameters
        self.instructionList = []
        self.variables = dict()

    def addVariable(self, variable):
        self.variables = {variable.name, variable}

    def eliminateVariable(self, name):
        del self.variables[name]

    def modifyValue(self, name, value):
        self.variables[name] = value

    def print(self):
        print("Soy una funcion")
        for x in range (0, len(self.instructionList)):
            self.instructionList[x]



class Variable:
    id = "VARIABLE"
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.id)

class VectorVariable:
    id = "VECTOR VARIABLE"

    def __init__(self, name,pos):
        self.name = name
        self.pos = pos

    def print(self):
        print(self.id)



class EmptyVariableDeclaration:
    id = 'EMPTY DECLARATION'
    def __init__(self, name):
        self.name = name[1:]

    def print(self):
        print(self.id)

class VariableDeclaration:
    id = 'VARIABLE DECLARATION'
    def __init__(self, name,value):
        self.name = name[1:]
        self.value = value

    def print(self):
        print(self.id)

class VectorDeclaration:
    id = 'VECTOR DECLARATION'
    def __init__(self, name,size):
        self.name = name[1:]
        self.size = size

    def print(self):
        print(self.id)



class For:
    id = 'FOR'
    def __init__(self):
        self.conditions = []
        self.arithmethicOperations = []
        self.localVariables = {}
        self.instructionList = []


    def print(self):
        print(id)
        for x in range (0, len(self.instructionList)):
            print(self.instructionList[x].print())



class If:
    id = 'IF'
    def __init__(self, conditions):
        self.conditions = conditions
        self.logicalOperators = []
        self.localVariables = {}
        self.instructionList = []
    def print(self):
        print(id)
        for x in range (0, len(self.instructionList)):
            print(self.instructionList[x].print())



class Else:
    id = 'ELSE'
    def __init__(self):
        self.localVariables = {}
        self.instructionList = []

    def print(self):
        print(id)
        for x in range (0, len(self.instructionList)):
            print(self.instructionList[x])



class ElseIf:
    id = 'ELSEIF'

    def __init__(self, conditions):
        self.localVariables = {}
        self.instructionList = []

    def print(self):
        print(id)
        for x in range (0, len(self.instructionList)):
            print(self.instructionList[x].print())



class Condition:
    def __init__(self, term1, operator, term2):
        self.term1 = term1
        self.term2 = term2
        self.operator = operator

    def print(self):
        print(self.term1, self.term2, self.operator)



class FunctionCall:
    id = 'CALL'
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

    def print(self):
        print(id)



class VariableAssignation:
    id = 'VARIABLE ASSIGNATION'
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def print(self):
        print(self.id)

class VectorAssignation:
    id = 'VECTOR ASSIGNATION'
    def __init__(self, name, cellNumber, value):
        self.name = name
        self.cellNumber = cellNumber
        self.value = value
    def print(self):
        print(self.id)



class Instructions:
    def __init__(self, parameters, id):
        self.parameters = parameters
        self.id = id
    def print(self):
        print (id)



class Array:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def addType(self, type):
        self.type = type

    def addValue(self, value):
        self.value = value

    def print(self):
        print(self.name, self.size)



class ArrayAssignation:
    def __init__(self, name, index, value):
        self.name = name
        self.index = index
        self.value = value

    def print (self) :
        print(self.name, self.index, self.value)