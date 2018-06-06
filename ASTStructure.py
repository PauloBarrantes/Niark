class Niark:
    def __init__(self):
        self.statements = []

    def addStatement(self, statement):
        self.statements.insert(0,statement)

    def printObject(self):
        for x in range (0, len(self.statements)):
            self.statements[x].printObject()

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



class IncDec:
    id = 'INCDEC'
    def __init__(self, operator, variable):
        self.operator = operator
        self.variable = variable

    def printObject(self):
        print(self.id,self.operator,self.variable)

#############################################################
# End simple instruction section
#############################################################



#############################################################
# Begin parameters, conditions, arithmetics and incdec
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
        self.instructions = instructionList.instructions

    def addInstruction(self, instruction):
        self.instructions.insert(0,instruction)

    def printObject(self):
        print(self.id,self.conditions,self.instructions)
        if(self.conditions != None):
            self.conditions.printObject()

        if(self.instructions != None):
            for x in range (len(self.instructions)):
                if (self.instructions[x] != None):
                    self.instructions[x].printObject()
        else:
            print('No instructions in the IF section')


class IfAndElse:
    id = 'IFANDELSE'
    def __init__(self,conditions,instructionListIf,instructionListElse):
        self.conditions = conditions
        self.instructionsIf = instructionListIf.instructions
        self.instructionsElse = instructionListElse.instructions

    def printObject(self):
        print(self.id,self.conditions,self.instructionsIf,self.instructionsElse)
        if (self.conditions != None):
            self.conditions.printObject()

        if (self.instructionsIf != None):
            for x in range(len(self.instructionsIf)):
                if (self.instructionsIf[x] != None):
                    self.instructionsIf[x].printObject()
        else:
            print('No instructions in the IF section')

        if (self.instructionsElse != None):
            for x in range(len(self.instructionsElse)):
                if (self.instructionsElse[x] != None):
                    self.instructionsElse[x].printObject()
        else:
            print('No instructions in the ELSE section')

class For:
    id = 'FOR'
    def __init__(self,declaration,conditions,incdec,instructionList):
        self.conditions = conditions
        self.incdec = incdec

        self.instructions = []
        self.instructions.insert(0,declaration)
        self.instructions.extend(instructionList.instructions)

    def printObject(self):
        print(self.id)
        self.conditions.printObject()
        self.incdec.printObject()

        if (self.instructions != None):
            for x in range(len(self.instructions)):
                if (self.instructions[x] != None):
                    self.instructions[x].printObject()

#############################################################
# End complex instruction section
#############################################################



class Function:
    functionDomain = False
    returnType = False
    name = ''
    def __init__(self, functionDomain, returnType, name, parameter,instructionList):
        self.functionDomain = functionDomain
        self.returnType = returnType
        self.name = name
        self.parameter = parameter
        self.instructions = instructionList.instructions

    def printObject(self):
        print("Soy una funcion")
        for x in range (0, len(self.instructionList)):
            print("ejecuta")
            self.instructionList[x].id



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

class InstructionList:
    id = 'INSTRUCTION LIST'
    def __init__(self,instruction,instructionList):
        self.instructions = []
        self.instructions.insert(0,instruction)

        if (instructionList is not None):
            self.instructions.extend(instructionList.instructions)

    def printObject(self):
        if (self.instructions != None):
            for x in range(len(self.instructions)):
                self.instructions[x].printObject()


#############################################################
# End variables section
#############################################################

