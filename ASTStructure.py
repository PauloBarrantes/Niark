class File:
    def __init__(self):
        self.functions = []
        self.variables = dict()
        self.instructionList = []

    def addFunction(self, function):
        self.functions.append(function)

    def addVariable(self, variable):
        self.variables = {variable.name, variable}

    def eliminateVariable(self, name):
        del self.variables[name]

    def modifyValue(self, name, value):
        self.variables[name] = value


class Function:
    functionDomain = False
    returnType = False
    name = ''
    def __init__(self, returnType, functionDomain, name):
        self.functionDomain = functionDomain
        self.returnType = returnType
        self.name = name
        self.instructionList = []
        self.variables = dict()

    def addVariable(self, variable):
        self.variables = {variable.name, variable}

    def eliminateVariable(self, name):
        del self.variables[name]

    def modifyValue(self, name, value):
        self.variables[name] = value

class Variable:
    def __init__(self, type, value, name):
        self.name = name
        self.type = type
        self.value = value

class VariableDeclaration:
    def __init__(self, id, variable):
        self.id = id
        self.variable = variable

class For:
    id = 'FOR'
    def __init__(self):
        self.conditions = []
        self.arithmethicOperations = []
        self.localVariables = {}
        self.instructionList = []

class If:
    id = 'IF'
    def __init__(self):
        self.conditions = []
        self.logicalOperators = []
        self.localVariables = {}
        self.instructionList = []

class Else:
    id = 'ELSE'
    def __init__(self):
        self.localVariables = {}
        self.instructionList = []

class Condition:
    def __init__(self, term1, term2, operator):
        self.term1 = term1
        self.term2 = term2
        self.operator = operator

class FunctionCall:
    id = 'CALL'
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

class VariableAssignation:
    id = 'ASSIGNATION'
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Instructions:
    def __init__(self, name, parameters, id):
        self.name = name
        self.parameters = parameters
        self.id - id