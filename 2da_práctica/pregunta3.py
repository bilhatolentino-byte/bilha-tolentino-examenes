"""
3. Crea un programa en Python que implemente una función llamada
convertir_precio(texto: str) -> float que (4 ptos):
1. Reciba un string que representa un precio en soles (ejemplo: "123.50",
"45", "20.99").
2. Intente convertirlo a un número decimal (float).
3. Tenga las siguientes excepciones:
o Si el texto está vacío, debe lanzar un ValueError("El precio no
puede estar vacío").
o Si el texto contiene caracteres inválidos (ejemplo: "abc",

"12a3"), debe lanzar un ValueError("Formato de precio inválido").
o Si el número es negativo, debe lanzar un ValueError("El precio no
puede ser negativo").
- El programa debe pedir tres precios al usuario, usar la función
convertir_precio y almacenarlos en una lista.
- Finalmente, mostrar:
o La lista con los precios convertidos.
o El precio promedio de los tres valores ingresados.
"""



def convertir_precio(texto: str) -> float:
    try:

        precio = float(texto)
        return precio
    except ValueError:

        print("Error: El texto ingresado no es un precio válido.")
        return None

entrada = input("Ingresa un precio en soles: ")
resultado = convertir_precio(entrada)

if resultado is not None:
    print(f"El precio convertido es: {resultado}")

