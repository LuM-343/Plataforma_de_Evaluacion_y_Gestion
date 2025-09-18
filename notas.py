# ==============================
# MÓDULO: notas.py
# ==============================

# Función para mostrar las calificaciones del estudiante por curso
def mostrar_calificaciones(curso): # Se toma como parámetro al curso
    # Verificación de evaluaciones dentro del curso
    if not curso.getEvaluaciones():
        print(f"\n⚠️ No hay evaluaciones creadas en {curso.getNombre()}")
        return

    # Si hay, recorre las evaluaciones mostrando el tipo, nombre y ponderación de la misma
    print(f"\n📘 Calificaciones del curso {curso.getNombre()}")
    for ev in curso.getEvaluaciones():
        print(f"  {ev.tipo()} '{ev.nombre}' ({ev.ponderacion*100:.0f}%)")
        # Verifica si no hay estudiantes
        if not curso.getEstudiantes():
            print("    ⚠️ No hay estudiantes inscritos en este curso.")
        else:
            # Muestra las notas de cada estudiante por la evaluación
            for id_est, est in curso.getEstudiantes().items():
                nota = ev.obtener_nota(id_est)
                print(f"    {est.getId()}-{est.getNombre()}: {nota if nota is not None else 'Sin nota'}") # Muestra la nota si existe, o 'Sin nota' si no se le asignó

# Función para crear reportes para estudiantes con promedio bajos
def reporte_promedios_bajos(curso, limite=60): # Compara el límite de 60 puntos en las notas de 'curso'
    # Verifica si hay evaluaciones
    if not curso.getEvaluaciones():
        print(f"\n⚠️ No hay evaluaciones en {curso.getNombre()}, no se puede calcular promedio.")
        return
    # Verifica si hay estudiantes 
    if not curso.getEstudiantes():
        print(f"\n⚠️ No hay estudiantes inscritos en {curso.getNombre()}.")
        return

    print(f"\n📊 Promedios bajos en {curso.getNombre()} (< {limite})")
    encontrado = False # Variable para controlar la búsqueda de estudiantes con promedio bajo
    # Recorreo los estudiantes y calcula los promedios
    for id_est, est in curso.getEstudiantes().items():
        prom = curso.promedio_estudiante(id_est) # Se calcula el promedio ponderado en base a sus evaluaciones
        # Si el promedio existe y es menor al límite (60) se crea reporte
        if prom is not None and prom < limite:
            print(f"  ⚠️ {est.getNombre()}: {prom:.2f}")
            encontrado = True
    # Si no se encuentran estudiantes con promedios bajos no crea el reporte
    if not encontrado:
        print("✅ Ningún estudiante tiene promedio bajo.")