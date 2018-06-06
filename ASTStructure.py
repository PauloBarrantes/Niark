class File:
    def __init__(self):
        self.instructionList = []

    def addInstruction(self, instruction):
        self.instructionList.insert(0,instruction)

    def printObject(self):
        for x in range (0, len(self.instructionList)):
            self.instructionList[x].printObject()

#############################################################
# Begin simple instruction section
#############################################################

class VariableAssignation:
    id = 'VARIABLE ASSIGNATION'
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def printObject(self):
        print(self.id,self.name,self.value)

class ArrayAssignation:
    id = 'ARRAY ASSIGNATION'
    def __init__(self, name, index, value):
        self.name = name
        self.index = index
        self.value = value

    def printObject(self) :
        print(self.id,self.name, self.index, self.value)



class VariableDeclaration:
    id = 'VARIABLE DECLARATION'
    def __init__(self, variable):
        self.variable = variable

    def printObject(self):
        print(self.id,self.variable.printObject())

class ArrayDeclaration:
    id = 'ARRAY DECLARATION'
    def __init__(self, array):
        self.array = array

    def printObject(self):
        print(self.id,self.array.printObject())



class Instruction:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def printObject(self):
        print(self.id, self.value)




class FunctionCall:
    id = 'FUNCTION CALL'
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

    def printObject(self):
        print(self.id)

#############################################################
# End simple instruction section
#############################################################



#############################################################
# Begin parameters, conditions and arithmetics
#############################################################

class Condition:
    id = 'CONDITION'
    def __init__(self, term1, operator, term2):
        self.term1 = term1
        self.term2 = term2
        self.operator = operator

    def printObject(self):
        print(self.id,self.term1, self.term2, self.operator)

#############################################################
# End parameters, conditions and arithmetics
#############################################################



#############################################################
# Begin complex instruction section
#############################################################

class If:
    id = 'IF'
    def __init__(self, conditions,instructionList):
        self.conditions = conditions
        self.instructionList = instructionList

    def printObject(self):
        print(self.id,self.conditions,self.instructionList)
        if(self.conditions != None):
            self.conditions.printObject()

        if(self.instructionList != None):
            for x in range (len(self.instructionList)):
                self.instructionList[x].printObject()
        else:
            print('No instructions in the IF section')


class IfAndElse:
    id = 'IFANDELSE'
    def __init__(self,conditions,instructionListIf,instructionListElse):
        self.conditions = conditions
        self.instructionListIf = instructionListIf
        self.instructionListElse = instructionListElse

    def printObject(self):
        print(self.id,self.conditions,self.instructionListIf,self.instructionListElse)
        if (self.conditions != None):
            self.conditions.printObject()

        if (self.instructionListIf != None):
            for x in range(len(self.instructionListIf)):
                self.instructionListIf[x].printObject()
        else:
            print('No instructions in the IF section')

        if (self.instructionListElse != None):
            for x in range(len(self.instructionListElse)):
                self.instructionListElse[x].printObject()
        else:
            print('No instructions in the ELSE section')

#############################################################
# End complex instruction section
#############################################################



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

    def printObject(self):
        print("Soy una funcion")
        for x in range (0, len(self.instructionList)):
            print("ejecuta")
            self.instructionList[x].id





class For:
    id = 'FOR'
    def __init__(self):
        self.conditions = []
        self.arithmethicOperations = []
        self.localVariables = {}
        self.instructionList = []

    def printObject(self):
        print(id)
        for x in range (0, len(self.instructionList)):
            self.instructionList[x].printObject()




#############################################################
# Begin variables section
#############################################################

class Variable:
    id = 'VARIABLE'
    def __init__(self, name,value):
        self.name = name
        self.value = value

    def printObject(self):
        print(self.id, self.name, self.value)

class Array:
    id = 'ARRAY'
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def printObject(self):
        print(self.id, self.name, self.size)

#############################################################
# End variables section
#############################################################