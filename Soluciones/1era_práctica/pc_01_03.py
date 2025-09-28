"""
-Caso: Calculadora de propinas
 Crea un programa que permita ingresar el total de una cuenta en un restaurante,
 el porcentaje de propina que desea dejar el cliente y el número de personas que
 dividirán la cuenta. El programa debe mostrar:
 El monto total con propina.
 El monto que debe pagar cada persona (con 2 decimales).
 Un mensaje será personalizado, indicará si el monto individual supera los 100
 soles, mostrando un mensaje de advertencia si es el caso.
 Entrada esperada (por input):
 Total de la cuenta: float
 Porcentaje de propina: float
 Número de personas: int
 Salida ejemplo (output):
 Monto total con propina: S/. 230.00
 Cada persona debe pagar: S/. 115.00
 ¡Advertencia! El monto por persona supera los S/. 100

"""

total_cuenta = 1200
print("Total de la cuenta S/: {}".format(total_cuenta))
porcentaje_propina = 10
print("Porcentaje de propina (%): {}".format(porcentaje_propina))
numero_personas = 8
print("Número de personas: {}".format(numero_personas))

propina = total_cuenta * (porcentaje_propina / 100)
total_propina = total_cuenta + propina
monto_persona = total_propina / numero_personas

print("Monto total a pagar con propina: S/. {}".format(total_propina))
print("Cada persona debe realizar el pago de S/. {}".format(monto_persona))

if monto_persona > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")