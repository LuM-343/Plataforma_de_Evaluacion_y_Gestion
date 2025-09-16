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
                print(f"    {est.nombre}: {nota if nota is not None else 'Sin nota'}") # Muestra la nota si existe, o 'Sin nota' si no se le asignó