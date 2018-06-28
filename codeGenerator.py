from BitMap import *
from semantic import *

def codeGenerator():
    if True:
        semantic()
        niark = getNiark()
        executable = open("CompiledCode.txt", "w+")
        for list in niark:
            for object in list:
                generateCode(object, executable)
        executable.close()
    else:
        print("Please fix errors so we can create an executable.")

def generateCode(object, file):
    file.write("Este es un archivo de prueba")

codeGenerator()