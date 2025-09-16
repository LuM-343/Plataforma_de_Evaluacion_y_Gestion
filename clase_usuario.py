#Parte a cargo de Luis Manuel

#Bases de datos de estudiantes, instructores
estudiantesBaseDatos={}
instructoresBaseDatos={}

#---------CLASE DE USUARIOS------------------
class Usuario:             
    def __init__(self, nombre, edad, id, correo):
        self.__nombre=nombre
        self.__edad=edad
        self.__id=id
        self.__correo=correo

    def __str__(self):      #str para información
        return f"{self.__nombre} de {self.__edad} años, tiene el id: {self.__id}, contacto al {self.__correo}" 

    def getNombre(self):        #Obtener nombre 
        return self.__nombre

    def getId(self):        #Obtener id
        return self.__id
    
    def getCorreo(self):        #Obtener id
        return self.__correo
    
    def getEdad(self):          #Obtener edad
        return self.__edad


#---------CLASE DE Estudiante------------------    
class Estudiante(Usuario):
    def __init__(self, nombre, edad, id, correo, carrera):
        super().__init__(nombre, edad, id, correo)
        self.__carrera=carrera
        estudiantesBaseDatos[self.getId()]=self     #Guardamos las instancias creadas en un diccionario para consultas posteriores

    def __str__(self):
        return f"{self.getNombre()}, de {self.getEdad()} años, tiene el id: {self.getId()} y estudia {self.__carrera}, contacto al {self.getCorreo()}"
    
    def resumen(self):
        return f"{self.getNombre()}, {self.__carrera}, contacto al {self.getCorreo()}" 

#---------CLASE DE INSTRUCTOR------------------
class Instructor(Usuario):
    def __init__(self, nombre, edad, id, correo, profesion):
        super().__init__(nombre, edad, id, correo)
        self.__profesion=profesion
        instructoresBaseDatos[self.getId()]=self    #Guardamos las instancias creadas en un diccionario para consultas posteriores

    def __str__(self):
        return f"{self.getNombre()}, de {self.getEdad()} años, tiene el id: {self.getId()} y su profesion es {self.__profesion}, contacto al {self.getCorreo()}"

    def resumen(self):
        return f"{self.getNombre()}, {self.__profesion}, contacto al {self.getCorreo()}" 
    