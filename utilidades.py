import pickle   #Importación de pickle, módulo para la persistencia de datos guardando directamente los diccionarios sin necesidad
#serializar los datos, mucho más sencillo para nuestro caso ya que no se debe exportar ningun dato

# función para crear Estudiante
import clase_usuario
import clase_curso

def comprobar_vacio(texto):     #Función para comprobar que los datos ingresados no esten vacios
    while texto=="":
        print("No puedes dejar este espacio en blanco")
        texto=input("Ingresalo de nuevo: ")
    return texto

def comprobacion_num(tipo):     #Para la comprobación de numeros trabajaremos con funciones anidadas
    def validar_edad(n):        #Validación de edad
        if 0 < n < 100:         #La edad debe estar entre 0 y 100
            return True
        raise ValueError("La edad debe estar entre 1 y 99")

    def validar_id(n):          #Validación de id
        if 10000 <= n <= 99999:         #debe tener 5 digitos
            if n in clase_usuario.estudiantesBaseDatos or n in clase_usuario.instructoresBaseDatos: #No debe estar entre los usuarios ya creados
                raise ValueError("Ese ID ya se encuentra en uso")
            return True
        raise ValueError("El ID debe tener 5 dígitos")

    def validar_capacidad(n):   #Validación de capacidad
        if n > 0:               #Debe ser mayor a 0
            return True
        raise ValueError("La capacidad debe ser mayor que 0")

    def validar_codigo(n):          #Validación de código
        if 10000 <= n <= 99999:         #Debe tener 5 dígitos
            if n in clase_curso.cursosBaseDatos:    #No debe repetirse con los curso ya creados
                raise ValueError("Ese código ya se encuentra en uso")
            return True
        raise ValueError("El código debe tener 5 dígitos")

    def validar_id_instructor(n):       #Validación de id de instructor
        if 10000 <= n <= 99999 and n in clase_usuario.instructoresBaseDatos:    #Debe tener 5 digitos y estar en la base de instructors
            return True
        raise ValueError("ID no válido para instructor")
    
    def validar_id_estudiante(n):       #Validación de id de estudiante
        if 10000 <= n <= 99999 and n in clase_usuario.estudiantesBaseDatos:    #Debe tener 5 digitos y estar en la base de instructors
            return True
        raise ValueError("ID no válido para instructor")
    
    def validar_id_general(n):
        if 10000 <= n <= 99999 and (n in clase_usuario.instructoresBaseDatos or n in clase_usuario.estudiantesBaseDatos):    #Debe tener 5 digitos y estar en la base de instructors
            return True
        raise ValueError("ID no no encontrado")

    def validar_codigo_curso(n):        #Validación de id para codigo de curso
        if 10000 <= n <= 99999 and n in clase_curso.cursosBaseDatos:    #Debe tener 5 digitos y estar en la bas de datos de curso
            return True
        raise ValueError("Código de curso no válido")

    validaciones = {        #diccionario, con las funciones anidas y el tipo que se ingresa para después llamarla
        "edad": validar_edad,
        "id": validar_id,
        "capacidad": validar_capacidad,
        "codigo": validar_codigo,
        "Id Instructor": validar_id_instructor,
        "Id Estudiante": validar_id_estudiante,
        "codigo del curso": validar_codigo_curso,
        "id personal":validar_id_general
    }

    while True:         
        try:
            numero = int(input(f"Ingresa el/la {tipo}: "))  #Se pide el numero
            if validaciones[tipo](numero):  #Se llama a la validación indicada
                return numero
        except ValueError as e:     #Manejo de errores
            print("ERROR:", e)
        except KeyError:
            print("ERROR: Tipo no reconocido")
            return None

def comprobacion_correo(correo):    #Función para comprobar correo
    while correo=="" or ("@" not in correo or ".com" not in correo):    #El correo debe incluir @ .com
        print("Correo no valido")
        correo=input("Ingresalo de nuevo: ")
    return correo

def resumenCursos():    #Función para mostrar todoso los cursos existentes
    if len(clase_curso.cursosBaseDatos)==0:     #Comprobar que ya existan cursos
        print ("ERROR: No existen cursos disponibles")
        return False
    else:
        for clave, valor in clase_curso.cursosBaseDatos.items():        #Mostrar todos los cursos disponibles
            print(f"{clave} - {valor.resumen()}")
        return True

def resumenInstructores():  #Función para mostrar todos los instructores existentes
    if len(clase_usuario.instructoresBaseDatos)==0:       #Comprobar que exista algun Instructor ya
        print ("ERROR: Primero debes crear un instructor")
    else:
        print("\nEscribe el id, del instructor a asignar")
        for clave, valor in clase_usuario.instructoresBaseDatos.items():    #Imprimir todos ls instructores existentes
            print(f"{clave} - {valor.resumen()}")
    
def cursosInstructores(instructor):
    i=0
    print("\n📘 Tus cursos:")
    for clave, valor in clase_curso.cursosBaseDatos.items():        #Mostrar todos los cursos disponibles
        if valor.getInstructor().getId() == instructor.getId():                 #Comprobar que el instructor es el mismo
            print(f"{clave} - {valor.resumen()}")
            i+=1
    if i==0:        #Mostrar un error si no tiene asignado ningun curso
        print("ERROR: No tienes agregado ningun curso")
        return False
    else:
        curso=clase_curso.cursosBaseDatos[comprobacion_num("codigo del curso")] #Si tiene algun curso, pedir el codigo
        return curso    #Retornar el curso

def crearEstudiante():      #Función para crear una nueva instancia de estudiante
    print("\n---Ingresa los datos del nuevo estudiante---")     #Se piden los datos
    nombre=input("Ingresa el nombre: ")         # Y se llaman a las comprobaciones necesarias
    nombre=comprobar_vacio(nombre)
    edad=comprobacion_num("edad")
    print("Recuerda el Id debe ser único y tener 5 dígitos")
    ident=comprobacion_num("id")
    correo=input("Ingresa el correo: ")
    correo=comprobacion_correo(correo)
    carrera=input("Ingresa la carrera: ")
    carrera=comprobar_vacio(carrera)

    print("Gracias por los datos")
    estudiante=clase_usuario.Estudiante(nombre, edad, ident, correo, carrera)   #Se crea la instancia
    print(estudiante)       #Se imprime un resumen de la instancia creada

def eliminarEstudianteTotalmente():    #Para realizar esto ya debe haverse identificado y por eso se pide a estudiantes
    if len(clase_usuario.estudiantesBaseDatos)>0:
        print("Estudiantes disponibles")
        for clave, valor in clase_usuario.estudiantesBaseDatos.items():
            print(f"{clave} - {valor.resumen()}")
        estudiante=clase_usuario.estudiantesBaseDatos[comprobacion_num("Id Estudiante")]
        print("\nSe eliminará al siguiente estudiante")
        print(estudiante)      #Se muestra un resumen del estudiante
        opcion=input("Escribe 'si' para confirmarlo o 'no' para salir: ")       #Se confirma
        if opcion=='si':
            print("\nEliminado al estudiante de los siguientes cursos")
            for clave, valor in clase_curso.cursosBaseDatos.items():    #Se recorren todos los cursos existentes
                if estudiante.getId() in valor.getEstudiantes():    #Se comprueba si el estudiante ya está inscrito en alguno
                    print(f"{clave} - {valor.resumen()}")
                    valor.elimarEstudiantes(estudiante)           
            print("Eliminando de la base de datos")
            del clase_usuario.estudiantesBaseDatos[estudiante.getId()]
            print("\nEstudiante eliminado del sistema 🤖")
            return
        else:
            print("\nSaliendo al menu principal")
            return
    else:
        print("ERROR: Primero debes crear un estudiante")

def crearInstructor():      #Función para crear una nueva instancia de  instructor
    print("\n---Ingresa los datos del nuevo instructor---")     #Se piden los datos y se realizan las comprobaciones necesarias
    nombre=input("Ingresa el nombre: ")
    nombre=comprobar_vacio(nombre)
    edad=comprobacion_num("edad")
    print("Recuerda el Id debe ser único y tener 5 dígitos")
    ident=comprobacion_num("id")
    correo=input("Ingresa el correo: ")
    correo=comprobacion_correo(correo)
    profesion=input("Ingresa la profesión o especialidad: ")
    profesion=comprobar_vacio(profesion)

    print("Gracias por los datos")
    instructor=clase_usuario.Instructor(nombre, edad, ident, correo, profesion) #Se crea la instancia
    print("Informe de instructor creado")
    print(instructor)   #Se muestra un resumen de la instancia de instructor creada

def crearCurso():       #Función para crear curso
    print("\n---Ingresa los datos del curso nuevo---")  #Se piden los datos y se realizan las comprobaciones necesarias
    nombre=input("Ingresa el nombre del curso: ")
    nombre=comprobar_vacio(nombre)
    capacidad=comprobacion_num("capacidad")
    print("Recuerda el código debe ser único y tener 5 dígitos")
    codigo=comprobacion_num("codigo")
    aula=input("Ingresa el aula: ")
    aula=comprobar_vacio(aula)
    print("Ahora debes ingresar un instructor, si no lo has creado escribe 'salir' para hacerlo primero u otra tecla para seguir")
    opcion=input("¿Deseas salir?: ")    #Preguntar si desean continuar o salir

    if opcion =="salir":    
        return
    else:
        resumenInstructores()
        instructor=comprobacion_num("Id Instructor")      #Comprobar validez de este codigo ingresado
    print("Gracias por todos los datos")
    curso=clase_curso.Curso(nombre, capacidad, codigo, aula, clase_usuario.instructoresBaseDatos[instructor])   #Crear instancia de curso
    print("Resumen del curso creado")
    curso.infoCurso()   #Imprimir un resumen del curso creado

def cambio_instructor():    #Función para cambiar el instructor de algun curso
    print("\nBienvenido al cambio de Instructor")
    if resumenCursos()==True: #Se llama a la función resumen cursos
        curso=clase_curso.cursosBaseDatos[comprobacion_num("codigo del curso")] #Ingreso del curso al que se asignará
        instructorActual=curso.getInstructor()
        if len(clase_usuario.instructoresBaseDatos)<2: print ("ERROR: No existen suficientes instructores") #Comprobar que ya existan cursos
        else:
            resumenInstructores()   #Se llama a la función para mostrar instructores disponibles
            instructorNuevo=clase_usuario.instructoresBaseDatos[comprobacion_num("Id Instructor")]
            if instructorActual==instructorNuevo:  print("ERROR: Debe ser un instructor diferente") #Comprobar que el instructor sea diferente
            else: curso.setInstructor(instructorNuevo)
    else: return

def agregar_estudiante(estudiante):             #Para realizar esto ya debe haverse identificado y por eso se pide a estudiantes
    print("\nBienvenido a la asignación de cursos")
    resumenCursos()     #Se llama a la función para msotrar todos los cursos
    curso=clase_curso.cursosBaseDatos[comprobacion_num("codigo del curso")] #Ingreso del curso al que se asignará
    
    print("Te asignaras al siguiente curso")        #Mostrar resumen del curso al que se asignará
    curso.infoCurso()
    opcion=input("Escribe 'si' para confirmarlo o 'no' para salir: ")       #Confirmación
    if opcion=='si':
        curso.agregarEstudiante(estudiante) #Se llama al método para agregar al estudiante
        print("Agregado exitosamente")
        return
    else:
        print("Saliendo al menu principal")
        return
    
def mostrar_inscritos(curso):
    if len(curso.getEstudiantes())==0:       #Comprobar que exista algun estudiante inscrito
        print (f"\nNo hay estudiantes incritos en el curso {curso.getNombre()} ({curso.getCodigo()})")
    else:
        print(f"\n👥 Estudiantes incritos al curso {curso.getNombre()} ({curso.getCodigo()})")
        for clave, valor in curso.getEstudiantes().items(): #Con un for recorrer todos los estudiantes inscritos
            print(f"{clave} - {valor.resumen()}")   #Imprimir los estudiantes
    
def eliminarEstudiante(estudiante):    #Para realizar esto ya debe haverse identificado y por eso se pide a estudiantes
    print("\nBienvenido a la plataforma de retiro académico")
    i=0
    for clave, valor in clase_curso.cursosBaseDatos.items():    #Se recorren todos los cursos existentes
        if estudiante.getId() in valor.getEstudiantes():    #Se comprueba si el estudiante ya está inscrito en alguno
            print(f"{clave} - {valor.resumen()}")           
            i+=1
    if i==0: 
        print ("ERROR: No estás inscrito a ningun curso")   #Si no está inscrito, se lanza error
        return
    else:
        curso=clase_curso.cursosBaseDatos[comprobacion_num("codigo del curso")]     #Se toma el código del curso a desasignar
        print("Te retiras del siguiente curso")
        curso.infoCurso()       #Se muestra un resumen del curso
        opcion=input("Escribe 'si' para confirmarlo o 'no' para salir: ")       #Se confirma
        if opcion=='si':
            curso.eliminarEstudiante(estudiante)   #Se llama al método para eliminar el estudiante
            print("Eliminado exitosamente")
            return
        else:
            print("Saliendo al menu principal")
            return
    
def eliminarCurso():
    print("\nBienvenido a la papelera de cursos")
    if resumenCursos()==True:      #Se llama a la función resumen Instructores
        curso=clase_curso.cursosBaseDatos[comprobacion_num("codigo del curso")]
        print("\nSe eliminará el siguiente curso")
        curso.infoCurso()
        opcion=input("Escribe 'si' para confirmarlo o 'no' para salir: ")       #Se confirma
        if opcion=='si':
            del clase_curso.cursosBaseDatos[curso.getCodigo()]
            print("\nCurso eliminado del sistema 🤖")   #Se elimina el curso de la base de datos
            return
        else:
            print("Saliendo al menu principal")
            return
    else: 
        return

def guardar_datos():
    with open("estudiantes.pkl", "wb") as f:    #Guardar el diccionario "estudiantesBaseDatos" en un archivo .pkl para no perder datos
        pickle.dump(clase_usuario.estudiantesBaseDatos, f)
    with open("instructores.pkl", "wb") as f:    #Guardar el diccionario "instructoresBaseDatos" en un archivo .pkl para no perder datos
        pickle.dump(clase_usuario.instructoresBaseDatos, f)
    with open("cursos.pkl", "wb") as f:          #Guardar el diccionario "cursosBaseDatos" en un archivo .pkl para no perder datos
        pickle.dump(clase_curso.cursosBaseDatos, f)

def cargarDatos():
    print("📤 Cargando datos del sistema.")

    # Cargar estudiantes
    try:
        with open("estudiantes.pkl", "rb") as f:    #Tratar de abrir el archivo
            clase_usuario.estudiantesBaseDatos = pickle.load(f) #Importar los datos del archivo al diccionario de estudiantes
        print(f"✅ Estudiantes cargados: {len(clase_usuario.estudiantesBaseDatos)}")
    except FileNotFoundError:       #Manejo de erro si no se encuentra el archivo
        print("No existen datos guardados para estudiantes")

    # Cargar instructores
    try:
        with open("instructores.pkl", "rb") as f:
            clase_usuario.instructoresBaseDatos = pickle.load(f) #Importar los datos del archivo al diccionario de instructores
        print(f"✅ Instructores cargados: {len(clase_usuario.instructoresBaseDatos)}")
    except FileNotFoundError:   #Manejo de erro si no se encuentra el archivo
        print("No existen datos guardados para instructores")

    # Cargar cursos
    try:
        with open("cursos.pkl", "rb") as f:
            clase_curso.cursosBaseDatos = pickle.load(f) #Importar los datos del archivo al diccionario de cursos
        print(f"✅ Cursos cargados: {len(clase_curso.cursosBaseDatos)}")
    except FileNotFoundError:   #Manejo de erro si no se encuentra el archivo
        print("No existen datos guardados para cursos")
