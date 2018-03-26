class estudiante:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido



nombre = raw_input("Nombre ")
apellido = raw_input("Apellido ")
x = estudiante(nombre, apellido)
print(x.nombre)
print(x.apellido)
