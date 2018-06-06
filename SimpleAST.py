
class GlobalFile:
    instructionList = []

    def __init__(self):
        pass

    def imprimir(self):
        if self.instructionList is not None:
            print("hay algo")


class VariableDeclaration:
    def __init__(self, name):
        self.name = name

    def imprimir(self):
        print(self.name)

