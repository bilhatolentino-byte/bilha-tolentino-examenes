"""
Reglas:
- El nombre del entorno virtual tendrá el nombre con la siguiente estructura
(apellido_nombre_edad)
- Instalar las siguientes librerías: Django: 5.0.6, fastapi: 0.112.0, numpy: 2.0.0 y
aws (última versión)
- Generar el archivo de requirements.txt (mostrar las librerías instaladas)
- Caso: Reporte de calificaciones:
Se tiene un alumno con calificaciones en tres cursos:
Matemáticas: 17, Ciencia: 14, Historia: 15
Cada curso tiene un peso diferente en la nota final:
Matemáticas: 40%, Ciencia: 30%, Historia: 30%
Realizar lo que se pide a continuación:
Calcula la nota final ponderada del alumno.
Muestra un mensaje como: "La nota final es: 15.6" con 1 decimal.
Evalúa si el alumno aprueba (nota final >= 13.0). Muestra un mensaje booleano:
"¿Aprobado?: True" o "¿Aprobado?: Sí"
Genera una cadena resumen que diga:
"El estudiante obtuvo una nota final de 15.6 y su estado final es: Aprobado"
En caso no apruebe indicar lo contrario en los mensajes.
"""
#CASO
nota_mate=17
nota_ciencia=14
nota_historia=15

nota_final=0.4*nota_mate+0.3*nota_ciencia+0.3*nota_historia
print(f"La nota final es: {nota_final:.1f}")

if nota_final >= 13.0:
    print("¿Aprobado?: Sí")
    print(f"El estudiante obtuvo una nota final de {nota_final:.1f} y su estado final es: Aprobado")

elif nota_final <13:
    print(f"¿Aprobado?: No")
    print(f"El estudiante obtuvo una nota final de {nota_final:.1f} y su estado final es: Desaprobado")
