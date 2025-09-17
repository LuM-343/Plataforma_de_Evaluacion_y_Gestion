# ==============================
# CLASE: MENÚS
# ==============================
# Importación de módulos para uso de clases dentro de los menús
import utilidades
from clase_usuario import estudiantesBaseDatos, instructoresBaseDatos
from clase_curso import cursosBaseDatos
from evaluaciones import Examen, Tarea

# Clase base Menus
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
    def menu_catedratico(self, instructor):  # Al iniciar sesión se comparte la instancia del usuario con el método del menu
        catedratico_id=instructor.getId() #Se define el id del profesor para futuros llamados
        while True:
            # Se muestra una lista de opciones únicas para el catedráico 
            print(f"\n--- Menú Catedrático ({instructor.getNombre()}) ---") # Se muestra el nombre del catedrático dentro del programa
            print("1. Crear evaluación")
            print("2. Registrar calificación")
            print("3. Ver calificaciones")
            print("4. Reporte promedios bajos")
            print("0. Salir")
            op = input("Opción: ") # Selección de opción

            if op == "1":    # Crear evaluación
                # Verifica que existan cursos
                if not cursosBaseDatos:
                    print("⚠️ No hay cursos creados aún.")
                    continue

                # Muestra el listado de cursos disponibles
                print("\n📘 Cursos disponibles:")
                for c in cursosBaseDatos.values():
                    print(f"- {c.getCodigo()} - {c.getNombre()}")
                codigo = input("Código del curso: ") # Ingresa el código del curso 
                # Verifca el código del curso 
                if codigo in cursosBaseDatos:
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
                    cursosBaseDatos[codigo].agregar_evaluacion(evaluacion)
                else:
                    print("❌ Curso no encontrado.")

            elif op == "2":  # Registrar calificación
                # Se verifica que existan cursos
                if not cursosBaseDatos:
                    print("⚠️ No hay cursos creados aún.")
                    continue

                # Muestra el listado de cursos disponibles
                print("\n📘 Cursos disponibles:")
                for c in cursosBaseDatos.values():
                    print(f"- {c.getCodigo()} - {c.getNombre()}")
                codigo = input("Código del curso: ") # Se ingresa el código del curso donde se registrará la calificación
                
                # Se valida que exista el curso ingresado
                if codigo in cursosBaseDatos:
                    curso = cursosBaseDatos[codigo] # Se asigna el curso en donde se estará trabajando

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

            elif op == "3":  # Ver calificaciones
                # Validar la existencia de cursos
                if not cursosBaseDatos:
                    print("⚠️ No hay cursos creados aún.")
                    continue

                # Muestra el listado de cursos disponibles
                print("\n📘 Cursos disponibles:")
                for c in cursosBaseDatos.values():
                    print(f"- {c.getCodigo()} - {c.getNombre()}")
                codigo = input("Código del curso: ") # Ingreso del código del curso a ver las calificaciones
                
                # Verifica existencia del curso
                if codigo in cursosBaseDatos:
                    cursosBaseDatos[codigo].mostrar_calificaciones() # Se llama al método 'mostrar_calificaciones' del módulo 'evaluaciones'
                else:
                    print("❌ Curso no encontrado.")

            elif op == "4":  # Reporte de promedios bajos
                # Validar la existencia de cursos
                if not cursosBaseDatos:
                    print("⚠️ No hay cursos creados aún.")
                    continue

                # Muestra el listado de cursos disponibles
                print("\n📘 Cursos disponibles:")
                for c in cursosBaseDatos.values():
                    print(f"- {c.getCodigo()} - {c.getNombre()}")
                codigo = input("Código del curso: ") # Ingreso del código del curso
                
                # Verifica existencia del curso
                if codigo in cursosBaseDatos:
                    cursosBaseDatos[codigo].reporte_promedios_bajos() # Se llama al método 'reporte_promedios_bajos' del módulo 'evaluaciones'
                else:
                    print("❌ Curso no encontrado.")

            elif op == "0": # Opción para finalizar el menú del catedrático
                break
            else: # Ingreso de opción fuera de rango de opciones del menú
                print("❌ Opción inválida.")

    # Menú para Estudiante
    def menu_estudiante(self, estudiante):  # Al iniciar sesión se comparte la instancia del usuario con el método del menu
        estudiante_id=estudiante.getId()    #Se define el id del estudiante para futuros llamados
        while True:
            # Se muestra una lista de opciones únicas para el estudiante
            print(f"\n--- Menú Estudiante ({estudiante.getNombre()}) ---") # Se muestra el nombre del estudiante dentro del programa
            print("1. Asignación de cursos")
            print("2. Retiro académico")
            print("3. Ver cursos inscritos")
            print("4. Ver calificaciones")
            print("0. Salir")
            op = input("Opción: ")

            if op=="1": utilidades.agregar_estudiante(estudiante)   #Se llama a la función de agregar estudiante a curso en utilidades
            elif op=="2": utilidades.eliminarEstudiante(estudiante) #Se llama a la función eliminar estudiante (solo de un curso) en utilidades

            elif op == "3":  # Ver cursos inscritos
                # Se obtiene todos los cursos en los que un estudiante está inscrito y los guarda en la lista 'cursos_inscritos'
                cursos_inscritos = [c for c in cursosBaseDatos.values() if estudiante_id in c.getEstudiantes()]
                # Verifica que el estudiante esté inscrito a cursos
                if not cursos_inscritos:
                    print("⚠️ No estás inscrito en ningún curso.")
                else:
                    # Se desenglosa los cursos en los cuales está inscrito
                    print("\n📘 Cursos inscritos:")
                    for c in cursos_inscritos:
                        print(f"- {c.getNombre()} - {c.resumen()}")

            elif op == "4":  # Ver calificaciones
                # Se obtiene todos los cursos en los que un estudiante está inscrito y los guarda en la lista 'cursos_inscritos'
                cursos_inscritos = [c for c in cursosBaseDatos.values() if estudiante_id in c.getEstudiantes()]
                # Verifica que el estudiante esté inscrito a cursos
                if not cursos_inscritos:
                    print("⚠️ No estás inscrito en ningún curso.")
                else:
                    # Recorre los cursos en los cuáles está inscrito el estudiante
                    for c in cursos_inscritos:
                        # Calcula el promedio del estudiante del curso 'c' iterado, por medio del método 'promedio_estudiante' del módulo 'clase_curso'
                        prom = c.promedio_estudiante(estudiante_id)
                        if not c.getEvaluaciones(): # Verificación de existencia de evaluaciones dentro del curso
                            print(f"\n📘 {c.getNombre()} - ⚠️  No hay evaluaciones registradas.")
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

    # Menú para Administrativo
    def menu_administrativo(self):
        while True:
            print(f"\n--- Menú Administrativo ---")     #Se muestra el menu administrativo
            print("1. Estudiante")
            print("2. Instructores")
            print("3. Cursos")
            print("0. Salir")
            op = input("Opción: ")  #Se pide opción

            if op == "1":  # Opciones estudiantes
                print("\nMenú de gestión de estudiantes")  
                print("1. Agregar estudiante")
                print("2. Eliminar estudiante de todo el Sistema")
                print("0. Salir al menu principal")
                op2=input("Opción: ")   #Se pide opción

                if op2=="1": utilidades.crearEstudiante()  #Se llama a la función en utilidades para crear Estudiante
                elif op2=="2": utilidades.eliminarEstudianteTotalmente()    #Se llama a la función en utilidades para Eliminar estudiante totalmente
                else: print("Saliendo al menu principal")

            elif op == "2":  # Opciones Instructores
                print("\nMenú de gestión de Instructores")
                print("1. Agregar Instructores")
                print("2. Resumen de Instructores")
                print("0. Salir al menu principal")
                op2=input("Opción: ")   #Se pide opción
                if op2=="1": utilidades.crearInstructor()       #Se llama a la función de crear instructor en el modulo de utilidades
                elif op2=="2": utilidades.resumenInstructores()     #Se llama a la función de mostrar instructores en utilidades
                else: print("Saliendo al menú principal")

            elif op=="3":   #Opciones Curso
                print("\nMenú de gestión de cursos")
                print("1. Agregar curso")
                print("2. Cambiar instructor")
                print("3. Resumen cursos")
                print("4. Eliminar curso")
                print("0. Salir al menu principal")
                op2=input("Opción: ")   #Se pide opción

                if op2=="1": utilidades.crearCurso()        #Se llama a la función de crear curso en utilidades
                elif op2=="2": utilidades.cambio_instructor()   #Se llama a la función de cambiar instructor en utilidades
                elif op2=="3": utilidades.resumenCursos()   #Se llama a la función de resumir curso en utilidades
                elif op2=="4": utilidades.eliminarCurso()   #Se llama a la función de eliminar curso en utilidades
                else: print("Saliendo al menú principal")
            elif op == "0":
                break
            else:
                print("❌ Opción inválida.")

    # Menú Principal
    def menu_principal(self):
        acceso='Trafico pesado'
        while True:
            # Lista de opciones del menú principal
            print("\n--- Menú Principal ---")
            print("1. Iniciar Sesión")
            print("2. Portal Administrativo")
            print("0. Salir")
            op = input("Opción: ") # Ingreso de opción
            if op == "1":  # Registrar estudiante
                if len(estudiantesBaseDatos)==0 and len(instructoresBaseDatos)==0:  #Comprobar que ya existas al menos un usuario creado
                    print("Se ha detectado que el sistema es nuevo")
                    print("Primero espera que tu organización cree cada usuario")
                else:
                    print("\nPara poder ingresar, solamente necesitas tu ID !!")    
                    id=utilidades.comprobacion_num("id personal")       #Llamar comprobación de id
                    if id in estudiantesBaseDatos:
                        self.menu_estudiante(estudiantesBaseDatos[id])  #Identificar si es estudiante o catedrático y llamar al menú correspondiente
                    elif id in instructoresBaseDatos:
                        self.menu_catedratico(instructoresBaseDatos[id])

            elif op=="2":       #Ingreso al protal 'administrativo' 
                print("La contraseña es 'Trafico pesado'") #Para ingresar aquí se necesita una contraseña
                contra=input("Ingresa la contraseña ultra secreta: ")
                if contra==acceso:
                    self.menu_administrativo()      #Se llama al menú administrativo
                else:
                    print("❌ Contraseña incorrecta")

            elif op == "0":  # Opción para salir del programa
                print("📥 Guardando los datos")
                utilidades.guardar_datos() #Función para guardar los datos modificados en la sesión
                print("👋 Saliendo del sistema...")
                break
            else: # Ingreso de opción fuera de rango de opciones del menú
                print("❌ Opción inválida.")

#Iniciar el menu
if __name__ == "__main__":
    m = Menus()
    utilidades.cargarDatos() #Función para cargar datos ya guardados
    m.menu_principal()