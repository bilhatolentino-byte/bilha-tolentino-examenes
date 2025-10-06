"""
1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:

• Clase base Persona
o Atributos: nombre, edad, nacionalidad="peruana", saldo=0.0.
o Métodos para esta clase:
▪ actualizar_nombre(nombre) y actualizar_edad(edad)
(validar edad > 0).
▪ cumplir_anios() (incrementa edad en 1).
▪ mostrar_saldo() (imprime el saldo actual).
▪ transferir(destino, monto) (si no hay fondos
suficientes, imprimir “Saldo insuficiente”; si hay,
basarse en self y acreditar a destino).
• Crear la clase que hereda: Empleado(Persona)
o Atributo adicional: sueldo (float).
o Métodos para esta clase:
▪ aumento_sueldo(porcentaje=0.30) (incrementa el
sueldo en 30% por defecto).
▪ prediccion(anio_objetivo, edad_param=None)
▪ Retorna el mensaje: “En el año XXXX tendrá
XX años”.
▪ Si edad_param se pasa y es menor que
self.edad, imprimir “No es posible realizar la
operación” y no calcular.

• Pruebas mínimas
o Instanciar al menos dos Empleado.
o Aplicar aumento_sueldo 2 veces y mostrar el sueldo
incrementado.
o Realizar una transferencia entre ambos empleados y mostrar
saldos antes y después de ambos

o Probar un caso de saldo insuficiente.
o Usar prediccion(...) con y sin edad_param inválido.
"""
class Persona:
    def __init__(self, nombre, edad, nacionalidad="peruana", saldo=0.0):
        self.nombre = nombre
        self.edad = edad if edad > 0 else 1
        self.nacionalidad = nacionalidad
        self.saldo = saldo

    def cumplir_anios(self):
        self.edad += 1

    def mostrar_saldo(self):
        print(f"{self.nombre}: S/{self.saldo:.2f}")

    def transferir(self, destino, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            destino.saldo += monto
            print(f"{self.nombre} transfirió S/{monto} a {destino.nombre}")
        else:
            print("Saldo insuficiente")


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo, saldo=0.0):
        super().__init__(nombre, edad, saldo=saldo)
        self.sueldo = sueldo

    def aumento_sueldo(self, porcentaje=0.30):
        self.sueldo *= (1 + porcentaje)

    def prediccion(self, anio, edad_param=None):
        actual = 2025
        if edad_param and edad_param < self.edad:
            print("No es posible realizar la operación")
        else:
            futura = edad_param if edad_param else self.edad + (anio - actual)
            print(f"En el año {anio} tendrá {futura} años")


# ---- Pruebas ----
e1 = Empleado("Juan", 25, 2000, 1000)
e2 = Empleado("Monica", 30, 2500, 500)

e1.aumento_sueldo()
e1.aumento_sueldo()
e1.transferir(e2, 300)
e2.transferir(e1, 2000)
e1.prediccion(2030)
e2.prediccion(2030, 20)
e2.prediccion(2030, 35)