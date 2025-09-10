estudiantesBaseDatos=[]
instructoresBaseDatos=[]
cursosBaseDatos=[]

class Usuario:
    def __init__(self, nombre, edad, id):
        self.__nombre=nombre
        self.__edad=edad
        self.__id=id

    def getNombre(self):
        return self.__nombre

    def getId(self):
        return self.__id
    

class Estudiante(Usuario):
    def __init__(self, nombre, edad, id, carrera):
        super().__init__(nombre, edad, id)
        self.carrera=carrera
        estudiantesBaseDatos.append(self)


class Instructor(Usuario):
    def __init__(self, nombre, edad, id, profesion):
        super().__init__(nombre, edad, id)
        self.profesion=profesion
        instructoresBaseDatos.append(self)

    def getInfo(self):
        return f"{self.getNombre()}, {self.profesion}" 
