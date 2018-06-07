from parser import *
from ASTStructure import *



def semantic():
    parse()
    niark = getNiarkCode()
    niark.printObject("")

semantic()
