
#Bases de datos de estudiantes, instructores
estudiantesBaseDatos=[]
instructoresBaseDatos=[]


#---------CLASE DE USUARIOS------------------
class Usuario:             
    def __init__(self, nombre, edad, id):
        self.__nombre=nombre
        self.__edad=edad
        self.__id=id

    def __str__(self):      #str para información
        return f"{self.__nombre} de {self.__edad} años, tiene el id: {self.__id}" 

    def getNombre(self):        #Obtener nombre 
        return self.__nombre

    def getId(self):        #Obtener id
        return self.__id


#---------CLASE DE Estudiante------------------    
class Estudiante(Usuario):
    def __init__(self, nombre, edad, id, carrera):
        super().__init__(nombre, edad, id)
        self.carrera=carrera
        estudiantesBaseDatos.append(self)


#---------CLASE DE INSTRUCTOR------------------
class Instructor(Usuario):
    def __init__(self, nombre, edad, id, profesion):
        super().__init__(nombre, edad, id)
        self.__profesion=profesion
        instructoresBaseDatos.append(self)

    def __str__(self):
        return f"{self.getNombre()}, {self.__profesion}" 
    

juan = Instructor("Juan", 35, 1001, "Licenciado en Matemáticas")


julian = Estudiante("Julian", 20, 23421, "Psicología")
oscar = Estudiante("Oscar", 22, 23422, "Ingeniería")
ana = Estudiante("Ana", 21, 23423, "Filosofía") 


