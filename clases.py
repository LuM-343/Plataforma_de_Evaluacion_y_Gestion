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
    
class Curso:
    def __init__(self, nombre, capacidad, aula, codigo, instructor):
        self.nombre=nombre
        self.__capacidad=capacidad
        self.__aula=aula
        self.__codigo=codigo
        self.__instructor=instructor
        self.notaTotal=0
        self.__estudiantes=[]
        self.__actividades={}
    
    def getCodigo(self):
        return self.__codigo
    
    def infoCurso(self):
        print("\n----- Resumen del Curso -----")
        print("Materia:", self.nombre)
        print("Capacidad del curso:", self.__capacidad)
        print("Aula:", self.__aula)
        print("Instructor:", self.__instructor.getInfo())

    def informeGeneral(self):
        print("\n----- Informe General de Notas -----")
        print("Estudiante           | Nota")
        for alumno in self.__estudiantes:
            print(f"- {alumno["estudiante"].getNombre()}: {alumno["notas"]}")

    def reporteBajoRendimiento(self):
        if self.notaTotal>0:
            print("\nEstudiantes con bajo rendimiento")
            for alumno in self.__estudiantes:
                if alumno["notas"]/self.notaTotal <65:
                    print(f"-{alumno["estudiante"].getNombre()}, con {alumno["notas"]}, equivale al {alumno["notas"]/self.notaTotal*100}% de la nota total")
        else:
            print("Primero debes ingresar notas")
    
    def agregar_estudiante(self, estudiante):
        if len(self.__estudiantes)>= self.__capacidad:
            print("El curso llegó a su capacidad máxima, pide que abran otra sección")
            return
        
        for alumno in self.__estudiantes:
            if alumno["estudiante"].getId() == estudiante.getId():
                print("El estudiante ya se encuentra inscrito en el curso")
                return
        a={"estudiante": estudiante,
           "notas":0}
        self.__estudiantes.append(a)
        print("Usuario agregado")

juan = Instructor("Juan", 35, 1001, "Licenciado en Matemáticas")
mate = Curso("Álgebra", 2, "B212", 23123, juan)

julian = Estudiante("Julian", 20, 23421, "Psicología")
oscar = Estudiante("Oscar", 22, 23422, "Ingeniería")
ana = Estudiante("Ana", 21, 23423, "Filosofía") 


mate.agregar_estudiante(julian)  
mate.agregar_estudiante(oscar)   
mate.agregar_estudiante(julian)  
mate.agregar_estudiante(ana)     

mate.infoCurso()

mate.informeGeneral()