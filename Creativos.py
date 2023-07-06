class Creativos:
    rut=0
    nombre=''
    apellido=''
    num_entrada=0
    valor=0

    def __int__(self):
        self.rut = '12345678'
        self.nombre='s/a'
        self.apellido='s/a'
        self.num_entrada=100
        self.valor=0


    def setRut(self,rut):
        if len(rut>=1) and len(rut<=8):
            self.rut= rut
            return True
        else:
            print("rut no valido")
            return False


    def SetNombre (self, nombre):
        if len(nombre >3) and len(nombre <20):
            self.Nombre=nombre
            return True
        else:
            print("los caracteres del nombre no coiciden, (debe ser entre 3 y 20)")
            return False

    def SetApellido (self, apellido):
        if len(apellido >4) and len(apellido <20):
            self.apellido=apellido
            return True
        else:
            print("los caracteres del nombre no coiciden, (debe ser entre 4 y 20)")
            return False

    def SetNum_entrada (self,num_entrada):
        if len(num_entrada>0) and len(num_entrada<101):
            self.num_entrada=num_entrada
            return True
        else:
            print("la entrada no es valida, (debe ser un numero del 1 al 100)")
            return False