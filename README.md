# Proyecto No. 1 PLATAFORMA DE GESTIÓN Y EVALUACIÓN DE CURSOS ONLINE

## Integrantes

* Velásquez González Luis Manuel – 1502325
* Pelaez Virula Moshé Arenz – 1556425

## Descripción

En este proyecto se desarrollo un sistema capaz de gestionar evaluaciones de cursos online, integrando accesos de instructores, estudiantes y administración. 
En el que cada uno puede realizar diferentes gestiones, se busco crear un proyecto robusto que no tan fácil falle y que llegué a ser amigable con los usuarios.


El sistema:

* Crear usuario para estudiantes e instructores
* Crear cursos nuevos
* Asignación a cursos por parte de los estudiantes
* Ver resumenes utiles para estudiantes, instructores y administrativos
* Desasignación de curso desde estudiantes
* Creación de actividades, implementación de notas y promedio de parte de Instructor
* Eliminación de estudiantes y cursos desde el portal administrativo
* Poder consultar datos guardados en sesión anteriores

El trabajo se organizó con roles de equipo para fomentar la colaboración, el uso de GitHub y las buenas prácticas de programación en Python.


## Instrucciones de uso

1. Clonar el repositorio

   ```
   git clone https://github.com/LuM-343/Plataforma_de_Evaluacion_y_Gestion
   cd Plataforma_de_Evaluacion_y_Gestion
   ```

2. Ejecutar el juego
   Asegúrate de tener Python instalado y ejecuta el siguiente archivo:

   ```
   python main.py
   ```


3. Menú principal
   Al iniciar el programa, se mostrará un menú con opciones:

   * `1) Iniciar Sesión` → Acceso a opciones y gestiones de estudiantes e instructores segun ID 
   * `2) Portal Administrativo` → Acceso aopciones y funciones unicas de administración, se debe ingresar una contraseña por seguridad. Esta es "Trafico pesado"
   * `0) Salir` → Se sale del programa y se guardan todos los datos de la sesión

     
4. Menú Catedrático
   Si se detecta que el ID es de instructor desde el menú principal llegarás a este menú
   * `---Menú Catedrático (Nombre del catedrático)---`
   * `1) Crear evaluación` → Crear evaluación de  curso del que es responsable el catedrático (Se necesita ingresar nombre, ponderacion y tiempo/fecha por cada evaluación)
   * `2) Registrar calificación` → De las evaluaciones ya creadas en los cursos del instructor podrá asginar un punteo a cada estudiante (Se necesita tener una evaluación creada)
   * `3) Ver calificaciones` → De los cursos a su cargo, el instructor puede ver un resumen de las calificaciones ingresadas por curso.
   * `4) Reporte promedios bajos` → De los cursos a su cargo, el instructor puede ver un reporte de los estudiantes con bajo rendimiento, dividido por curso.
   * `5) Estudiantes Inscritos` → De los cursos a su cargo, el instructor puede ver todos los estudiantes asignados por curso.
   * `0) Salir` → Se cierra la sesión del catedrático y se regresa al menú principal

  
5. Menú Estudiante
   Si se detecta que el ID es de estudiante desde el inisión de sesión, se enviará a este menú
   * `---Menú Estudiante (Nombre del estudiante)---`
   * `1) Asignación de cursos` → El estudiante puede asignarse a cada uno de los cursos creados, siempre y cuando no haya superado su capacidad, solo debe ingresar el código del curso.
   * `2) Retiro académico` → Se le da la oportunidad al estudiante de retirarse de los cursos a los que ya esta inscrito, solo debe ingresar el código de este curso.
   * `3) Ver cursos inscritos` → Se despliega un resumen de todos los cursos de los que forma parte el estudiante
   * `4) Ver calificaciones` → Puede ver la calificación ingresada por el profesor y un promedio del curso, esto por cada curso de los que forma parte el estudiante.
   * `0) Salir` → Se cierra la sesión del estudiante y se regresa al menú principal

  
6. Menú Administrarivo
   Si se coloca la contraseña correcta en la opción 2 del menú principal es dirigido a este menú.
   * `---Menú Administrativo---`
   * `1) Estudiante` → Administración de estudiantes
      * `1) Agregar Estudiante` → Agregar un nuevo estudiante al sistema (se necesita el id, nombre, edad, correo, carrera del nuevo estudiante)
      * `2) Eliminar estudiante de todo el sistema` → Elimina el estudiante de todas las bases de datos (se necesita el id del estudiante a eliminar)
      * `0) Salir al menú principal` → Se regresa al menú administrativo
        
   * `2) Instructores` → Administración de instructores
      * `1) Agregar Instructores` → Agregar un nuevo instructor al sistema (se necesita el id, nombre, edad, correo, profesión del nuevo instructor)
      * `2) Resumen de Instructores` → Se despliega un resumen de todos los instructores existentes.
      * `0) Salir al menú principal` → Se regresa al menú administrativo
   * `3) Cursos` → Administración de cursos
      * `1) Agregar curso` → Agregar un nuevo curso al sistema (se necesita el código, nombre, capacidad, aula e instructor del nuevo curso)
      * `2) Cambiar Instructor` → Se puede cambiar el instructor de un curso (se necesita código del curso y id del nuevo instructor)
      * `3) Resumen de cursos` → Se despliega un resumen de todos los cursos existentes.
      * `4) Eliminar curso` → Elimina el curso de todas las bases de datos (se necesita el código del curso a eliminar)
      * `5) Listado de Estudiantes de un Curso` → Se muestran todos los estudiantes asignados a un curso (se necesita el código del curso a ver).
      * `0) Salir al menú principal` → Se regresa al menú administrativo
   * `0) Salir` → Se cierra la sesión administrativa y se regresa al menú principal

