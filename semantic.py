from parser import *
from ASTStructure import *
#from tableOfSymbols import *

'''
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1+list2

print (list3)
print (list2)
print (list1)

'''
#tos =  TableOfSymbols()
#tos.insert(2)
def semantic():
    parse()
    niark = getNiarkCode()
    niark.printObject("")

semantic()
