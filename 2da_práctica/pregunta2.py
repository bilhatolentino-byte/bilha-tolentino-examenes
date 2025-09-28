"""
2. Usando el concepto de funciones (3 ptos):
Reglas:
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso en el input de
datos)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original
"""


def normalizar_nombres(nombres):
    lista_normalizada = []

    for nombre in nombres:

        nombre = nombre.strip()

        partes = nombre.split()

        for parte in partes:

            normalizado = parte.title()
            lista_normalizada.append(normalizado)

    return lista_normalizada



nombres_original = []

print("Ingresa como mínimo 6 nombres:")
for i in range(6):
    nombre = input(f"Nombre {i + 1}: ")
    nombres_original.append(nombre)

resultado = normalizar_nombres(nombres_original)

print("\nLista original:", nombres_original)
print("Lista normalizada:", resultado)