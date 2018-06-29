class BitMap:
    def __init__(self):
        self.bitmap = []

    def liberar(self,snameReg):
        encontrado = False
        contador = 0
        while (contador < 32) and not encontrado:
            if self.bitmap[contador].state == False:
                encontrado = True
            else:
                contador += 1
        self.bitmap[contador].state = False

    def obtener(self):
        print("gg1")
        encontrado = False
        contador = 0
        while contador < 32 and not encontrado:
            if self.bitmap[contador].state == False:
                encontrado = True
            else:
                contador += 1

        print("gg4",contador)
        if contador == 32:
            contador = -1
        self.bitmap[contador].state = True
        return self.bitmap[contador].nameReg

    def imprimir(self):
        for bit in self.bitmap:
            print(bit.nameReg, bit.state)
            
    def inicializar(self):

        bit1 = bit("$zero",True)
        self.bitmap.append(bit1)
        bit2 = bit("$v0",False)
        self.bitmap.append(bit2)
        bit3 = bit("$v1",False)
        self.bitmap.append(bit3)
        bit4 = bit("$a0",False)
        self.bitmap.append(bit4)
        bit5 = bit("$a1",False)
        self.bitmap.append(bit5)
        bit6 = bit("$a2",False)
        self.bitmap.append(bit6)
        bit7 = bit("$a3",False)
        self.bitmap.append(bit7)
        bit8 = bit("$t0",False)
        self.bitmap.append(bit8)
        bit9= bit("$t1",False)
        self.bitmap.append(bit9)
        bit10 = bit("$t2",False)
        self.bitmap.append(bit10)
        bit11 = bit("$t3",False)
        self.bitmap.append(bit11)
        bit12 = bit("$t4",False)
        self.bitmap.append(bit12)
        bit13 = bit("$t5",False)
        self.bitmap.append(bit13)
        bit14 = bit("$t6",False)
        self.bitmap.append(bit14)
        bit15 = bit("$t7",False)
        self.bitmap.append(bit15)
        bit16 = bit("$s0",False)
        self.bitmap.append(bit16)
        bit17 = bit("$s0",False)
        self.bitmap.append(bit17)
        bit18 = bit("$s1",False)
        self.bitmap.append(bit18)
        bit19 = bit("$s2",False)
        self.bitmap.append(bit19)
        bit20 = bit("$s3",False)
        self.bitmap.append(bit20)
        bit21 = bit("$s4",False)
        self.bitmap.append(bit21)
        bit22 = bit("$s5",False)
        self.bitmap.append(bit22)
        bit23 = bit("$s6",False)
        self.bitmap.append(bit23)
        bit24 = bit("$s7",False)
        self.bitmap.append(bit24)
        bit25 = bit("$s8",False)
        self.bitmap.append(bit25)
        bit26 = bit("$t8",False)
        self.bitmap.append(bit26)
        bit27 = bit("$t9",False)
        self.bitmap.append(bit27)
        bit28 = bit("$gp",False)
        self.bitmap.append(bit28)
        bit29 = bit("$sp",False)
        self.bitmap.append(bit29)
        bit30 = bit("$fp",False)
        self.bitmap.append(bit30)
        bit31 = bit("$ra",True)
        self.bitmap.append(bit31)

class bit:
    nameReg = ''
    state = False
    def __init__(self, nameReg, state):
        self.nameReg = nameReg
        self.state = state


