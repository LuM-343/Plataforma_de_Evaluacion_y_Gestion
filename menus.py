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
    # Funciones auxiliares de validación de entrada de datos
    def pedir_id(self, mensaje):
        # Pide al usuario un ID numérico sin espacios
        while True:
            entrada = input(mensaje).strip()  # Elimina espacios
            if entrada.isdigit():  # Valida que sean números
                return entrada
            print("❌ El ID debe ser numérico y sin espacios.")

    def pedir_nombre(self, mensaje):
        # Pide al usuario un nombre sin números
        while True:
            entrada = input(mensaje).strip().title()
            if entrada.replace(" ", "").isalpha():  # Letras y espacios permitidos
                return entrada
            print("❌ El nombre no debe contener números ni caracteres inválidos.")

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

                # Enlista los cursos disponibles con sus código y nombres
                print("\n📘 Cursos disponibles:")
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
                    print("\n👥 Estudiantes disponibles:")
                    for e in estudiantes.values():
                        print(f"- {e.id} - {e.nombre}")
                    est_id = self.pedir_id("ID del estudiante: ") # Pide el ingreso del ID del estudiante a inscribir y lo valida

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

                # Muestra el listado de cursos disponibles
                print("\n📘 Cursos disponibles:")
                for c in cursos.values():
                    print(f"- {c.getCodigo()} - {c.getNombre()}")
                codigo = input("Código del curso: ") # Ingresa el código del curso 
                # Verifca el código del curso 
                if codigo in cursos:
                    # Se pide el tipo, nombre y ponderación de la evaluación a crear
                    tipo = input("Tipo (examen/tarea): ").lower() 
                    nombre = input("Nombre de la evaluación: ")
                    # Manejo de errores en entrada tipo float de 'ponderación'
                    try:
                        ponderacion = float(input("Ponderación (ej. 0.3): "))
                    except ValueError:
                        print("❌ Ponderación inválida. Debe ser un número.")
                        continue

                    # Se verifica que tipo de evaluación es
                    if tipo == "examen":
                        # Si es de tipo 'examen' se pide su atributo específico 
                        # Manejo de errores en entrada tipo int de 'duración'
                        try:
                            duracion = int(input("Duración en minutos: "))
                        except ValueError:
                            print("❌ Duración inválida. Debe ser un número entero.")
                            continue
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

                # Muestra el listado de cursos disponibles
                print("\n📘 Cursos disponibles:")
                for c in cursos.values():
                    print(f"- {c.getCodigo()} - {c.getNombre()}")
                codigo = input("Código del curso: ") # Se ingresa el código del curso donde se registrará la calificación
                
                # Se valida que exista el curso ingresado
                if codigo in cursos:
                    curso = cursos[codigo] # Se asigna el curso en donde se estará trabajando

                    # Valida que existan evaluaciones dentro del curso
                    if not curso.getEvaluaciones():
                        print("⚠️ No hay evaluaciones en este curso.")
                        continue

                    # Enlista los estudiantes disponibles a inscribir con su ID y nombre
                    print("\n👥 Estudiantes en el curso:")
                    for e in curso.getEstudiantes().values():
                        print(f"- {e.id} - {e.nombre}")
                    est_id = self.pedir_id("ID del estudiante: ") # Se pide el ingreso del ID del estudiante para su nota y lo valida

                    # Valida que exista el estudiante dentro del curso
                    if est_id not in curso.getEstudiantes():
                        print("❌ Estudiante no inscrito en el curso.")
                        continue

                    # Enlista las evaluaciones que están dentro del curso
                    print("\nEvaluaciones disponibles:")
                    for idx, ev in enumerate(curso.getEvaluaciones(), 1):
                        print(f"{idx}. {ev.tipo()} {ev.nombre}")

                    # Ingreso del ID de la evaluación y la nota a registrar con manejo de errores en entrada
                    try:
                        idx = int(input("Elige evaluación: ")) - 1
                        nota = float(input("Nota: "))
                    except ValueError:
                        print("❌ Entrada inválida. Debe ingresar números.")
                        continue

                    # Validación del rango de opciones de evaluación
                    if 0 <= idx < len(curso.getEvaluaciones()):
                        # Se obtiene la lista de evaluaciones del curso
                        # Se selecciona la evaluación elegida por su índice
                        # Se llama al método 'asignar_nota' de esa evaluación, registrando la nota del estudiante en esa evaluación específica
                        curso.getEvaluaciones()[idx].asignar_nota(est_id, nota, curso.getEstudiantes())
                        print("✅ Nota registrada.")
                    else:
                        print("❌ Número de evaluación inválido.")
                else:
                    print("❌ Curso no encontrado.")

            elif op == "5":  # Ver calificaciones
                # Validar la existencia de cursos
                if not cursos:
                    print("⚠️ No hay cursos creados aún.")
                    continue

                # Muestra el listado de cursos disponibles
                print("\n📘 Cursos disponibles:")
                for c in cursos.values():
                    print(f"- {c.getCodigo()} - {c.getNombre()}")
                codigo = input("Código del curso: ") # Ingreso del código del curso a ver las calificaciones
                
                # Verifica existencia del curso
                if codigo in cursos:
                    cursos[codigo].mostrar_calificaciones() # Se llama al método 'mostrar_calificaciones' del módulo 'evaluaciones'
                else:
                    print("❌ Curso no encontrado.")

            elif op == "6":  # Reporte de promedios bajos
                # Validar la existencia de cursos
                if not cursos:
                    print("⚠️ No hay cursos creados aún.")
                    continue

                # Muestra el listado de cursos disponibles
                print("\n📘 Cursos disponibles:")
                for c in cursos.values():
                    print(f"- {c.getCodigo()} - {c.getNombre()}")
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

    # Menú para Estudiante
    def menu_estudiante(self, estudiante_id): # Se pide como parámetro el ID del estudiante a ingresar
        while True:
            # Se muestra una lista de opciones únicas para el estudiante
            print(f"\n--- Menú Estudiante ({estudiantes[estudiante_id].nombre}) ---") # Se muestra el nombre del catedrático dentro del programa
            print("1. Ver cursos inscritos")
            print("2. Ver calificaciones")
            print("0. Salir")
            op = input("Opción: ") # Ingreso de opción

            if op == "1":  # Ver cursos inscritos
                # Se obtiene todos los cursos en los que un estudiante está inscrito y los guarda en la lista 'cursos_inscritos'
                cursos_inscritos = [c for c in cursos.values() if estudiante_id in c.getEstudiantes()]
                # Verifica que el estudiante esté inscrito a cursos
                if not cursos_inscritos:
                    print("⚠️ No estás inscrito en ningún curso.")
                else:
                    # Se desenglosa los cursos en los cuales está inscrito
                    print("\n📘 Cursos inscritos:")
                    for c in cursos_inscritos:
                        print(f"- {c.getNombre()} (Catedrático: {c.getCatedratico().nombre})")

            elif op == "2":  # Ver calificaciones
                # Se obtiene todos los cursos en los que un estudiante está inscrito y los guarda en la lista 'cursos_inscritos'
                cursos_inscritos = [c for c in cursos.values() if estudiante_id in c.getEstudiantes()]
                # Verifica que el estudiante esté inscrito a cursos
                if not cursos_inscritos:
                    print("⚠️ No estás inscrito en ningún curso.")
                else:
                    # Recorre los cursos en los cuáles está inscrito el estudiante
                    for c in cursos_inscritos:
                        # Calcula el promedio del estudiante del curso 'c' iterado, por medio del método 'promedio_estudiante' del módulo 'clase_curso'
                        prom = c.promedio_estudiante(estudiante_id)
                        if not c.getEvaluaciones(): # Verificación de existencia de evaluaciones dentro del curso
                            print(f"\n📘 {c.getNombre()} - ⚠️ No hay evaluaciones registradas.")
                        else:
                            # Mustra el curso y promedio si existe o 'Sin notas' si no existe
                            print(f"\n📘 {c.getNombre()} - Promedio: {prom if prom else 'Sin notas'}")
                            # Recorre las evaluaciones y obtiene la nota por medio del método 'obtener_nota' del módulo 'evaluaciones'
                            for ev in c.getEvaluaciones():
                                nota = ev.obtener_nota(estudiante_id)
                                print(f"  {ev.tipo()} {ev.nombre}: {nota if nota else 'Sin nota'}")

            elif op == "0": # Opción para finalizar el menú del estudiante
                break
            else: # Ingreso de opción fuera de rango de opciones del menú
                print("❌ Opción inválida.")

    # Menú Principal
    def menu_principal(self):
        while True:
            # Lista de opciones del menú principal
            print("\n--- Menú Principal ---")
            print("1. Registrar estudiante")
            print("2. Registrar catedrático")
            print("3. Ingresar como estudiante")
            print("4. Ingresar como catedrático")
            print("0. Salir")
            op = input("Opción: ") # Ingreso de opción

            if op == "1":  # Registrar estudiante
                id_est = self.pedir_id("ID del estudiante: ") # Ingreso del ID del estudiante validándolo
                # Manejo de duplicación de ID registrado 
                if id_est in estudiantes:
                    print("⚠️ Ya existe un estudiante con ese ID.")
                    continue

                nombre = self.pedir_nombre("Nombre del estudiante: ").title() # Ingreso del nombre del estudiante a registrar y validándolo
                estudiantes[id_est] = Estudiante(id_est, nombre) # Se agrega el registro del estudiante al diccionario 'estudiantes' con el objeto del módulo 'clase_usuario'
                print(f"✅ Estudiante {nombre} registrado.")

            elif op == "2":  # Registrar catedrático
                id_cat = self.pedir_id("ID del catedrático: ") # Ingreso del ID del catedrático y validándolo
                # Manejo de duplicación de ID registrado
                if id_cat in catedraticos:
                    print("⚠️ Ya existe un catedrático con ese ID.")
                    continue

                nombre = self.pedir_nombre("Nombre del catedrático: ").title() # Ingreso del nombre del catedrático a registrar y validándolo
                catedraticos[id_cat] = Catedratico(id_cat, nombre) # Se agrega el registro del catedrático al diccionario 'catedraticos' con el objeto del módulo 'clase_usuario'
                print(f"✅ Catedrático {nombre} registrado.")

            elif op == "3":  # Ingresar como estudiante
                id_est = self.pedir_id("ID del estudiante: ") # Ingreso del ID del estudiante y validándolo
                # Verifica el registro del estudiante
                if id_est in estudiantes:
                    self.menu_estudiante(id_est) # Se llama al menú para estudiantes
                else:
                    print("❌ Estudiante no registrado.")

            elif op == "4":  # Ingresar como catedrático
                id_cat = self.pedir_id("ID del catedrático: ") # Ingreso del ID del catedrático y validándolo
                # Verifica el registro del catedrático
                if id_cat in catedraticos:
                    self.menu_catedratico(id_cat) # Se llama al menú para catedráticos
                else:
                    print("❌ Catedrático no registrado.")

            elif op == "0":  # Opción para salir del programa
                print("👋 Saliendo del sistema...")
                break
            else: # Ingreso de opción fuera de rango de opciones del menú
                print("❌ Opción inválida.")