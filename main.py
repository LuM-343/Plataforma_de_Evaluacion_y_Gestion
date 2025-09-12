# función para crear Estudiante
import clase_usuario

def comprobar_vacio(texto):
    while texto=="":
        print("No puedes dejar este espacio en blanco")
        texto=input("Ingresalo de nuevo: ")
    return texto

def comprobacion_num(tipo):
    while True:
        numero=input(f"Ingresa tu {tipo}: ")
        try:
            numero=int(numero)
            if (numero>0 and numero<100) and tipo=="edad":
                return numero
            elif numero>9999 and numero<100000 and tipo=="id":
                if numero in clase_usuario.estudiantesBaseDatos or numero in clase_usuario.instructoresBaseDatos:
                    raise ValueError ("Ese id ya se encuentra en uso")
                return numero
            else:
                raise ValueError ("Número ingresado no válido, intenta de nuevo")
        except ValueError as e:
            print("ERROR", e)

def comprobacion_correo(correo):
    while correo=="" or ("@" not in correo or ".com" not in correo):
        print("Correo no valido")
        correo=input("Ingresalo de nuevo: ")
    return correo
    
def crearEstudiante():
    print("\n---Ingresa los datos del nuevo estudiante---")
    nombre=input("Ingresa tu nombre: ")
    nombre=comprobar_vacio(nombre)
    edad=comprobacion_num("edad")
    print("Recuerda el Id debe ser único y tener 5 dígitos")
    ident=comprobacion_num("id")
    correo=input("Ingresa tu correo: ")
    correo=comprobacion_correo(correo)
    carrera=input("Ingresa tu carrera: ")
    carrera=comprobar_vacio(carrera)

    print("Gracias por los datos")
    estudiante=clase_usuario.Estudiante(nombre, edad, ident, correo, carrera)
    print("Informe de estudiante creado")
    print(estudiante)

def crearInstructor():
    print("\n---Ingresa los datos del nuevo instructor---")
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
    instructor=clase_usuario.Instructor(nombre, edad, ident, correo, profesion)
    print("Informe de instructor creado")
    print(instructor)

#crearEstudiante()
crearInstructor()
print(clase_usuario.estudiantesBaseDatos)
print(clase_usuario.instructoresBaseDatos)