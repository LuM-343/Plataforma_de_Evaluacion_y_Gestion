# función para crear Estudiante
import clase_usuario
import clase_curso

def comprobar_vacio(texto):     #Función para comprobar que los datos ingresados no esten vacios
    while texto=="":
        print("No puedes dejar este espacio en blanco")
        texto=input("Ingresalo de nuevo: ")
    return texto

def comprobacion_num(tipo):     #Función para comrpobar validez de id y edad por tipo
    while True:
        numero=input(f"Ingresa el/la {tipo}: ")    #se pide el dato
        try:
            numero=int(numero)      #Se convierte a entero
            if (numero>0 and numero<100) and tipo=="edad":  #La edad debe ser mayor a cero y menor a 100
                return numero
            
            elif numero>9999 and numero<100000 and tipo=="id":      #El id debe tener 5 digitos
                if numero in clase_usuario.estudiantesBaseDatos or numero in clase_usuario.instructoresBaseDatos:   #El id no debe estar ya en la base de datos
                    raise ValueError ("Ese id ya se encuentra en uso")  #Manejo de errores
                return numero
            
            elif numero>0 and tipo=="capacidad":        #La capacidad debe ser mayor a 0
                return numero
            
            elif numero>9999 and numero<100000 and tipo=="codigo":      #El codigo debe tener 5 digitos
                if numero in clase_curso.cursosBaseDatos:                   #El id no debe estar ya en la base de datos
                    raise ValueError ("Ese codigo ya se encuentra en uso")  #Manejo de errores
                return numero
            
            elif numero>9999 and numero<100000 and tipo=="Id Instructor":   #Comprobar que el id tenga 5 digitos
                if numero in clase_usuario.instructoresBaseDatos:           #Comrpobar que ya se encuentre en la base de datos
                    return numero
                else:
                    raise ValueError("Id no válido para instructor")
                
            else:
                raise ValueError ("Número ingresado no válido, intenta de nuevo")
        except ValueError as e:
            print("ERROR", e)

def comprobacion_correo(correo):    #Función para comprobar correo
    while correo=="" or ("@" not in correo or ".com" not in correo):    #El correo debe incluir @ .com
        print("Correo no valido")
        correo=input("Ingresalo de nuevo: ")
    return correo
    
def crearEstudiante():      #Función para crear una nueva instancia de estudiante
    print("\n---Ingresa los datos del nuevo estudiante---")     #Se piden los datos
    nombre=input("Ingresa tu nombre: ")         # Y se llaman a las comprobaciones necesarias
    nombre=comprobar_vacio(nombre)
    edad=comprobacion_num("edad")
    print("Recuerda el Id debe ser único y tener 5 dígitos")
    ident=comprobacion_num("id")
    correo=input("Ingresa tu correo: ")
    correo=comprobacion_correo(correo)
    carrera=input("Ingresa tu carrera: ")
    carrera=comprobar_vacio(carrera)

    print("Gracias por los datos")
    estudiante=clase_usuario.Estudiante(nombre, edad, ident, correo, carrera)   #Se crea la instancia
    print(estudiante)       #Se imprime un resumen de la instancia creada

def crearInstructor():      #Función para crear una nueva instancia de  instructor
    print("\n---Ingresa los datos del nuevo instructor---")     #Se piden los datos y se realizan las comprobaciones necesarias
    nombre=input("Ingresa tu nombre: ")
    nombre=comprobar_vacio(nombre)
    edad=comprobacion_num("edad")
    print("Recuerda el Id debe ser único y tener 5 dígitos")
    ident=comprobacion_num("id")
    correo=input("Ingresa tu correo: ")
    correo=comprobacion_correo(correo)
    profesion=input("Ingresa tu profesión o especialidad: ")
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
    elif len(clase_usuario.instructoresBaseDatos)==0:       #Comprobar que exista algun Instructor ya
        print("Primero debes crear un instructor")
        return
    else:
        print("\nEscribe el id, del instructor a asignar")
        for clave, valor in clase_usuario.instructoresBaseDatos.items():    #Imprimir todos ls instructores existentes
            print(f"{clave} - {valor.resumen()}")
        instructor=comprobacion_num("\nId Instructor")      #Comprobar validez de este codigo ingresado
        
    print("Gracias por todos los datos")
    curso=clase_curso.Curso(nombre, capacidad, codigo, aula, clase_usuario.instructoresBaseDatos[instructor])   #Crear instancia de curso
    print("Resumen del curso creado")
    curso.infoCurso()   #Imprimir un resumen del curso creado

crearCurso()