"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos)
Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía para un
usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
salario, según corresponda.
"""
from selectors import SelectSelector

nombre="Bilha"
salario=4500
edad="19"
compañia="Amazon"

#Tipos
print(f"La variable nombre es de tipo: {type(nombre)}")
print(f"La variable salario es de tipo: {type(salario)}")
print(f"La variable edad es de tipo: {type(edad)}")
print(f"La variable compañia es de tipo:{type(compañia)}")

#Conversión de string a int
edad=int(edad)

#Condicional
if edad>30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    bono_final=(salario**2)+(0.1*salario)
    print(f"El bono final es: {bono_final}")
else:
    print("Usted tiene un bono del 5% en el mes diciembre")
    bono_final=(salario**2)+(0.05*salario)
    print(f"El bono final es: {bono_final}")


