#Parte realizada por Luis Manuel

import clase_usuario #Importar la clase usuario
cursosBaseDatos=[]  #Base de Datos de Cursos

# ----Clase Curso------
class Curso:        #Clase para cursos, con nombre, aula, capacidad, codigo e instructor, realizar comprobaciones antes de crear instancia!!!
    def __init__(self, nombre, capacidad, codigo, aula, instructor):    #Se utilizan atributos privados
        self.__nombre=nombre
        self.__capacidad=capacidad
        self.__aula=aula
        self.__codigo=codigo
        self.__instructor=instructor
        self.__notaTotal=0      #Total de notas subidas en el curso
        self.__estudiantes={}       #Estudiantes incritros
        self.__actividades=[]       #Actividades realizadas
        cursosBaseDatos.append(self)
    
    def getCodigo(self):        #Obtener codigo unico del curso
        return self.__codigo
    
    def infoCurso(self):        #Resumen general del curso
        print("\n----- Resumen del Curso -----")
        print("Materia:", self.__nombre)
        print("Capacidad del curso:", self.__capacidad)
        print("Aula:", self.__aula)
        print("Instructor:", self.__instructor.__str__())

    def agregar_estudiante(self, estudiante):   #Metodo para agregar estudiantes
        if len(self.__estudiantes)>= self.__capacidad:      #Comprobar que el curso no este lleno
            raise ValueError("ERROR, El curso llegó a su capacidad máxima, pide que abran otra sección")
        
        for alumno in self.__estudiantes.values():
            if alumno["estudiante"].getId()== estudiante.getId():  #Comprobar que el estudiante no este inscrito ya
                raise ValueError ("ERROR, El estudiante ya se encuentra inscrito en el curso")

        self.__estudiantes[estudiante.getId()] = {"estudiante": estudiante, "notas": []} # Aquí se guardarán las notas de las evaluaciones}
        print("Usuario agregado")                   

    def informeGeneral(self):           #Informe de notas de todos los estudiantes
        print("\n----- Informe General de Notas -----")
        print("Estudiante           | Nota")
        for alumno in self.__estudiantes.values():
            print(f"- {alumno["estudiante"].getNombre()}: {sum(alumno['notas'])}")

    def reporteBajoRendimiento(self):       #metodo para mostrar estudiantes con mal rendimiento
        if self.__notaTotal>0:        #Comprobar que ya se hayan subido alguna nota
            print("\nEstudiantes con bajo rendimiento")
            for alumno in self.__estudiantes.values():
                if sum(alumno["notas"])/self.__notaTotal <65:      #Comprobar que en porcentaje sea menor a 65 para mostrar
                    print(f"-{alumno["estudiante"].getNombre()}, con {sum(alumno['notas'])}pts, equivale al {sum(alumno['notas'])/self.__notaTotal*100}% de la nota total")
        else:
            raise ZeroDivisionError("ERROR, Primero ingresa alguna nota")
        

mate = Curso("Álgebra", 2, "B212", 23123, clase_usuario.juan)
mate.agregar_estudiante(clase_usuario.julian)  
mate.agregar_estudiante(clase_usuario.oscar)   
#mate.agregar_estudiante(julian)  
#mate.agregar_estudiante(ana)     

mate.infoCurso()

mate.informeGeneral()
#mate.reporteBajoRendimiento()