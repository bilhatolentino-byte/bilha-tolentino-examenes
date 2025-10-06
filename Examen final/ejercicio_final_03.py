"""
3. (2 ptos) Crear un decorador conteo.
Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente al usuario.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada exitosamente.
- La función que vas a crear va a capturar, la edad, nombre de un alumno, la
hora y el minuto en que fue registrado (usar la librería correspondiente de
tiempo)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante.
"""
from datetime import datetime


def conteo(funcion):
    def wrapper(*args, **kwargs):
        cantidad = len(args) + len(kwargs)
        if cantidad <= 1:
            print("Debe ingresar más de un parámetro para continuar.")
            return
        resultado = funcion(*args, **kwargs)
        print(f"La función fue ejecutada exitosamente con {cantidad} parámetros.")
        return resultado
    return wrapper

def registrar_alumno(nombre, edad, nota1, nota2, nota3, nota4):
    ahora = datetime.now()
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"{nombre} de {edad} años ha sido registrado a las "
          f"{ahora.hour} horas con {ahora.minute} minutos.")
    print(f"Promedio del alumno: {promedio:.2f}")
    return promedio


funcion_decorada = conteo(registrar_alumno)


funcion_decorada("Pedro", 30, 15, 18, 12, 16)