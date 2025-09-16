# ==============================
# MÓDULO: Evaluaciones
# ==============================

# Clase base para manejo de evaluaciones
class Evaluacion:
    # Atributos: nombre, ponderación y notas con información adicional   
    def __init__(self, nombre, ponderacion, **kwargs):
        self.nombre = nombre
        self.ponderacion = ponderacion
        self.notas = {}        # {id_estudiante: {"nota": x, "info": args, "extra": kwargs}}
        self.extra = kwargs

    #  Método de asignación de notas
    def asignar_nota(self, estudiante_id, nota, inscritos, *args, **kwargs): # Parámetros: ID del estudiante, nota, inscritos: lista de estudiantes inscritos en el curso, args: información extra (comentarios o detalles), kargs: información extra (fecha, rúbrica, tiempo)
        # Validación de estudiante inscrito en el curso 
        if estudiante_id not in inscritos:
            raise ValueError(f"❌ Estudiante con ID {estudiante_id} no inscrito en el curso.")
        # Validación para que la nota esté entre 0 y 100 puntos
        if nota < 0 or nota > 100:
            raise ValueError("❌ La nota debe estar entre 0 y 100.")
        self.notas[estudiante_id] = {"nota": nota, "info": args, "extra": kwargs} # Se almacena la nota en 'notas'

    # Método para consultar la nota de estudiante
    def obtener_nota(self, estudiante_id): # Parámetro: ID del estudiante
        datos = self.notas.get(estudiante_id)
        return datos["nota"] if datos else None # Devuelve la nota si existe, o 'None' si no tiene nota asignada

# Subclase para crear evaluaciones tipo Examen (Herencia)
class Examen(Evaluacion):
    # Atributo adicional: duración en minutos del examen
    def __init__(self, nombre, ponderacion, duracion_minutos, **kwargs):
        super().__init__(nombre, ponderacion, **kwargs)
        self.duracion_minutos = duracion_minutos

    # Método para redefinir el tipo de evaluación a Examen (Polimorfismo)
    def tipo(self):
        return "Examen"