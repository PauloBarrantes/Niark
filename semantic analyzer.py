a = {'a': 1, 'a':2, 'b':2, 'c': 3}
a['a'] = 3
print(a.get('a'))

class Atributos:
    __name = ""
    __value = 0

    def __init__(self, n, v):
        self.__name= n
        self.__value = v

    def __getattr__(self):
        print(self.__name, self.__value)

x = Atributos("hola",0)
x.__getattr__()
# import ply.yacc as yacc
# import parserTemporal
#
# def metodo(n):
#     print(parser.parser.token)
#
#