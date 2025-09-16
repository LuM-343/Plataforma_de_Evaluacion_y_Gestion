# ==============================
# MÓDULO: Menús
# ==============================

# Importación de módulos para uso de clases dentro de los menús
from clase_usuario import Estudiante, Catedratico
from clase_curso import Curso
from evaluaciones import Examen, Tarea

# Datos globales para almacenar los objetos del sistema y usarlos dentro del mismo
cursos = {}
estudiantes = {}
catedraticos = {}

# Clase base Menus
class Menus:
    # Menú para Catedrático
    def menu_catedratico(self, catedratico_id): # Se pide como parámetro el ID del catedrático
        while True:
            # Se muestra una lista de opciones únicas para el catedráico 
            print(f"\n--- Menú Catedrático ({catedraticos[catedratico_id].nombre}) ---") # Se muestra el nombre del catedrático dentro del programa
            print("1. Crear curso")
            print("2. Inscribir estudiante en curso")
            print("3. Crear evaluación")
            print("4. Registrar calificación")
            print("5. Ver calificaciones")
            print("6. Reporte promedios bajos")
            print("0. Salir")
            op = input("Opción: ") # Selección de opción

            if op == "1":  # Crear curso
                codigo = input("Código del curso: ") # Se pide código del curso a crear
                nombre = input("Nombre del curso: ") # Se pide nombre del curso a crear

                # Se crea un objeto 'Curso' con código, nombre y el catedrático que lo creó
                # Lo guarda en 'cursos' usando el código como clave
                cursos[codigo] = Curso(codigo, nombre, catedraticos[catedratico_id])
                print(f"✅ Curso '{nombre}' creado por {catedraticos[catedratico_id].nombre}")

            elif op == "2":  # Inscribir estudiante
                # Verifica que existan cursos
                if not cursos:
                    print("⚠️ No hay cursos creados aún.")
                    continue

                # EnliSta los cursos disponibles con sus código y nombres
                print("\nCursos disponibles:")
                for c in cursos.values():
                    print(f"- {c.getCodigo()} - {c.getNombre()}")
                codigo = input("Código del curso: ") # Pide al usuario el ingreso del código del curso a inscribir

                # Valida el código del curso
                if codigo in cursos:
                    # Verifica que existan estudiantes registrados en el curso
                    if not estudiantes:
                        print("⚠️ No hay estudiantes registrados aún.")
                        continue
                    # Enlista los estudiantes disponibles a inscribir con su ID y nombre
                    print("\nEstudiantes disponibles:")
                    for e in estudiantes.values():
                        print(f"- {e.id} - {e.nombre}")
                    est_id = input("ID del estudiante: ") # Pide el ingreso del ID del estudiante a inscribir

                    # Se valida el ID del estudiante y se agrega al curso po
                    if est_id in estudiantes:
                        cursos[codigo].agregar_estudiante(estudiantes[est_id]) # Añade al estudiante a la lista de inscritos del curso por medio del método 'agregar_estudiantes' de la clase 'Curso'
                    else:
                        print("❌ Estudiante no encontrado.")
                else:
                    print("❌ Curso no encontrado.")

            elif op == "3":  # Crear evaluación
                # Verifica que existan cursos
                if not cursos:
                    print("⚠️ No hay cursos creados aún.")
                    continue

                codigo = input("Código del curso: ") # Ingresa el código del curso 
                # Verifca el código del curso 
                if codigo in cursos:
                    # Se pide el tipo, nombre y ponderación de la evaluación a crear
                    tipo = input("Tipo (examen/tarea): ").lower() 
                    nombre = input("Nombre de la evaluación: ")
                    ponderacion = float(input("Ponderación (ej. 0.3): "))

                    # Se verifica que tipo de evaluación es
                    if tipo == "examen":
                        # Si es de tipo 'examen' se pide su atributo específico 
                        duracion = int(input("Duración en minutos: "))
                        evaluacion = Examen(nombre, ponderacion, duracion)  # Se crea el objeto para agregar al curso
                    else:
                        # Si no, es de tipo 'tarea' y se piden sus atributos específicos 
                        fecha = input("Fecha de entrega: ")
                        evaluacion = Tarea(nombre, ponderacion, fecha) # Se crea el objeto para agregar al curso

                    # Se agrega al curso con su método 'agregar_evaluacion' por medio del objeto 'evaluacion'
                    cursos[codigo].agregar_evaluacion(evaluacion)
                else:
                    print("❌ Curso no encontrado.")

            elif op == "4":  # Registrar calificación
                # Se verifica que existan cursos
                if not cursos:
                    print("⚠️ No hay cursos creados aún.")
                    continue

                # Se ingresa el código del curso donde se registrará la calificación
                codigo = input("Código del curso: ")
                # Se valida que exista el curso ingresado
                if codigo in cursos:
                    curso = cursos[codigo] # Se asigna el curso en donde se estará trabajando

                    # Valida que existan evaluaciones dentro del curso
                    if not curso.getEvaluaciones():
                        print("⚠️ No hay evaluaciones en este curso.")
                        continue

                    # Se pide el ingreso del ID del estudiante para su nota
                    est_id = input("ID del estudiante: ")
                    # Valida que exista el estudiante dentro del curso
                    if est_id not in curso.getEstudiantes():
                        print("❌ Estudiante no inscrito en el curso.")
                        continue

                    # Enlista las evaluaciones que están dentro del curso
                    print("\nEvaluaciones disponibles:")
                    for idx, ev in enumerate(curso.getEvaluaciones(), 1):
                        print(f"{idx}. {ev.tipo()} {ev.nombre}")

                    # Ingreso del ID de la evaluación y la nota a registrar
                    idx = int(input("Elige evaluación: ")) - 1
                    nota = float(input("Nota: "))

                    # Se obtiene la lista de evaluaciones del curso
                    # Se selecciona la evaluación elegida por su índice
                    # Se llama al método 'asignar_nota' de esa evaluación, registrando la nota del estudiante en esa evaluación específica
                    curso.getEvaluaciones()[idx].asignar_nota(est_id, nota, curso.getEstudiantes())
                    print("✅ Nota registrada.")
                else:
                    print("❌ Curso no encontrado.")

            elif op == "5":  # Ver calificaciones
                codigo = input("Código del curso: ") # Ingreso del código del curso a ver las calificaciones
                # Verifica existencia del curso
                if codigo in cursos:
                    cursos[codigo].mostrar_calificaciones() # Se llama al método 'mostrar_calificaciones' del módulo 'evaluaciones'
                else:
                    print("❌ Curso no encontrado.")

            elif op == "6":  # Reporte de promedios bajos
                codigo = input("Código del curso: ") # Ingreso del código del curso
                # Verifica existencia del curso
                if codigo in cursos:
                    cursos[codigo].reporte_promedios_bajos() # Se llama al método 'reporte_promedios_bajos' del módulo 'evaluaciones'
                else:
                    print("❌ Curso no encontrado.")

            elif op == "0": # Opción para finalizar el menú del catedrático
                break
            else: # Ingreso de opción fuera de rango de opciones del menú
                print("❌ Opción inválida.")