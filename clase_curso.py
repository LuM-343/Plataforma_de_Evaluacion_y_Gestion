#Parte realizada por Luis Manuel
from notas import mostrar_calificaciones, reporte_promedios_bajos
cursosBaseDatos={}  #Base de Datos de Cursos

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
        self.__evaluaciones = []        #Actividades realizadas
        cursosBaseDatos[self.__codigo]=self
    
    def getCodigo(self): return self.__codigo  #Obtener codigo unico del curso
    def getEstudiantes(self): return self.__estudiantes
    def getInstructor(self): return self.__instructor
    def getEvaluaciones(self): return self.__evaluaciones
    def getNombre(self): return self.__nombre

    def setInstructor(self, instructor):
        self.__instructor=instructor
        print("Instructor cambiado con exito")
    
    def resumen(self):
        return f"Curso: {self.__nombre}, con {len(self.__estudiantes)}/{self.__capacidad} estudiantes y se dará en el aula {self.__aula}"
    
    def infoCurso(self):        #Resumen general del curso
        print("\n----- Resumen del Curso -----")
        print("Materia:", self.__nombre)
        print("Capacidad del curso:", self.__capacidad)
        print("Aula:", self.__aula)
        print("Instructor:", self.__instructor.resumen())

    def agregarEstudiante(self, estudiante):   #Metodo para agregar estudiantes
        if len(self.__estudiantes)>= self.__capacidad:      #Comprobar que el curso no este lleno
            print("ERROR: El curso llegó a su capacidad máxima, pide que abran otra sección")
        
        if estudiante.getId() in self.__estudiantes:  #Comprobar que el estudiante no este inscrito ya
            print("ERROR: El estudiante ya se encuentra inscrito en el curso")

        self.__estudiantes[estudiante.getId()] = {"estudiante": estudiante, "notas": []} # Aquí se guardarán las notas de las evaluaciones}
        print("Estudiante agregado")  

    def eliminarEstudiante(self, estudiante):
        if estudiante.getId() in self.__estudiantes:  #Comprobar que el estudiante este inscrito
            del self.__estudiantes[estudiante.getId()]
            print("Estudiante eliminado")
        else:
            print ("ERROR: El estudiante no se encuentra inscrito a este curso")

    def informeGeneral(self):           #Informe de notas de todos los estudiantes
        print("\n----- Informe General de Notas -----")
        print("Estudiante           | Nota")
        for alumno in self.__estudiantes.values():
            print(f"- {alumno['estudiante'].getNombre()}: {sum(alumno['notas'])}")

    def agregar_evaluacion(self, evaluacion):
        self.__evaluaciones.append(evaluacion)
        print(f"✅ Evaluación '{evaluacion.nombre}' agregada en {self.__nombre}")

    def mostrar_calificaciones(self):
        mostrar_calificaciones(self)

    def promedio_estudiante(self, estudiante_id):
        total, peso_total = 0, 0
        for ev in self.__evaluaciones:
            nota = ev.obtener_nota(estudiante_id)
            if nota is not None:
                total += nota * ev.ponderacion
                peso_total += ev.ponderacion
        return total / peso_total if peso_total > 0 else None

    def reporte_promedios_bajos(self, limite=60):
        reporte_promedios_bajos(self, limite)