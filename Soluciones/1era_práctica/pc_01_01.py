"""
-Asignar en variables los datos de tu nombre, salario, edad y compañía
 para un usuario e identificar sus tipos de variables
-Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse
 una conversión de datos
-Identificar si la edad es mayor a 30, mostrar un mensaje ingresado "Usted tiene
 un bono de 10% en el mes de diciembre" caso contrario mostrar "Usted tiene un bono del
 5% en el mes diciembre"
-Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10% de su salario,
 según corresponda

"""
#Primer paso: Asignamos las variables
nombre = "Melina"
salario = 9000
edad = "33"
empresa = "CERSEU"

print("Tipos de variables: ")
print("Nombre: {}".format(type(nombre)))
print("Salario: {}".format(type(salario)))
print("Edad: {}".format(type(edad)))
print("Compañía: {}".format(type(empresa)))

edad_int = int(edad)

if edad_int > 30:
    bono = 0.10
    print("Usted tiene un bono de 10% en el mes de diciembre, por tener la edad de {}".format(edad_int))

if edad_int < 30:
    bono = 0.05
    print("Usted tiene un bono del 5% en el mes de diciembre, por tener la edad de {}".format(edad_int))

#Ahora realizamos el cálculo final
p_s = salario ** 2
bono_extra = salario * bono
monto_final = p_s + bono_extra

print("El monto final que se va a obtener es: {}".format(monto_final))

