class File:
    def __init__(self):
        self.functions = []
        self.variables = dict()
        self.instructionList = []

    def addFunction(self, function):
        self.functions.append(function)

    def addInstruction(self, instruction):
        self.functions.append(instruction)

    def addVariable(self, variable):
        self.variables = {variable.name, variable}

    def eliminateVariable(self, name):
        del self.variables[name]

    def modifyValue(self, name, value):
        self.variables[name] = value

    def printObject(self):
        print("Soy un archivo")
        for i in range (0, len(self.functions)):
            if(self.functions[i] is not None):
                self.functions[i].printObject()
        for x in range (0, len(self.instructionList)):
            if(self.instructionList[x] is not None):
                self.instructionList[x].printObject()

class Function:
    functionDomain = False
    returnType = False
    name = ''
    def __init__(self, functionDomain, returnType, name, parameters, instructions):
        self.functionDomain = functionDomain
        self.returnType = returnType
        self.name = name
        self.parameters = parameters
        self.instructionList = instructions
        self.variables = dict()
        print("Crea funcion")

    def addVariable(self, variable):
        self.variables = {variable.name, variable}

    def eliminateVariable(self, name):
        del self.variables[name]

    def modifyValue(self, name, value):
        self.variables[name] = value

    def printObject(self):
        print("Soy una funcion")
        if(self.instructionList is not None):
            for x in range (0, len(self.instructionList)):
                if(self.instructionList[x] is not None):
                    self.instructionList[x].printObject()

class Variable:
    type = "unknown"
    def __init__(self, name):
        self.name = name

    def addType(self, type):
        self.type = type

    def addValue(self, value):
        self.value = value

    def printObject(self):
        print(self.name, self.type, self.value)

class VariableDeclaration:
    id = 'DECLARATION'
    def __init__(self, variable):
        self.name = "declaracion"
        self.variable = variable

    def addValue(self, value):
        self.variable.value = value

    def printObject(self):
        print(id)

class For:
    id = 'FOR'
    def __init__(self, counterVariable, conditions, incdec, instructions):
        self.conditions = conditions
        self.arithmethicOperations = []
        self.localVariables = {}
        self.instructionList = [incdec]
        self.instructionList.extend(instructions)


    def printObject(self):
        print(id)
        for x in range (0, len(self.instructionList)):
            print(self.instructionList[x].printObject())

class While:
    id = 'WHILE'
    def __init__(self, conditions, instructions):
        self.conditions = conditions
        self.logicalOperators = []
        self.localVariables = {}
        self.instructionList = instructions

    def printObject(self):
        print(id)
        for x in range (0, len(self.instructionList)):
            self.instructionList[x].printObject()

class If:
    id = 'IF'
    def __init__(self, conditions, instructions):
        self.conditions = conditions
        self.logicalOperators = []
        self.localVariables = {}
        self.instructionList = instructions
    def printObject(self):
        print(id)
        for x in range (0, len(self.instructionList)):
            self.instructionList[x].printObject()

class Else:
    id = 'ELSE'
    def __init__(self,instructions):
        self.localVariables = {}
        self.instructionList = instructions

    def printObject(self):
        print(id)
        for x in range (0, len(self.instructionList)):
            print(self.instructionList[x])

class ElseIf:
    id = 'ELSEIF'

    def __init__(self, conditions):
        self.localVariables = {}
        self.instructionList = []

    def printObject(self):
        print(id)
        for x in range (0, len(self.instructionList)):
            print(self.instructionList[x].printObject())

class Condition:
    def __init__(self, term1, operator, term2):
        self.term1 = term1
        self.term2 = term2
        self.operator = operator

    def printObject(self):
        print(self.term1, self.term2, self.operator)

class FunctionCall:
    id = 'CALL'
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

    def printObject(self):
        print(id)

class VariableAssignation:
    id = 'ASSIGNATION'
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def printObject(self):
        print(id)

class Instructions:
    def __init__(self, parameters, id):
        self.parameters = parameters
        self.id = id
    def printObject(self):
        print (id)

class Array:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def addType(self, type):
        self.type = type

    def addValue(self, value):
        self.value = value

    def printObject(self):
        print(self.name, self.size)

class ArrayAssignation:
    def __init__(self, name, index, value):
        self.name = name
        self.index = index
        self.value = value

    def printObject(self) :
        print(self.name, self.index, self.value)
