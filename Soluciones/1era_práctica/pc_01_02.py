"""
-El nombre del entorno virtual tendrá el nombre con la siguiente estructura
 (apellido_nombre_edad)
-Instalar las siguientes librerías: Django: 5.0.6, fastapi: 0.112.0, numpy: 2.0.0 y
 aws (última versión)
-Generar el archivo de requirements.txt (mostrar las librerías instaladas)
-Caso: Reporte de calificaciones:
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

mate = 17
ciencia = 14
historia = 15

p_1 = mate * 0.4
p_2 = ciencia * 0.3
p_3 = historia * 0.3

nota_final = p_1 + p_2 + p_3

print("La nota final es: {:.1f}".format(nota_final))

if nota_final >= 13.0:
    print("¿Aprobado?:", True)

if nota_final < 13.0:
    print("¿Aprobado?:", False)

#(opcional - ternario)
#estado = "Aprobado" if nota_final >= 13.0 else "Desaprobado"

if nota_final >= 13.0:
    estado = "Aprobado"
else:
    estado = "Desaprobado"

print("El estudiante obtuvo una nota final de {} y su estado final es: {}".format(nota_final,estado))

